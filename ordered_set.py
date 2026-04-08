from typing import Any


class OrderedSet:
    def __init__(self, *args: Any) -> None:
        self._unique_set: set[tuple[Any]] = set()
        self._objects = args
        temp_tuple = ()
        temp_set: set[Any] = set()
        for value in args:
            if value in temp_set:
                raise ValueError("Must not have duplicates of values")
            temp_set.add(value)
            temp_tuple = tuple([*temp_tuple, value])
            self._unique_set.add(temp_tuple)

    def __getitem__(self, key: int) -> Any:
        return self._objects[key]

    def __eq__(self, value: object) -> bool:
        if isinstance(value, OrderedSet):
            return self._unique_set == value._unique_set
        return False

    def __len__(self) -> int:
        return len(self._unique_set)

    def __repr__(self) -> str:
        return f"OrderedSet({self._objects})"
    