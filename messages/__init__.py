def __import_handle(name):
    return __import__(name, globals(), locals(), [], -1)

MESSAGES = []
