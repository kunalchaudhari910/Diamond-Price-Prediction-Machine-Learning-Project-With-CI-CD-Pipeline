from setuptools import find_packages , setup
from typing import List

HYPHON_E_DOT = "-e ."

def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readline()
        requirements = [req.replace("\n","") for req in requirements]
        
        if HYPHON_E_DOT in requirements:
            requirements.remove(HYPHON_E_DOT)






setup(name='Diamond_Price_Prediction_Machine_Learning_Project_With_CI_CD_Pipeline',
      version='0.0.1',
      author='Dhananjay Rokade',
      author_email='dhananjayrokade9665@gmail.com',
      url='https://github.com/Rokade-DP/Diamond-Price-Prediction-Machine-Learning-Project-With-CI-CD-Pipeine',
      packages=find_packages('requirements.txt')
     )