class ErrorLogger:
	from os.path import split
	from  traceback import format_exception

	def __init__(self, exception):
		self.__etype = type(exception)
		self.__tb = exception.__traceback__
		self.__fullpath = self.__tb.tb_frame.f_code.co_filename
		self.__fname = ErrorLogger.split(self.__fullpath)[1]
		self.__lineno = self.__tb.tb_lineno
		self.__description = str(exception)
		self.__tb_str = ''.join(ErrorLogger.format_exception(self.__etype, exception, self.__tb))

	def personal_log(self):
		"""
		Returns error with very little information considering user privacy
		"""
		return {"filename": self.__fname, 
				"etype": self.__etype, 
				"des": self.__description,
				"lineno": self.__lineno
			}

	def full_log(self):
		"""
		Returns the entire traceback with as much as information poassible omiting user privacy
		"""
		return {"filename": self.__fname,
				"fullpath": self.__fullpath,
				"etype": self.__etype,
				"des": self.__description,
				"lineno": self.__lineno,
				"traceback": self.__tb_str
		}