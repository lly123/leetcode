# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def _build_tree(arr, pos):
    arr_len = len(arr)

    if not arr[pos]:
        return None

    node = TreeNode(arr[pos])

    left_tree_root_pos = pos * 2 + 1
    if left_tree_root_pos < arr_len:
        node.left = _build_tree(arr, left_tree_root_pos)

    right_tree_root_pos = pos * 2 + 2
    if right_tree_root_pos < arr_len:
        node.right = _build_tree(arr, right_tree_root_pos)

    return node


def build_tree(arr):
    return _build_tree(arr, 0)
