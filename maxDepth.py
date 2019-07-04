from util import TreeNode, build_tree


class Solution:
    def depth(self, root, level):
        if not root:
            return 0

        return max(level, self.depth(root.left, level + 1), self.depth(root.right, level + 1))

    def maxDepth(self, root: TreeNode) -> int:
        return self.depth(root, 1)


tree = build_tree([3, 9, 20, None, None, 15, 7])
o = Solution()
ret = o.maxDepth(tree)
print(ret)
