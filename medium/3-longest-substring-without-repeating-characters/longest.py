import typing as t


def has_unique_char(s1: str) -> bool:
    as_set = set(list(s1))
    return len(as_set) == len(s1)


def substring(
    s1: str,
):
    if len(s1) == 1:
        return 1

    visited: t.Dict[str, int] = {}
    i = 0
    j = i + 1
    while i < len(s1):
        while j < len(s1) + 1:
            if i == j:
                j += 1
                continue

            window = s1[i:j]
            if visited.get(window):
                j += 1
                continue

            if has_unique_char(window):
                visited[window] = len(window)

            j += 1
        j = i + 1
        i += 1

    return max([v for k, v in visited.items()])
