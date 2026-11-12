from typing import reveal_type

a = [1, 2]                      # no declared type on the left
reveal_type(a)                  # both checkers infer the type from the right side

b: list[object] = [1, 2]        # declared type on the left is used while checking the right side: accepted
c: list[object] = a             # the right side already has the type list[int]: rejected

d: list[float] = []             # an empty list gets its element type from the left side
reveal_type(d)
e = []                          # nothing on the left to help
