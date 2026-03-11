"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Constraints:

    The number of the nodes in the list is in the range [0, 104].
    -105 <= Node.val <= 105
    pos is -1 or a valid index in the linked-list.

Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def solution(head: Optional[ListNode]) -> bool:
    """
    This method should treturn true if a list has a cycle and false if it has not.

    In this task it seems like hashmap should be utilised to track the nodes
    we have visited - and after moving to node.next and finding node we already
    have registered - return its position.

    Since position of this graph is essentially what we are looking for
    (-1 of no cycle) we need to keep track of the amount of jumps we have done.
    It ought to be incremented with each jump.

    Base case would be - either x.next is none - so we ended and there was no cycle.
    In this case -1 is returned

    Otherwise - we came back and hit position already registerd in the hashmap
    then we return the position and the truth.

    What is not really clear is what kind of key we should use.
    - Just position - insufficient. Since how do we verify if (in case of the loop)
    that the node we have entered is actually the right one? We'd end up in an infinite loop
    - Just the value - insufficient. Since two nodes can have the same value.

    So the only (that i see) solution it to track both in a tuple (pos, val).
    That way when we enter into the cycle we increment the position.

    Something isn't right

    So if we have (pos, val). And we go over the graph, we have something like this:

    or let's change our thought

    let's say position to value

    0 : 3
    1 : 2
    2 : 3
    3 : -4
    4 : 2

    no, that doesn't work - we are left with nothing.

    Actually - let's not overthink.

    We have a known number of nodes? No we dont. we just get the head. Let's think of it differently
    could it be a recursion problem?

    yeah we could solve it as recursion - but that doesn't change - that we need to track it


    if we did it by going with two pointers approach:

    A would stay, other would

    --- asked claude for guidance - was overcomplicating

    Okay let's simplify it - for some reason i forgot id() exists and was looking
    for a memory address. Really out of shape.
    """

    map = set() # i'll not use a dictionary - just a set

    # okay - main condition - if head is none -> no cycle since we have finished
    # edge case - node can point to itself!
    while head is not None:

        # in case we have traversed a node - it must be in the set
        if id(head) in map:
            # cycle found
            return True

        # saving the traversed node to the set (hashmap)
        map.add(id(head))

        # iterating
        head = head.next

    # when we're out of while - we're done - no cycle
    return False

def solution_tortoise(head: Optional[ListNode]) -> bool:
    """
    Okay, here let's think through the O(1) solution which is basically two
    pointer solution.

    If I understand correctly - the point is that if one pointer moves by +1
    and the other by +2 - if there is no cycle - they can't meet. If they do
    there is a cycle.

    I'll code this and then we'll check if my understanding is correct.

    Will try to first just assign the tortoise to point to head and hare to the
    next - not really sure if this +2 is correct at the moment.

    No that's wrong - I mean they would just chase each other and not meet.
    They need to start at one ponit
    """
    # first of all - while will catch the head == None
    # edge case in this instance is if there is a single node.

    # single node cannot have a cycle - unless to itself;
    # but then they'd meet - since they don't change position
    # if head.next is None:
    # return False


    tortoise = head
    hare = head

    # optimization - do not check tortoise

    while hare is not None and hare.next is not None:
        tortoise = tortoise.next
        hare = hare.next.next

        if tortoise == hare:
            return True


    return False


if __name__ == "__main__":

    # definition of the list from example
    head = ListNode(3)
    head.next = ListNode(2)
    cycle_object = head.next
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = cycle_object

    # ensuring no cycle also works well
    no_cycle = ListNode(1)


    print(solution_tortoise(head))
    print(solution_tortoise(no_cycle))
