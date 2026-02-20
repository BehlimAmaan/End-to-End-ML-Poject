from setuptools import find_packages, setup
from typing import List

Hyphen_dot = "-e ."
def get_requirements(file_path:str)->List[str]: 
    '''
    this function will return list of requirements
    '''
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readline()
        requirements = [req.replace("\n","")for req in requirements]
    if Hyphen_dot in requirements:
        requirements.remove(Hyphen_dot)

setup(
    name='Ml Project',
    author="Amaan Behlim",
    version='0.0.1',
    install_requires=get_requirements("requirements.txt"),
    author_email="itzamaanbehlim45@gmail.com",
    packages=find_packages()
)