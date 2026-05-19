[loggers]
keys=root,sampleLogger

[logger_root]
level=DEBUG
handlers=console

[logger_sampleLogger]
level=DEBUG
handlers=console,file
qualname=sampleLogger
propagate=0

[formatters]
keys=sampleFormatter

[formatter_sampleFormatter]
© Dalhousie University, Internetworking Program 12/17
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s

[handlers]
keys=console,file

[handler_console]
class=StreamHandler
level=DEBUG
formatter=sampleFormatter
args=(sys.stdout,)

[handler_file]
class=FileHandler
level=DEBUG
formatter=sampleFormatter
args=('task5C.log',)
