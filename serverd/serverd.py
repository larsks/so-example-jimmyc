import os
import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.PUSH)
address = os.environ.get('SERVER_LISTEN_URI')
socket.bind(address)
print("Sending to {}...".format(address))
while True:
    message = socket.send_string("Got it!")
    print("Sent message")
    time.sleep(1)
