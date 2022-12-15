import typing as t


def top(
    nums: t.List[int],
    k: int,
):
    count: t.Dict[int, int] = {}

    for n in nums:
        count[n] = 1 + count.get(n, 0)

    sorted_dict = sorted(
        count.items(),
        key=lambda x: x[1],
        reverse=True,
    )

    result = [int(elt[0]) for elt in sorted_dict][:k]

    return result


def test_top():
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    expected = [1, 2]

    result = top(
        nums=nums,
        k=k,
    )

    assert result == expected
