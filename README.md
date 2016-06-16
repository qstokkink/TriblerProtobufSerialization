# TriblerProtobufSerialization
Standalone prototype for serialization of messages for [Tribler](https://github.com/Tribler/tribler) using [Protocol Buffers](https://github.com/google/protobuf).

## Creating a message
This section will explain how to get your first message compiled.

### Create your Protocol Buffers definition
This is mostly the same as [creating a normal Protocol Buffers definition](https://developers.google.com/protocol-buffers/docs/proto).
There are two things you must do however:

1. Put your `.proto` definition in the `src/` folder.
2. Add an import of `defaults.proto` to your file.

For example `src/my_community.proto`:

```
import "defaults.proto";

message Votecast {
  required string cid = 1 [(length) = 8]; // 8 bytes
  required int32 vote = 2 [(length) = 2]; // 2 bytes
  required int64 timestamp = 3;
}
```

Note that there is a `length` option specified.
This is a custom option to specify the maximum number of bytes a field can _maximally_ occupy.
Because values are packed, this will - in almost all cases - never be the actual amount of bytes the field will use _on-wire_.

### Compile using the compiler
To compile your fresh `.proto` just call the `compiler.py` script in the `src/` folder (make sure to install the protoc compiler first: `sudo apt-get install libprotobuf-dev protobuf-compiler`).
This will create a file called `<your_proto_file_name>_pb2.py`.
In our previous example:

```sh
python compiler.py my_community.proto
```

### Move your compiled file
Now move/copy your compiled package (`<your_proto_file_name>_pb2.py`) into the `messages/` folder.
As a final touch edit the `__init__.py` file in the `messages/` folder.
You will need to change the definition of `MESSAGES` to include the `__import_handle()` of your module.
In our example:

```python
MESSAGES = [__import_handle('my_community_pb2')]
```

## Using the Serializer
Here we assume you have added at least one message to the file tree as described in the previous section. You will also need to have Protocol Buffers installed (`sudo apt-get install python-protobuf`).
To use the Serializer you need to create a `Serializer` instance (you can have multiple instances if you want):
```python
from serializer import Serializer

s = Serializer()
```

### Serialization
To serialize a message you need to call the `serialize()` function.
In our running example one would for example to the following:

```python
# By Votecast definition order:
s.serialize("Votecast", "mycid", 15, 12300014)
# By Votecast field names:
s.serialize("Votecast", cid = "mycid", vote = 15, timestamp = 12300014)
```

### Unserializing
To get messages from raw data, you need two things:

1. A handler class (`add_package_handler()`) or function per message(`add_handler()`).
2. To call `unserialize()` on your data.

Several advanced features of `unserialize()` include the ability to skip unusable bytes and to buffer data for the next call.
In our example:

```python
class TestHandler:
    def on_votecast(obj):
        print obj.cid + ", " + str(obj.vote) + ", " + str(obj.timestamp)

def test_handler(obj):
    print obj.cid + ", " + str(obj.vote) + ", " + str(obj.timestamp)
    
s.add_package_handler("my_community", TestHandler())
s.add_handler("Votecast", test_handler)
```

## Complete example
This is a reference for all source files required for a minimal working example.
You will still need to compile `src/my_community.proto` as described above.

`src/my_community.proto`:

```
import "defaults.proto";

message Votecast {
  required string cid = 1 [(length) = 8]; // 8 bytes
  required int32 vote = 2 [(length) = 2]; // 2 bytes
  required int64 timestamp = 3;
}
```

`messages/__init__.py`:

```python
def __import_handle(name):
    return __import__(name, globals(), locals(), [], -1)

MESSAGES = [__import_handle('my_community_pb2')]
```

`test.py`:

```python
from serializer import Serializer

class TestHandler:
    def on_votecast(obj):
        print "TestHandler received: " + obj.cid + ", " + str(obj.vote) + ", " + str(obj.timestamp)

def test_handler(obj):
    print "test_handler received: " + obj.cid + ", " + str(obj.vote) + ", " + str(obj.timestamp)
    
s = Serializer()
s.add_package_handler("my_community", TestHandler())
s.add_handler("Votecast", test_handler)

# Encode
enc = s.serialize("Votecast", "mycid", 15, 12300014)

# Handle decode
s.unserialize(enc)
```
