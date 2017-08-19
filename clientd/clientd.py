import os
import zmq

context = zmq.Context()
socket = context.socket(zmq.PULL)
address = os.environ.get('SERVER_CONNECT_URI')
socket.connect(address)
print("Listening to {}...".format(address))
while True:
    message = socket.recv_string()
    print("Client got message! {}".format(message))
