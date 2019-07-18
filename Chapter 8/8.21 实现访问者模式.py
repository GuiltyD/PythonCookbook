class Node:
	pass

class BinaryOperator(Node):
	def __init__(self,left,right):
		self.left = left
		self.right = right

class ADD(BinaryOperator):
	pass

class SUB(BinaryOperator):
	pass

class MUL(BinaryOperator):
	pass

class DIV(BinaryOperator):
	pass

class Number(Node):
	def __init__(self,value):
		self.value = value

class NodeVisitor:
	def visit(self,node):
		methname = 'visit_' + type(node).__name__
		meth = getattr(self,methname,Node)
		if meth is Node:
			raise RuntimeError('No {} Method'.format('visit_'+type(node).__name__))
		return meth(node)


class Evaluator(NodeVisitor):
	def visit_Number(self,node):
		return node.value
	def visit_ADD(self,node):
		return self.visit(node.left)+self.visit(node.right)
	def visit_SUB(self,node):
		return self.visit(node.left)-self.visit(node.right)
	def visit_MUL(self,node):
		return self.visit(node.left)*self.visit(node.right)
	def visit_DIV(self,node):
		return self.visit(node.left)/self.visit(node.right)

t1 = SUB(Number(3),Number(4))
t2 = MUL(Number(2),t1)
t3 = DIV(t2,Number(5))
t4 = ADD(Number(1),t3)
e = Evaluator()
print(e.visit(t4))