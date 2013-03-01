import time


class Timer:
	def __init__(self):
		self.start_time = None

	def start(self):
		self.start_time = time.clock()

	def stop(self):
		if self.start_time is None:
			raise RuntimeError('Timer not started.')

		seq = ['Total time: ', str(time.clock() - self.start_time), 's']
		print(''.join(seq))
