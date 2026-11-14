# Draws the same thick arc and counts holes inside the band; run once with pygame and once with pygame-ce (Python forum topic 101403)
import os, math
os.environ["SDL_VIDEODRIVER"] = "dummy"; os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
import pygame
pygame.init()
name = "pygame-ce" if getattr(pygame, "IS_CE", False) else "pygame"
surf = pygame.Surface((300, 300)); surf.fill((255, 255, 255))
rect = pygame.Rect(50, 50, 200, 200); width = 6
pygame.draw.arc(surf, (0, 0, 0), rect, math.radians(20), math.radians(250), width)
drawn = holes = 0
for y in range(300):
    for x in range(300):
        r = math.hypot(x - 149.5, y - 149.5)
        ang = math.degrees(math.atan2(149.5 - y, x - 149.5)) % 360
        inside_band = 100 - width + 1.5 <= r <= 100 - 1.5 and 25 <= ang <= 245      # safely inside the band of the arc
        black = surf.get_at((x, y))[:3] == (0, 0, 0)
        drawn += black
        if inside_band and not black: holes += 1
print(f"{name} {pygame.version.ver} (SDL {'.'.join(map(str, pygame.get_sdl_version()))}): black pixels {drawn} | white holes inside the band of the arc: {holes}")
pygame.image.save(surf, f"arc_{name}.png")
