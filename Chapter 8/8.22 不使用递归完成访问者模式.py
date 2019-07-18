
import types
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
		stack = [node]
		last_result = None
		while stack:
			print(stack)
			try:
				last = stack[-1]
				if isinstance(last,types.GeneratorType):
					stack.append(last.send(last_result))
					last_result = None
				elif isinstance(last,Node):
					stack.append(self._visit(stack.pop()))
				else:
					last_result = stack.pop()
			except StopIteration:
				print('end')
				stack.pop()
		return last_result

	def _visit(self,node):
		methname = 'visit_' + type(node).__name__
		meth = getattr(self,methname,None)
		if meth is Node:
			raise RuntimeError('No {} Method'.format('visit_'+type(node).__name__))
		return meth(node)


class Evaluator(NodeVisitor):
	def visit_Number(self,node):
		return node.value
	def visit_ADD(self,node):
		print('start add')
		lf = yield node.left
		print('lfadd = ', lf)
		rt = yield node.right
		print('rtadd = ', rt)
		yield lf + rt
	def visit_SUB(self,node):
		print('start sub')
		lf = yield node.left
		print('lfsub = ',lf)
		rt = yield node.right
		print('rtsub = ', rt)
		yield lf - rt
	def visit_MUL(self,node):
		print('start mul')
		lf = yield node.left
		print('lfmul = ', lf)
		rt = yield node.right
		print('rtmul = ', rt)
		yield lf * rt
	def visit_DIV(self,node):
		print('start div')
		lf = yield node.left
		print('lfdiv = ', lf)
		rt = yield node.right
		print('rtdiv = ', rt)
		yield lf / rt

t1 = SUB(Number(3),Number(4))

e = Evaluator()
print(e.visit(t1))