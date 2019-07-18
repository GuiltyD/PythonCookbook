class Connect:
	def __init__(self):
		self.new_state(ClosedConnectionState)

	def new_state(self,state):
		self._state = state

	def read(self):
		return self._state.read(self)

	def open(self):
		return self._state.open(self)

	def write(self,value):
		return self._state.write(self,value)

	def close(self):
		return self._state.close(self)

class ClosedConnectionState:
	@staticmethod
	def read(conn):
		raise RuntimeError('Not Open')
	@staticmethod
	def open(conn):
		conn.new_state(OpenConnectionState)
	@staticmethod
	def write(conn):
		raise RuntimeError('Not Open')
	@staticmethod
	def close(conn):
		raise RuntimeError('Areadly closed')
class OpenConnectionState:
	@staticmethod
	def read(conn):
		print('reading')
	@staticmethod
	def open(conn):
		raise RuntimeError('areadly open')
	@staticmethod
	def write(conn):
		print('writing')
	@staticmethod
	def close(conn):
		conn.new_state(ClosedConnectionState)


c= Connect()
c.open()
c.read()