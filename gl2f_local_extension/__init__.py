class Local_Serve:
	@staticmethod
	def add_to():
		return 'gl2f.local', 'serve'

	@staticmethod
	def add_args(parser):
		parser.set_defaults(handler = lambda _:print(f'local extension installed'))

registrars = [Local_Serve]
