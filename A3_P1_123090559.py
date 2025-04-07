
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = {}

    def add_child(self, child, attack_point):
        self.children[child] = attack_point


class Tree:
    def __init__(self, root_value):
        self.nodes = {root_value: TreeNode(root_value)}

    def add_edge(self, u, v, attack_point):
        if u not in self.nodes:
            self.nodes[u] = TreeNode(u)
        if v not in self.nodes:
            self.nodes[v] = TreeNode(v)

        self.nodes[u].add_child(self.nodes[v], attack_point)
        self.nodes[v].add_child(self.nodes[u], attack_point)

    def find_max_hp_path(self):
        max_hp = float('-inf')

        def dfs(node, parent, current_hp, current_mp):
            nonlocal max_hp

            if len(node.children) == 1 and list(node.children.keys())[0] == parent:
                max_hp = max(max_hp, current_hp)
                return

            for child, attack_point in node.children.items():
                if child == parent:
                    continue
                new_mp = current_mp + 1
                if new_mp >= attack_point:
                    new_hp = current_hp
                else:
                    new_hp = current_hp + (attack_point - new_mp)
                dfs(child, node, new_hp, new_mp)

        root = self.nodes[root_value]
        dfs(root, None, current_hp=0, current_mp=0)
        return max_hp


n, m, root_value = map(int, input().split())
tree = Tree(root_value)
for i in range(m):
    u, v, attack_point = map(int, input().split())
    tree.add_edge(u, v, attack_point)

max_final_hp = tree.find_max_hp_path()
print(max_final_hp)


