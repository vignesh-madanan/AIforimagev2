from subprocess import Popen
from detect import DetectionManager
from .common.logger_manager import Logger
from .common.queue_managemet import ProxyManager, Sender, Receiver


class ServiceMain:
    def __init__(self):
        self.detection_instance = DetectionManager()

    def run_detection(image):
        return self.detection_instance.format_output(self.detection_instance.detect_model(image))

    def start_queue():
        raise NotImplementedError
        ProxyManager.start_proxy_server
