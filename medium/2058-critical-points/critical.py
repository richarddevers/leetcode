import typing as t

Head = t.List[int]


def is_local_minimum(
    before: int,
    value: int,
    after: int,
) -> bool:
    return value < before and value < after


def is_local_maximum(
    before: int,
    value: int,
    after: int,
) -> bool:
    return value > before and value > after


def points(
    head: Head,
) -> Head:
    if len(head) < 4:
        return [-1, -1]

    critical_points = []

    for index, value in enumerate(head):
        if index == 0 or index == len(head) - 1:
            continue
        before = head[index - 1]
        after = head[index + 1]
        local_mini = is_local_minimum(
            before=before,
            value=value,
            after=after,
        )
        local_max = is_local_maximum(
            before=before,
            value=value,
            after=after,
        )

        if local_mini or local_max:
            critical_points.append(index + 1)

    if not critical_points:
        return [-1, -1]

    critical_points.sort()
    min_distance = critical_points[-1] - critical_points[-2]
    max_distance = critical_points[-1] - critical_points[0]

    return [min_distance, max_distance]
