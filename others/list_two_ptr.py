prices = [1, 2, 3, 4, 5, 6]

# iter over list, then remaining


def iter1() -> None:
    l = 0
    r = 1
    while r < len(prices):
        print(f"left:{prices[l]}")
        for i in range(r, len(prices)):
            print(f"right:{prices[i]}")
        print(f"right:{prices[r]}")
        l += 1
        r += 1
    # not very eficient, something like O(n^n-1)
    # but spatial is O(1) (i think :/)


iter1()
