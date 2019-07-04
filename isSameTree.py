from util import TreeNode, build_tree


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True

        if (not p and q) or (p and not q):
            return False

        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False


p = build_tree([1, 2])
q = build_tree([1, None, 2])
o = Solution()
ret = o.isSameTree(p, q)
print(ret)
