import typing as tp

T = tp.TypeVar("T")

Container = tp.Union[
    T,
    tp.Tuple["Container", ...],
    tp.Dict[str, "Container"],
]
