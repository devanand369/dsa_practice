from linked_list import LinkedList

def merge_sort(linked_list):
    """
    Sorts a linked list in ascending order
    - Recursively divide the linked list into sublist containing a single node
    - Repeatedly merge the sublists to prodece sorted sublists untill one remains

    Returns a sorted linked list
    """

    if linked_list.size == 1:
        return linked_list

    elif linked_list.head == None:
        return linked_list

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    
    return merge(left, right)

def split(linked_list):
    """
    Divide the unsorted list at midpoint into sublist
    """

    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None

        return left_half, right_half

    else:
        size = linked_list.size() 
        mid = size//2

        mid_node = linked_list.node_at_index(mid-1)

        left_half = linked_list
        right_half = LinkedList()
        right_half.head = right_half.next_node
        mid_node.next_node = None

        return left_half, right_half

def merge(left, right):
    """
    Merges two linked lists, sotring data in nodes
    Returns a new, merge list
    """
    