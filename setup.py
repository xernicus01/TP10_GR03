from setuptools import find_packages,setup
from typing import List
hypen = '-e.'
def get_requirements(path:str)->List[str]:
    requirements = []
    with open(path) as file:
        requirements = file.readlines()
        requirements = [req.replace('.\n','') for req in requirements]

        if hypen in requirements:
            requirements.remove(hypen)
    return requirements

setup(
    author='Ance',
    author_email='charlidelta840@gmail.com',
    name='boston_house_model',
    version='1.0.0',
    packages=find_packages(),
    install_requires = get_requirements('requirement.txt')
)