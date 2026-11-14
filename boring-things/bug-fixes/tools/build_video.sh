#!/bin/bash
# Build the fast portrait video of every fix on the shelf.
# Usage: bash tools/build_video.sh WORK_FOLDER OUTPUT.mp4
# Needs: python3 with Pillow and NumPy, and ffmpeg with libx264 and aac.
# Result: 1080 by 1920, opening screen 3 s, each fix 1.5 s, closing screen 3 s,
# straight cuts, first frame is the opening screen, original music.
set -e
TOOLS="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORK="$1"; OUT="$2"
mkdir -p "$WORK/cards"
python3 "$TOOLS/video_cards.py" "$WORK/cards"
N=$(python3 -c "import json;print(len(json.load(open('$TOOLS/shelf-data.json'))['fixes']))")
LAST=$(printf "%03d" $((N+1)))
{
  echo "file 'cards/000.png'"; echo "duration 3"
  for i in $(seq 1 "$N"); do printf "file 'cards/%03d.png'\nduration 1.5\n" "$i"; done
  echo "file 'cards/$LAST.png'"; echo "duration 3"
  echo "file 'cards/$LAST.png'"
} > "$WORK/list.txt"
# One encode of still screens: small file and sharp text.
ffmpeg -v error -y -f concat -safe 0 -i "$WORK/list.txt" -vf "fps=30,format=yuv420p" \
  -c:v libx264 -crf 31 -preset veryslow -tune stillimage -x264-params keyint=900 \
  -pix_fmt yuv420p -an "$WORK/silent.mp4"
SECONDS_LONG=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$WORK/silent.mp4")
python3 "$TOOLS/video_music.py" "$SECONDS_LONG" "$WORK/music.wav"
ffmpeg -v error -y -i "$WORK/silent.mp4" -i "$WORK/music.wav" -map 0:v -map 1:a \
  -c:v copy -c:a aac -b:a 48k -shortest -movflags +faststart "$WORK/tmp_out.mp4"
mv "$WORK/tmp_out.mp4" "$OUT"
echo "built $OUT: $N fixes, $SECONDS_LONG seconds"
