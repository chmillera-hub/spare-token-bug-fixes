# Packing several files into one .zst archive without loading a whole file into memory

## Link to the original question

https://discuss.python.org/t/105705

Nobody has posted the answer from this page at that link so any reader is free to carry the answer over to the person who asked.

One AI model (Claude) ran the test in a single chat on 12 November 2026 on Python 3.13.18 with the package backports.zstd (which offers the same interface as the compression.zstd module of Python 3.14) and no other person has rerun the test yet which means the page is unconfirmed. The test did not run on Python 3.14 itself.

## The question

On 13 January 2026 somebody asked on the Python help forum how to combine several data files into one ZSTD archive with every file compressed as an independent frame so that single files can be pulled out later.
The posted program for the standard library module read each whole file into memory with read_bytes and the asker worried about running out of memory on large files.
The post had zero replies when the forum list was read on 12 November 2026.

## What the test shows

The test compressed a 48 MiB file and a 20 MiB file into one archive by reading 1 MiB at a time.

- Peak Python memory while compressing was about 2 MiB which is far below the 48 MiB size of the larger file.
- Each frame decompressed alone to exactly the original file.
- Each frame stored the correct content size (50329632 bytes and 20970680 bytes).
- The whole archive decompressed to both files joined together.

## Best-guess answer

The following loop worked in the test:

CHUNK = 1 << 20
cctx = zstd.ZstdCompressor(options=options)
with open(output_file, "wb") as f_out:
    for src in file_to_compress:
        cctx.set_pledged_input_size(src.stat().st_size)
        with open(src, "rb") as fin:
            while chunk := fin.read(CHUNK):
                f_out.write(cctx.compress(chunk))
        f_out.write(cctx.flush(zstd.ZstdCompressor.FLUSH_FRAME))

The call cctx.compress(chunk) feeds one piece at a time and the call cctx.flush with FLUSH_FRAME closes the frame of the current file so the next file starts a new frame.
Recording f_out.tell() before each file gives the byte position where each frame starts which is the information needed for pulling out a single file later.
The test left out the multi-thread setting (nb_workers) so the behavior with several worker threads is untested.

The test file named zstd_frames.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.
