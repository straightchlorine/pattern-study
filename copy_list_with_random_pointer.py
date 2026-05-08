"""
A linked list of length n is given such that each node contains an additional
random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand
new nodes, where each new node has its value set to the value of its corresponding
original node. Both the next and random pointer of the new nodes should point to
new nodes in the copied list such that the pointers in the original list and copied
list represent the same list state. None of the pointers in the new list should
point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where

X.random --> Y,

then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes.
Each node is represented as a pair of [val, random_index] where:

    val: an integer representing Node.val
    random_index: the index of the node (range from 0 to n-1) that the
        random pointer points to, or null if it does not point to any node.

Your code will only be given the head of the original linked list.

https://assets.leetcode.com/uploads/2019/12/18/e1.png

```
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
```

https://assets.leetcode.com/uploads/2019/12/18/e2.png

```
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
```

https://assets.leetcode.com/uploads/2019/12/18/e3.png

```
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
```

Constraints:

    0 <= n <= 1000
    -104 <= Node.val <= 104
    Node.random is null or is pointing to some node in the linked list.
"""


class Node:
    def __init__(
        self, x: int, next: "Node | None" = None, random: "Node | None" = None
    ):
        self.val = int(x)
        self.next = next
        self.random = random


def solution(head: Node | None):
    if head is None:
        return head

    cloned = {}

    def dfs(node: Node) -> Node:
        if node in cloned:
            return cloned[node]

        new_node = Node(node.val)
        cloned[node] = new_node

        if node.next is not None:
            new_next = dfs(node.next)
            new_node.next = new_next

        if node.random is not None:
            new_random = dfs(node.random)
            new_node.random = new_random

        return new_node

    return dfs(head)


def solution_iter(head: Node | None):
    if head is None:
        return None
    clone = {}
    cur = head

    while cur:
        clone[cur] = Node(cur.val)
        cur = cur.next

    cur = head
    while cur:
        clone[cur].next = clone.get(cur.next)
        clone[cur].random = clone.get(cur.random)
        cur = cur.next

    return clone[head]


def solution_mem(head: Node | None):
    if head is None:
        return None

    cur = head
    while cur:
        clone = Node(cur.val, cur.next)
        cur.next = clone
        cur = clone.next

    cur = head
    while cur:
        if cur.random:
            cur.next.random = cur.random.next
        cur = cur.next.next
    cur, new_head = head, head.next
    while cur:
        clone = cur.next
        cur.next = clone.next
        clone.next = clone.next.next if clone.next else None
        cur = cur.next
    return new_head


def printList(head: Node | None):
    if head is None:
        return []

    current = head
    while current is not None:
        print(current.val, end=" ")
        print("rand: ", "null" if current.random is None else current.random.val)
        current = current.next


if __name__ == "__main__":
    nnnn_head = Node(1)
    nnn_head = Node(10, nnnn_head)
    nn_head = Node(11, nnn_head)
    n_head = Node(13, nn_head)
    head = Node(7, n_head)

    head.random = nnnn_head
    n_head.random = head
    nn_head.random = nnnn_head
    nnn_head.random = nn_head
    nnnn_head.random = head

    printList(solution(head))
