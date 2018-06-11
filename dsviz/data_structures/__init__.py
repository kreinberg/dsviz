try:
    from dsviz.data_structures.array_stack import ArrayStack
except ImportError as e:
    print(e)
    print('Failed to import ArrayStack')

try:
    from dsviz.data_structures.avl_tree import AVLTree
except ImportError as e:
    print('Failed to import AVLTree')

try:
    from dsviz.data_structures.binary_heap import BinaryHeap
except ImportError as e:
    print('Failed to import BinaryHeap')

try:
    from dsviz.data_structures.binary_search_tree import BinarySearchTree
except ImportError as e:
    print('Failed to import BinarySearchTree')

try:
    from dsviz.data_structures.double_ended_queue import DoubleEndedQueue
except ImportError as e:
    print('Failed to import DoubleEndedQueue')

try:
    from dsviz.data_structures.doubly_linked_list import DoublyLinkedList
except ImportError as e:
    print('Failed to import DoublyLinkedList')

try:
    from dsviz.data_structures.single_ended_queue import SingleEndedQueue
except ImportError as e:
    print('Failed to import SingleEndedQueue')

try:
    from dsviz.data_structures.singly_linked_list import SinglyLinkedList
except ImportError as e:
    print('Failed to import SinglyLinkedList')
