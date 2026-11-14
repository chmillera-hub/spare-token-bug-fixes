import enum
from typing import Final


class _Missing(enum.Enum):
    MISSING = enum.auto()


MISSING: Final = _Missing.MISSING


def my_func(need_value: int, not_need_value: str | _Missing = MISSING) -> None:
    if not_need_value is MISSING:
        print(f"No 'not_need_value'. The 'need_value' is {need_value}")
        return
    print(f"'not_need_value' is {not_need_value.upper()} and 'need_value' is {need_value}")

my_func(1); my_func(1,"x")
