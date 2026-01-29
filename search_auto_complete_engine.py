class Trie:
    def __init__(self):
        self.child = {}
        self.end = False

root = Trie()

def insert(word):
    cur = root
    for c in word:
        cur = cur.child.setdefault(c, Trie())
    cur.end = True

def search(prefix):
    cur = root
    for c in prefix:
        if c not in cur.child:
            return []
        cur = cur.child[c]

    res = []
    def dfs(node, path):
        if node.end:
            res.append(path)
        for c in node.child:
            dfs(node.child[c], path + c)

    dfs(cur, prefix)
    return res


words = input().split()
for w in words:
    insert(w)

print(search(input()))
