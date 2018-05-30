class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root, str1 = ""):
    if not root:
        str1 += "# "
        return str1
    return str1 + root.val +" " + serialize(root.left) + serialize(root.right)

def deserialize(str1):
    
    def decode(vals):
        val = next(vals)
        if val == '#':
            return None
        node = Node(val)
        node.left = decode(vals)
        node.right = decode(vals)
        return node

    vals = iter(str1.split())
    return decode(vals)

node = Node('root', Node('left', Node('left.left')), Node('right'))
print(serialize(node))
assert deserialize(serialize(node)).left.left.val == 'left.left'
print(serialize(deserialize(serialize(node))))