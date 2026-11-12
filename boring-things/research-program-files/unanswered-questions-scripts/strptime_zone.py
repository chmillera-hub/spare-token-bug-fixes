# Tests what the %Z and %z codes of datetime.strptime return and two ways to get a time-zone-aware result (Python forum topic 86433)
import sys, datetime as dt, time
from zoneinfo import ZoneInfo
print("Python", sys.version.split()[0])
a = dt.datetime.strptime("2025-UTC", "%Y-%Z")
b = dt.datetime.strptime("2025-+0000", "%Y-%z")
print("%Z with 'UTC'   ->", repr(a), "| tzinfo:", a.tzinfo)
print("%z with '+0000' ->", repr(b), "| tzinfo:", b.tzinfo)
for name in ("UTC", "GMT", time.tzname[0], "EST", "CET", "Europe/Paris"):
    try: dt.datetime.strptime(f"2025-{name}", "%Y-%Z"); print(f"%Z accepts {name!r}: True")
    except ValueError: print(f"%Z accepts {name!r}: False")
print("local zone names known to this machine (time.tzname):", time.tzname)
c = dt.datetime.strptime("2025-UTC +0000", "%Y-%Z %z")
print("%Z and %z together ->", repr(c), "| tzname():", c.tzname())
# route 1: the text says UTC, so attach UTC after parsing
d = dt.datetime.strptime("2025-03-29 10:00 UTC", "%Y-%m-%d %H:%M %Z").replace(tzinfo=dt.timezone.utc)
print("route 1 (attach UTC after parsing):", d.isoformat())
# route 2: split the zone name off and look the zone up by name
text = "2025-03-29 10:00 Europe/Paris"
stamp, zone = text.rsplit(" ", 1)
e = dt.datetime.strptime(stamp, "%Y-%m-%d %H:%M").replace(tzinfo=ZoneInfo(zone))
print("route 2 (look the zone up by name):", e.isoformat(), "| offset:", e.utcoffset())
