import sys
import zmq
import json
port = "5556"
context = zmq.Context()
socket = context.socket(zmq.SUB)

socket.connect ("tcp://localhost:%s" % port)

socket = context.socket(zmq.SUB)
total_value = 0

while True:
    string = socket.recv_json()
    print(string)