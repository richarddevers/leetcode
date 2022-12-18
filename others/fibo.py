max = 9


def fibo1(max: int) -> None:
    n1 = 0
    n2 = 1
    print(n1)
    print(n2)

    for i in range(2, max):
        next = n1 + n2
        n1 = n2
        n2 = next
        print(next)


fibo1(max=max)
