type _MISSING = _MISSING


def my_func(need_value: int, not_need_value: str | _MISSING = _MISSING) -> None:
    if not_need_value is _MISSING:
        print(f"No 'not_need_value'. The 'need_value' is {need_value}")
        return
    print(f"'not_need_value' is {not_need_value} and 'need_value' is {need_value}")

my_func(1); my_func(1,"x")
