class Tree:

  def __init__(self, val=None):
    self.val = val
    self.left = None
    self.right = None

  def insert_left(self, val):
    if self.left is None:
      self.left = Tree(val)
    else:
      self.left.val = val

  def insert_right(self, val):
    if self.right is None:
      self.right = Tree(val)
    else:
      self.right.val = val



class BinarySearchTree(Tree):
  def insert(self, val):
    if self.val is None:
      self.val = val
      return

    if val < self.val:
      if self.left:
        self.left.insert(val)
      else:
        self.left = BinarySearchTree(val)
    else:
      if self.right:
        self.right.insert(val)
      else:
        self.right = BinarySearchTree(val)


