import ast
import typing as t

ListNode = t.List[int]


def two_numbers(
    *,
    l1: ListNode,
    l2: ListNode,
) -> ListNode:
    l1.reverse()
    l2.reverse()

    l1_as_string = "".join([str(elt) for elt in l1])
    l2_as_string = "".join([str(elt) for elt in l2])

    l1_ast = ast.literal_eval(l1_as_string)
    l2_ast = ast.literal_eval(l2_as_string)
    l3 = l1_ast + l2_ast

    result = [int(elt) for elt in list(str(l3))]
    result.reverse()
    return result
