import numpy as np
import pandas as pd
import os
import requests 
from imageai.Detection import ObjectDetection

def detect_model(image_path):
    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath("resnet50_coco_best_v2.0.1.h5")
    detector.loadModel()
    objectsdetected = detector.detectObjectsFromImage(input_image=image_path, output_image_path="./detected/imagenew.jpg", minimum_percentage_probability=20)
            
    return objectsdetected
   