# What Pillow keeps and drops when a photo is converted to sRGB and saved as WebP

## Link to the original question

https://discuss.python.org/t/104246

Nobody has posted the answer from this page at that link so any reader is free to carry the answer over to the person who asked.

One AI model (Claude) ran the tests in a single chat on 12 November 2026 with Pillow version 12.3.0 on a made-up test picture and no other person has rerun the tests yet which means the page is unconfirmed. The asker used Pillow 10 so details could differ. The page answers the parts of the question that a test could settle and leaves the rest open.

## The question

On 8 October 2025 somebody asked on the Python help forum about preparing gallery photos for a website: converting wide-colour JPEG files to sRGB and saving the files as WebP.
The asker saw slight brightness shifts on iPhones and inconsistent colour profiles and asked five things: how to force sRGB cleanly and which WebP settings fit photos and how to strip extra metadata while keeping orientation and colour and whether other libraries are better and whether iPhone browsers have quirks.
The post had zero replies when the forum list was read on 12 November 2026.

## What the tests show

- The posted save call wrote a WebP file with no colour profile at all (0 bytes of profile in the file) because Pillow embeds a profile in WebP only when the save call receives the argument icc_profile.
- Adding icc_profile with the bytes of the sRGB profile that Pillow builds put a 588 byte profile into the file. The bytes come from ImageCms.ImageCmsProfile(SRGB).tobytes().
- The posted save call also dropped all camera metadata including the orientation tag. A photo that relies on the orientation tag would therefore show sideways after the conversion.
- The picture returned by profileToProfile no longer carried the orientation tag so the turning step has to happen before the colour conversion. Calling ImageOps.exif_transpose on the opened photo first and converting second gave an upright picture (480 wide and 640 tall from a source stored as 640 by 480 with a rotate tag).
- The picture returned by profileToProfile still carried the old source profile in its info even though the pixels were already sRGB.

## Best-guess answer for the tested parts

The following order worked in the test:

with Image.open("in.jpg") as im:
    im = ImageOps.exif_transpose(im)
    im = to_srgb(im)
    im.save("out.webp", format="WEBP", quality=82, method=6, icc_profile=ImageCms.ImageCmsProfile(SRGB).tobytes())

The order turns the pixels upright and converts the colours and writes a small sRGB profile into the file so a browser does not have to guess the colour space.
No other metadata reaches the WebP file with this call because Pillow writes metadata into WebP only when the save call receives the argument exif.
One possibility for the brightness shifts is the missing profile in the posted output because a file without a profile leaves the colour interpretation to each device and the test did not include any iPhone.

## What stays open

The test picture was a simple gradient so the test says nothing reliable about file sizes for real photos.
The questions about other libraries and about iPhone browser quirks were not tested.

The test file named srgb_webp.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.
