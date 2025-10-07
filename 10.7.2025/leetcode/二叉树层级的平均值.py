from collections import deque
import TreeNode
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        

        if not root :
            return []

        queue = deque([root])
        average = []
        while queue:
            result = []
            ql = int(len(queue))
            for i in range(ql):
                current_node = queue.popleft()
                result.append(current_node.val)
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                        ueue.append(current_node.right)
            average.append(sum(result)/ql)
        return average