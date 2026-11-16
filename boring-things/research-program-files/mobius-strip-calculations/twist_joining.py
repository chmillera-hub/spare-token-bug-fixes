# Joining Mobius strips end to end: what does the joined strip look like?
# Part 1 (shape): each strip is cut crosswise and the cut ends are joined straight across
#   (no extra flip added at a joint) so the parts form one longer closed band.
#   The program builds the joined band as points in space and measures:
#   one-sided or two-sided, number of edges, and how many times the edges wind through each other.
# Part 2 (energy): a simple elastic model in which twisting and bending each cost energy.
#   The twist is free to spread along the joined band and the program reports how much energy is freed.
# Needs only Python with numpy.
import numpy as np

def build(twists, n_per=400, width=0.25):
    """twists: list of half-twist counts, +1 right-handed, -1 left-handed. Each part has length 1."""
    parts = len(twists); n = n_per * parts
    s = np.arange(n + 1) / n                      # 0..1 around the joined loop
    R = parts / (2 * np.pi)                       # loop length = number of parts
    # twist angle profile: each part turns by (half twists) * pi, smoothly inside its own part
    phi = np.zeros(n + 1)
    for k, h in enumerate(twists):
        a, b = k * n_per, (k + 1) * n_per
        u = np.linspace(0, 1, n_per + 1)
        phi[a:b + 1] = phi[a] + h * np.pi * u
    ang = 2 * np.pi * s
    core = np.stack([R * np.cos(ang), R * np.sin(ang), 0 * ang], 1)
    radial = np.stack([np.cos(ang), np.sin(ang), 0 * ang], 1)
    up = np.array([0, 0, 1.0])
    d = np.cos(phi)[:, None] * radial + np.sin(phi)[:, None] * up     # direction across the band
    tang = np.stack([-np.sin(ang), np.cos(ang), 0 * ang], 1)
    normal = np.cross(tang, d)
    return core, d, normal, width

def linking(a, b):
    """Gauss linking number of two closed polylines (rounded to nearest half)."""
    a0, a1 = a[:-1], a[1:]; b0, b1 = b[:-1], b[1:]
    ma, da = (a0 + a1) / 2, a1 - a0; mb, db = (b0 + b1) / 2, b1 - b0
    tot = 0.0
    for i in range(len(ma)):
        r = ma[i] - mb
        tot += np.sum(np.einsum('ij,ij->i', np.cross(da[i][None, :], db), r) / np.linalg.norm(r, axis=1) ** 3)
    return tot / (4 * np.pi)

def describe(twists):
    core, d, normal, w = build(twists)
    flipped = np.dot(normal[0], normal[-1]) < 0
    e1, e2 = core + w * d, core - w * d
    if flipped:   # one-sided: the two edge traces join into one long edge
        edge = np.vstack([e1[:-1], e2])
        lk = linking(edge, core)
        return dict(total=sum(twists), sides=1, edges=1, wind=round(lk, 2), what="edge around center line")
    lk = linking(e1, e2)
    return dict(total=sum(twists), sides=2, edges=2, wind=round(lk, 2), what="edge around other edge")

L, Rh = -1, +1
cases = [("one left-handed strip alone", [L]), ("one right-handed strip alone", [Rh]),
         ("left joined to right", [L, Rh]), ("left joined to left", [L, L]), ("right joined to right", [Rh, Rh]),
         ("left + left + right", [L, L, Rh]), ("left + left + left", [L, L, L]),
         ("left + right + left + right", [L, Rh, L, Rh]), ("four left", [L, L, L, L])]
print("PART 1: shape of the joined band")
for name, tw in cases:
    r = describe(tw)
    print(f"  {name}: total half twists {r['total']:+d} | sides {r['sides']} | edges {r['edges']} | winding ({r['what']}) {r['wind']:+.2f}")

print("\nPART 2: energy in a simple elastic model (twist stiffness 1, bend stiffness 1, each strip length 1)")
def twist_energy(total_half_twists, length):   # twist spread evenly
    return 0.5 * (total_half_twists * np.pi) ** 2 / length
def bend_energy(length):                        # round loop
    return 0.5 * (2 * np.pi) ** 2 / length
before = 2 * (twist_energy(1, 1) + bend_energy(1))
for name, tw in [("left joined to right", [L, Rh]), ("left joined to left", [L, L])]:
    after_t, after_b = twist_energy(sum(tw), 2), bend_energy(2)
    print(f"  {name}: before {before:.2f} (twist {2*twist_energy(1,1):.2f} + bend {2*bend_energy(1):.2f}) | after twist {after_t:.2f} + bend {after_b:.2f} = {after_t+after_b:.2f} | freed {100*(before-after_t-after_b)/before:.0f}% of all energy | twist energy freed {100*(2*twist_energy(1,1)-after_t)/(2*twist_energy(1,1)):.0f}%")

# numerical relaxation: let the twist angle spread along the joined band and watch the twist energy
def relax(tw, n=200, steps=200000, report=(0, 2000, 20000, 200000)):
    ds = 2.0 / n; phi = np.zeros(n + 1)
    # each strip starts with its half twist squeezed into the middle fifth of its own half
    for k, h in enumerate(tw):
        a = int((k + 0.4) * n / 2); b = int((k + 0.6) * n / 2)
        phi[a:b + 1] += h * np.pi * np.linspace(0, 1, b - a + 1); phi[b + 1:] += h * np.pi
    total = phi[-1] - phi[0]; out = []
    for t in range(steps + 1):
        if t in report: out.append(round(float(0.5 * np.sum(np.diff(phi) ** 2) / ds), 3))
        lap = np.zeros_like(phi)
        lap[1:-1] = phi[2:] - 2 * phi[1:-1] + phi[:-2]
        lap[0] = phi[1] - 2 * phi[0] + (phi[-2] - total)   # the loop closes on itself
        phi += 0.25 * lap; phi[-1] = phi[0] + total
    return out
print("\n  twist energy while the twist spreads (start, early, middle, settled):")
print("   left joined to right:", relax([L, Rh]))
print("   left joined to left: ", relax([L, L]))
