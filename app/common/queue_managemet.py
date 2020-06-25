import sys
import zmq
import json
import os
import logging
import traceback
from multiprocessing import Process
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ProxyManager:
    def __init__(self):
        self.SENDER_PORT = 3344
        self.RECEIVER_PORT = 3345
        self.SENDER_PROXY = f"tcp://*:{self.SENDER_PORT}"
        self.RECEIVER_PROXY = f"tcp://*:{self.RECEIVER_PORT}"
        self.__number_of_processes__ = 1

    def main(self):
        try:
            context = zmq.Context(1)
            
            # Socket facing clients
            sender = context.socket(zmq.XREP)
            sender.bind(self.SENDER_PROXY)
            # Socket facing services

            receiver = context.socket(zmq.XREQ)
            receiver.bind(self.RECEIVER_PROXY)
            print(f'Starting Proxy | Sender:{self.SENDER_PROXY} | Receiver{self.SENDER_PROXY}')
            zmq.device(zmq.QUEUE, sender, receiver)

        except Exception as e:
            print(e)
            print("bringing down zmq device")
            traceback.print_exc()
        finally:
            sender.close()
            receiver.close()
            context.term()

    def start_proxy_server(self):
        self.main()
        #p = Process(target=self.main)
        #p.start()
        #p.join()
               
class Sender(ProxyManager):
    def __init__(self):
        self.client_id = 1
        self.context = zmq.Context() 

        super().__init__()
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect("tcp://localhost:%s" % self.SENDER_PORT)

    def send_message(self, message):
        if isinstance(message, dict):
            mm  = {f'self.client_id':message}
            self.socket.send_json(mm)
            message = self.socket.recv()
            return True
        raise TypeError('Message should be of type Dict')


class Receiver(ProxyManager):
    
    def __init__(self):       
        self.server_id = 2
        super().__init__()
        self.context = zmq.Context() 
        self.socket = self.context.socket(zmq.REP)
        self.socket.connect("tcp://localhost:%s" % self.SENDER_PORT)

    def receive_message(self):
        message = self.socket.recv()
        message = json.dumps(message)
        print("Received Message", message)
        self.socket.send({self.server_id:True})
        return message

if __name__ == "__main__":
    if sys.argv[1] == 'proxy':
        ProxyManager().start_proxy_server()
    if sys.argv[1] == 'sender':
        sender = Sender()

        sender.send_message({'test':'TEST'})
    
    if sys.argv[1] == 'receiver':
        receiver = Receiver()
        receiver.receive_message()