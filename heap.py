生成哈夫曼树：

import heapq
 
class Node:
    def __init__(self, lc, rc, weight, height):
        self.lc = lc  # 左孩子节点
        self.rc = rc  # 右孩子节点
        self.weight = weight  # 当前节点的权重
        self.height = height  # 当前节点代表子树的高度
 
    def __gt__(self, other):
        # 优先级比较时，权重小的优先级更高，权重相同时，高度小的优先级更高
        if self.weight != other.weight:
            return self.weight > other.weight
        else:
            return self.height > other.height
 
 
# 输入获取
n = int(input())
weights = list(map(int, input().split()))
 
 
# 二叉树中序遍历
def midOrder(root, seq):
    # 中序遍历，即先遍历二叉树的左子树，再遍历二叉树的根，最后遍历二叉树的右子树
    if root.lc is not None:
        midOrder(root.lc, seq)
 
    seq.append(root.weight)
 
    if root.rc is not None:
        midOrder(root.rc, seq)
 
 
# 算法入口
def getResult():
    pq = []
 
    # 创建n个哈夫曼树节点，并加入优先队列
    for w in weights:
        heapq.heappush(pq, Node(None, None, w, 0))
 
    # 初始n个节点经过多轮合并，只剩一个节点时，那么该节点就是哈夫曼树的根节点，因此当优先队列中只剩一个节点时即可停止合并
    while len(pq) > 1:
        # 取出优先队列中前两个权值最小的节点，由于优先队列已按照 [节点权重，节点子树高度] 升序优先级，因此先出来的肯定是权重小，或者高度小的节点，即作为新节点的左子树
        lc = heapq.heappop(pq)
        rc = heapq.heappop(pq)
 
        # 将lc和rc合并，合并后新节点fa的权重，是两个子节点权重之和，fa子树高度 = rc子树高度+1; PS：rc的高度>=lc的高度
        fa_weight = lc.weight + rc.weight
        fa_height = rc.height + 1
 
        # 将合并后的新节点加入优先队列
        heapq.heappush(pq, Node(lc, rc, fa_weight, fa_height))
 
    # 最后优先队列中必然只剩一个节点，即哈夫曼树的根节点，此时对此根节点（哈夫曼树）进行中序遍历
    root = heapq.heappop(pq)
    seq = []
    midOrder(root, seq)
 
    return " ".join(map(str, seq))
 
 
# 算法调用
print(getResult())
