# Tests writing several files into one .zst archive as independent frames without reading a whole file into memory
# (Python forum topic 105705). Python 3.14 has "from compression import zstd"; older Pythons can use the backports.zstd package.
import os, sys, tempfile, tracemalloc
try:
    from compression import zstd
    origin = "compression.zstd (standard library)"
except ImportError:
    from backports import zstd
    origin = "backports.zstd (same interface for older Python versions)"
print("Python", sys.version.split()[0], "|", origin)

CHUNK = 1 << 20   # read 1 MiB at a time

def write_frames(sources, output_file):
    options = {zstd.CompressionParameter.content_size_flag: True, zstd.CompressionParameter.checksum_flag: True}
    cctx = zstd.ZstdCompressor(options=options)
    offsets = []
    with open(output_file, "wb") as f_out:
        for src in sources:
            offsets.append(f_out.tell())
            cctx.set_pledged_input_size(os.path.getsize(src))
            with open(src, "rb") as fin:
                while chunk := fin.read(CHUNK):
                    f_out.write(cctx.compress(chunk))
            f_out.write(cctx.flush(zstd.ZstdCompressor.FLUSH_FRAME))   # ends the frame for this file
    return offsets

tmp = tempfile.mkdtemp()
sources = []
for i, size_mb in enumerate((48, 20)):
    p = os.path.join(tmp, f"chunk_{i}.ndjson")
    with open(p, "wb") as f:
        line = (b'{"id": %d, "text": "' % i) + os.urandom(30).hex().encode() + b'"}\n'
        for _ in range(size_mb): f.write(line * ((1 << 20) // len(line)))
    sources.append(p)
out = os.path.join(tmp, "dataset.zst")
tracemalloc.start()
offsets = write_frames(sources, out)
peak = tracemalloc.get_traced_memory()[1]; tracemalloc.stop()
print("input sizes (MiB):", [round(os.path.getsize(p) / 2**20, 1) for p in sources], "| peak Python memory while compressing (MiB):", round(peak / 2**20, 2))
blob = open(out, "rb").read()
ends = offsets[1:] + [len(blob)]
for i, (a, b) in enumerate(zip(offsets, ends)):
    frame = blob[a:b]
    info = zstd.get_frame_info(frame)
    data = zstd.decompress(frame)
    print(f"frame {i}: starts at byte {a} | stored content size {info.decompressed_size} | decompresses alone to the original file: {data == open(sources[i], 'rb').read()}")
print("whole archive decompresses to both files joined:", zstd.decompress(blob) == b"".join(open(p, "rb").read() for p in sources))
