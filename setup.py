from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    """
    This function returns the list of requirements

    Params:
    file_path: sebuah path ke requirement.txt
    """
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements

setup(
    name='Diamond Price Prediction',
    version='0.1.0',
    author="Yoki Wahyudi",
    author_email="yoki.wahyu@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)