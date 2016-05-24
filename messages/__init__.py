def __import_handle(name):
    return __import__(name, globals(), locals(), [], -1)

MESSAGES = [__import_handle('allchannel_pb2'),
            __import_handle('bartercast4_pb2'),
            __import_handle('channel_pb2'),
            __import_handle('demers_pb2'),
            __import_handle('multichain_pb2'),
            __import_handle('search_pb2'),
            __import_handle('template_pb2'),
            __import_handle('tunnel_pb2')]
