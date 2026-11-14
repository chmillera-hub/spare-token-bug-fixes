# Tests what Pillow keeps when a wide-colour JPEG is converted to sRGB and saved as WebP (Python forum topic 104246)
import io, PIL
from PIL import Image, ImageCms, ImageOps
print("Pillow", PIL.__version__)
SRGB = ImageCms.createProfile("sRGB")
srgb_bytes = ImageCms.ImageCmsProfile(SRGB).tobytes()
print("size of the sRGB profile that Pillow builds:", len(srgb_bytes), "bytes")

# a made-up source photo: gradient image tagged with a different colour profile and an orientation tag
img = Image.linear_gradient("L").resize((640, 480)).convert("RGB")
exif = Image.Exif(); exif[0x0112] = 6; exif[0x010F] = "CameraMaker"      # orientation = rotate 90 degrees, plus a maker tag
buf = io.BytesIO(); img.save(buf, "JPEG", quality=90, icc_profile=srgb_bytes + b"", exif=exif); buf.seek(0)

def to_srgb(im):
    if "icc_profile" in im.info:
        src = ImageCms.ImageCmsProfile(io.BytesIO(im.info["icc_profile"]))
        im2 = ImageCms.profileToProfile(im, src, SRGB, renderingIntent=0, outputMode="RGB")
    else:
        im2 = im.convert("RGB")
    return im2

with Image.open(buf) as im:
    print("source: has profile:", "icc_profile" in im.info, "| orientation tag:", im.getexif().get(0x0112), "| size:", im.size)
    conv = to_srgb(im)
    print("after profileToProfile: info still carries a profile:", "icc_profile" in conv.info, "| same bytes as the source profile:", conv.info.get("icc_profile") == im.info["icc_profile"])
    def saved(label, image, **kw):
        out = io.BytesIO(); image.save(out, "WEBP", **kw); n = out.tell(); out.seek(0)
        with Image.open(out) as w:
            w.load()
            print(f"{label}: {n} bytes | profile in file: {'icc_profile' in w.info} ({len(w.info.get('icc_profile', b''))} bytes) | orientation tag in file: {w.getexif().get(0x0112)} | maker tag in file: {w.getexif().get(0x010F)} | size {w.size}")
    saved("posted save call (quality=82, method=6)        ", conv, quality=82, method=6)
    saved("same call with icc_profile=sRGB bytes          ", conv, quality=82, method=6, icc_profile=srgb_bytes)
    print("exif orientation tag still present after profileToProfile:", conv.getexif().get(0x0112))
    out = io.BytesIO(); conv.save(out, "JPEG"); out.seek(0)
    with Image.open(out) as j:
        print("saving the converted image as JPEG without extras embeds the old source profile:", j.info.get("icc_profile") == im.info["icc_profile"])
    upright = to_srgb(ImageOps.exif_transpose(im))          # turn the picture upright first, then convert the colours
    saved("exif_transpose first, then convert, then save  ", upright, quality=82, method=6, icc_profile=srgb_bytes)
    saved("lossless=True for comparison                   ", upright, lossless=True, method=6)
