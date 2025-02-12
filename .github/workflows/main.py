from project_types import Feedback
from model import SubtractASquareModel
from view import SubtractASquareView
from controller import SubtractASquareController

def main():
    model: SubtractASquareModel = SubtractASquareModel(1000, 4)
    view: SubtractASquareView = SubtractASquareView()
    controller: SubtractASquareController = SubtractASquareController()
        
    controller.start(model, view)
    
if __name__ == "__main__":
    main()