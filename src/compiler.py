import os, sys, subprocess

if len(sys.argv) != 2:
    exit("Call with the file you wish to compile")

filename = os.path.splitext(sys.argv[1])[0]
if (filename == "defaults") or (filename == "miniprotobuf"):
    exit("You are not supposed to compile " + filename)

subprocess.check_call(['protoc', '--python_out=.', sys.argv[1]])
