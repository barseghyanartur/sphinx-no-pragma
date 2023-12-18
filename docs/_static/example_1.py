from typing import Any, Optional


def my_func(arg1: Optional[Any] = None) -> int:
    # This is a very long line that should normally fail, but we want it to be present as is.
    a = arg1 or None or None or None or None or None or None or None or None or None or None  # noqa

    return "0"  # type: ignore
