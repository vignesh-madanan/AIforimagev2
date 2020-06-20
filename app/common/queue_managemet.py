import sys
import zmq
import json
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ZMQManager:
    def __init__(self):
        self.context = zmq.Context()
        self.BIND_IP = 'localhost'
        self.port = 5556

class Publisher(ZMQManager):
    def __init__(self):
        
        super().__init__()        
        self.socket = context.socket(zmq.PUB)
        self.socket.bind(f"tcp://{self.BIND_IP}:{self.port}")

    def send_message(self, message):
        if isinstance(message, dict):
            message = json.dumps(message)
            logger.info('Message Sent', message)
            socket.send("%d %d" % (topic, messagedata))
            return True
        raise TypeError('Message should be of type Dict')

if __name__ == "__main__":
    import zmq
    import random
    import sys
    import time

    port = "5556"
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:%s" % port)

    while True:
        topic = random.randrange(9999,10005)
        messagedata = random.randrange(1,215) - 80
        print("%d %d" % (topic, messagedata))
        socket.send_json({topic:messagedata})
        time.sleep(1)

