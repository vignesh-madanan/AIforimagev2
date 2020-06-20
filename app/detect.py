from imageai.Detection import ObjectDetection
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

MODEL_NAME = ''
MODEL_FOLDER = ''
MODEL_LOCATION = os.path.join(MODEL_NAME, MODEL_FOLDER)

class DetectionManager:
    def __init__(self):
        self.TEMP_FOLDER = os.path.join(os.getcwd(),'temp')
        self.MODEL_LOCATION = MODEL_LOCATION

        self.__check_model__()
        
        self.detector = ObjectDetection()
        self.detector.setModelTypeAsRetinaNet()
        self.detector.setModelPath(self.MODEL_LOCATION)
        logger.info(f'Loaded model from path: {self.MODEL_LOCATION}')
        self.detector.loadModel()
        
    def __check_model__(self):

        if not os.path.exists(self.TEMP_FOLDER):
            logger.info('No Temp Folder, Creating one...')
            os.mkdir(self.TEMP_FOLDER)
            
            self.input_temp_folder = os.path.join(self.TEMP_FOLDER, 'input')
            self.output_temp_folder  = os.path.join(self.TEMP_FOLDER, 'output')
            
            os.mkdir(self.input_temp_folder)
            os.mkdir(self.output_temp_folder)

        if not os.path.exists(self.MODEL_LOCATION):
            logger.info(f'Downloading Model to location {self.MODEL_LOCATION}')

        return True

    def detect_model(input_image_name, input_image_dir = self.input_temp_folder, output_image_dir = self.output_temp_folder, minimum_percentage_probability=50):
        image_name = os.path.join(input_image_dir, input_image_name)
        objectsdetected = detector.detectObjectsFromImage(input_image=, output_image_path=, minimum_percentage_probability=minimum_percentage_probability)
        return objectsdetected
   