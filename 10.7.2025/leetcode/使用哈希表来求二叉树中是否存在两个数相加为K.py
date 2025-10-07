import TreeNode
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        def dfs(node):
            if not node:
                return False
            current_node = node
            complement = k - current_node.val
            if complement in seen:
                return True
            else:
                seen.add(current_node.val)
            return dfs(node.left) or dfs(node.right)
        return dfs(root)
##集合用来确认是否存在非常方便。此处思路就是计算当前节点和k的差值，如果没有的话就讲当前节点放入哈希表中
# 继续遍历其他节点看其他节点和k的差值是否存在在哈希表中。如果存在就表明之前遍历的数值有一个和当前节点想相加的数值等于K    