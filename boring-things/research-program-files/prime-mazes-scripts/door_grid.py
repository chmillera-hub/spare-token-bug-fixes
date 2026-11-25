"""Door grids from the digits of primes.

Rule (proposed by the repository author): a square grid of rooms. Each room reads one digit and opens one door:
digit 1 -> north, 2 -> east, 3 -> south, 4 -> west, then the cycle repeats (5 north, 6 east, 7 south, 8 west, 9 north, 0 west).
A door opened from either side joins the two rooms. A door that points outside the grid joins nothing.
Digits fill the grid row by row starting at the top left room.

For a grid of k by k rooms a prime with k*k digits fills the grid exactly.
finish  = a walk through open doors exists from the top left room to the bottom right room
longest = the most rooms any walk can visit without entering a room twice
tube    = longest equals the number of rooms (one hallway through every room)
"""
from grid_tools import *

out = {}
# ---------- every 4 digit prime on the 2 by 2 grid ----------
p4 = [p for p in range(1000, 10000) if gmpy2.is_prime(p)]
m4 = [(p, measure(digits_to_dirs(str(p)), 2)) for p in p4]
out["grid2_all_4_digit_primes"] = {
    "primes": len(p4), "finish": sum(m["finish"] for _, m in m4),
    "longest_counts": {str(L): sum(m["longest"] == L for _, m in m4) for L in range(1, 5)},
    "tube_primes_first_20": [p for p, m in m4 if m["longest"] == 4][:20],
    "tube_primes_count": sum(m["longest"] == 4 for _, m in m4)}
all4 = [measure(digits_to_dirs("%04d" % x), 2) for x in range(1000, 10000)]
out["grid2_all_4_digit_numbers"] = {"numbers": 9000, "finish": sum(m["finish"] for m in all4), "tube": sum(m["longest"] == 4 for m in all4)}
print("2x2 done", out["grid2_all_4_digit_primes"], flush=True)

# ---------- every 9 digit prime on the 3 by 3 grid (table of all 4^9 door patterns) ----------
T_long = np.zeros(4 ** 9, dtype=np.int8); T_fin = np.zeros(4 ** 9, dtype=bool); T_reg = np.zeros(4 ** 9, dtype=np.int8)
for code in range(4 ** 9):
    dirs = [(code >> (2 * i)) & 3 for i in range(9)]
    m = measure(dirs, 3); T_long[code] = m["longest"]; T_fin[code] = m["finish"]; T_reg[code] = m["regions"]
print("3x3 table done", flush=True)
lim = 10 ** 9; half = lim // 2
sv = np.ones(half, dtype=bool); sv[0] = False            # index i stands for the odd number 2i+1
for i in range(1, int(lim ** 0.5) // 2 + 1):
    if sv[i]:
        p = 2 * i + 1; sv[(p * p) // 2::p] = False
lo = (10 ** 8) // 2
counts = np.zeros(4 ** 9, dtype=np.int64); tube_examples = []; total = 0; tube_small = None; tube_big = None
CH = 25_000_000
for a in range(lo, half, CH):
    idx = np.nonzero(sv[a:min(a + CH, half)])[0].astype(np.int64) + a
    pr = 2 * idx + 1; total += len(pr)
    code = np.zeros(len(pr), dtype=np.int64); q = pr.copy()
    for pos in range(8, -1, -1):              # last digit belongs to room 8 (bottom right)
        d = q % 10; q //= 10
        code |= ((d - 1) % 4) << (2 * pos)
    counts += np.bincount(code, minlength=4 ** 9)
    tubes = pr[T_long[code] == 9]
    if len(tubes):
        if tube_small is None: tube_small = int(tubes[0]); tube_examples = tubes[:15].tolist()
        tube_big = int(tubes[-1])
del sv
out["grid3_all_9_digit_primes"] = {
    "primes": int(total), "finish": int(counts[T_fin].sum()),
    "longest_counts": {str(L): int(counts[T_long == L].sum()) for L in range(1, 10)},
    "tube_primes_count": int(counts[T_long == 9].sum()), "smallest_tube_prime": tube_small, "largest_tube_prime": tube_big,
    "first_15_tube_primes": tube_examples,
    "average_longest": float((counts * T_long).sum() / total), "average_regions": float((counts * T_reg).sum() / total)}
# all 9 digit numbers = every pattern weighted by how many digit strings give the pattern (first digit not 0)
w_first = np.array([3, 2, 2, 2])   # north 1 5 9; east 2 6; south 3 7; west 4 8 (no leading 0)
w_rest = np.array([3, 2, 2, 3])    # west also takes the digit 0
codes = np.arange(4 ** 9); wt = w_first[codes & 3].astype(np.float64)
for i in range(1, 9): wt *= w_rest[(codes >> (2 * i)) & 3]
out["grid3_all_9_digit_numbers"] = {"numbers": int(wt.sum()), "finish_share": float(wt[T_fin].sum() / wt.sum()),
    "tube_share": float(wt[T_long == 9].sum() / wt.sum()), "average_longest": float((wt * T_long).sum() / wt.sum())}
print("3x3 done", out["grid3_all_9_digit_primes"], out["grid3_all_9_digit_numbers"], flush=True)

# ---------- samples for larger grids: primes against plain random digit strings ----------
rng = random.Random(5); rows = []
for k, reps in ((4, 20000), (5, 20000), (6, 8000), (7, 4000), (8, 3000), (10, 2000), (15, 600), (20, 300)):
    def batch(make):
        fin = 0; longs = []; regs = []; big = []; champ = (0, None)
        for _ in range(reps):
            s = make(); m = measure(digits_to_dirs(s), k)
            fin += m["finish"]; longs.append(m["longest"]); regs.append(m["regions"]); big.append(m["largest_region"])
            if m["longest"] > champ[0]: champ = (m["longest"], s)
        return {"finish_share": fin / reps, "average_longest": sum(longs) / reps, "max_longest": max(longs), "champion": champ[1],
                "average_regions": sum(regs) / reps, "average_largest_region": sum(big) / reps}
    nd = k * k
    pr = batch(lambda: str(random_prime(nd, rng)))
    rd = batch(lambda: str(rng.randrange(10 ** (nd - 1), 10 ** nd)))
    rows.append({"grid": k, "rooms": nd, "samples": reps, "primes": pr, "random_numbers": rd}); print(k, pr["finish_share"], rd["finish_share"], pr["average_longest"], rd["average_longest"], pr["max_longest"], flush=True)
out["larger_grids"] = rows
json.dump(out, open("door_grid_results.json", "w"), indent=1)
