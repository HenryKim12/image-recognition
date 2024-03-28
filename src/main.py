from controller.DatasetControllert import DatasetController
import os
from pathlib import Path

def main():
    data_controller = DatasetController()
    # root = Path(os.path.dirname(__file__)).parent.absolute()
    # data_path = os.path.join(root, "data")
    # if os.listdir(data_path) == []:
    #     data_controller.get_data()
    
    data_controller.playground()

if __name__ == "__main__":
    main()