import typing as t

can: t.List[int] = [2, 45, 19, 23, 12, 50, 8]

# for loop
for elt in can:
    print(f"for case {elt}")

# while
i = 0
while i < len(can):
    print(f"while case {can[i]}")
    i += 1

# for big list use generator
def iter_generator(
    can: t.List[int],
):
    for elt2 in can:
        yield elt2


for elt3 in iter_generator(
    can=can,
):
    print(f"generator case {elt3}")


# recursively


def deep(
    i: int,
    can: t.List[int],
):
    if i >= len(can):
        return
    print(f"recursive case {can[i]}")
    deep(
        i=i + 1,
        can=can,
    )


deep(
    i=0,
    can=can,
)
