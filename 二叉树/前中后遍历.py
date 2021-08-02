"""
二叉树的前中后遍历，非递归
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def dlr(root):
    """前序遍历"""
    ans = []
    st = []
    if root: st.append(root)
    while st:
        node = st.pop()
        ans.append(node.val)
        if node.right: st.append(node.right)
        if node.left: st.append(node.left)
    return ans

def ldr(root):
    """中序遍历"""
    ans = []
    st = []
    curr = root
    while curr or st:
        while curr:
            st.append(curr)
            curr = curr.left
        curr = st.pop()
        ans.append(curr.val)
        curr = curr.right
    return ans

def lrd(root):
    """后序遍历"""
    ans = []
    st = []
    if root: st.append(root)
    while st:
        node = st.pop()
        ans.insert(0, node.val)
        if node.left: st.append(node.left)
        if node.right: st.append(node.right)
    return ans

def arr2tree(arr):
    root = TreeNode(arr[0])
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(arr):
        node = nodeQueue[front]
        front += 1
        item = arr[index]
        index += 1
        if item != None:
            node.left = TreeNode(item)
            nodeQueue.append(node.left)
            if index >= len(arr): break
        item = arr[index]
        index += 1
        if item != None:
            node.right = TreeNode(item)
            nodeQueue.append(node.right)
    return root

if __name__ == '__main__':
    arr = [5,3,6,2,4,None,8,1,None,None,None,7,9]
    root = arr2tree(arr)
    print("前序遍历: ", dlr(root))
    print("中序遍历: ", ldr(root))
    print("后序遍历: ", lrd(root))