from Tree import BinarySearchTree




def _count(tree, target):
    if tree.val is None:
        return 0

    count = 0
    if target == tree.val:
        count += 1

    if target <= tree.val and tree.left:
        count += _count(tree.left, target)
    if target >= tree.val and tree.right:
        count += _count(tree.right, target)

    return count

def search(tree, val):
    if tree.val is None:
        return False
    if val == tree.val:
        return True
    elif val < tree.val and tree.left:
        return search(tree.left, val)
    elif val > tree.val and tree.right:
        return  search(tree.right, val)
    return False

def contains_all_characters(tree, s):
    s = str(s)

    for char in s:
        found = search(tree, char)
        if not found:
            try:
                found = search(tree, int(char))
            except ValueError:
                pass

        if not found:
            return False

    return True


bst = BinarySearchTree("e")
bst.insert("b")
bst.insert("m")
bst.insert("a")
bst.insert("c")


print(_count(bst, 'b'))
print(contains_all_characters(bst, "ace"))
print(contains_all_characters(bst, "bat"))