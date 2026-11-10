from Tree import Tree

def is_mirror(left_node, right_node):
    if left_node is None and right_node is None:
        return True
    if left_node is None or right_node is None:
        return False
    
    return (left_node.val == right_node.val) and is_mirror(left_node.left, right_node.right) and is_mirror(left_node.right, right_node.left)

def is_palindrome_tree(root):
    if root is None:
        return True
    return is_mirror(root.left, root.right)





root = Tree("A")

root.insert_left("B")
root.left.insert_left("C")
root.left.insert_right("D")

root.left.left.insert_left("E")
root.left.left.left.insert_left("G")
root.left.left.left.insert_right("H")

root.left.right.insert_left("F")
root.left.right.left.insert_left("I")


root.insert_right("B")
root.right.insert_left("D")
root.right.insert_right("C")

root.right.left.insert_right("F")
root.right.left.right.insert_right("I")

root.right.right.insert_right("E")
root.right.right.right.insert_left("H")
root.right.right.right.insert_right("G")