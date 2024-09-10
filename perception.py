class Perception:
    def __init__(self):
        self.perceived_objects = []

    def perceive(self, objects):
        self.perceived_objects = objects

    def get_perceived_objects(self):
        return self.perceived_objects
    

class ImagePerception(Perception):
    def __init__(self):
        super().__init__()

    def perceive_image(self, image):
        # Perform image processing and object detection
        # to generate perceived objects
        objects = self.detect_objects(image)
        self.perceive(objects)

    def detect_objects(self, image):
        # Implement object detection algorithm here
        # and return the detected objects
        pass


class DetectorFactory:
    def create_detector(self, detector_type):
        if detector_type == "cell":
            return CellDetector()
        elif detector_type == "subcellular":
            return SubcellularDetector()
        else:
            raise ValueError("Invalid detector type")


class CellDetector:
    def detect(self, image):
        # Implement object detection algorithm for cells
        # and return a list of detected objects
        objects = []
        # Perform object detection
        # Append detected objects to the objects list
        return objects

class SubcellularDetector:
    def detect(self, image):
        # Implement object detection algorithm for subcellular structures
        # and return a list of detected objects
        objects = []
        # Perform object detection
        # Append detected objects to the objects list
        return objects