from typing import Any


class OrderedSet:
    def __init__(self, *args: Any) -> None:
        self._unique_set: set[tuple[Any]] = set()
        self._objects = args
        temp_tuple = ()
        temp_values: list[Any] = []
        for value in args:
            if value in temp_values:
                raise ValueError("Must not have duplicates of values")
            temp_values.append(value)
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


class OtimizedOrderedSet:
    def __init__(self, *args: Any) -> None:
        self._objects = args
        temp_values: list[Any] = []
        for value in args:
            if value in temp_values:
                raise ValueError("Cannot contain duplicate values")
            temp_values.append(value)

    def __getitem__(self, key: int) -> Any:
        return self._objects[key]

    def __eq__(self, value: object) -> bool:
        if isinstance(value, OtimizedOrderedSet):
            return self._objects == value._objects
        return False

    def __len__(self) -> int:
        return len(self._objects)

    def __repr__(self) -> str:
        return f"OtimizedOrderedSet({self._objects})"
