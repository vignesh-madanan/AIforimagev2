import logging
import logging.config

class Logger:
    def __init__(name):
        assert isinstance(name,str)
        logging.config.fileConfig(os.path.join(os.getcwd().'common/config/logging.ini')), disable_existing_loggers=True)
        self.logger = logging.getLogger(name)