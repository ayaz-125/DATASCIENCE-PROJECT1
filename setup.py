from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements.
    '''
    requirements = []

    with open(file_path) as file_obj:
        # Read all lines from the file into a list
        requirements = file_obj.readlines()
        # Remove newline characters from each requirement
        requirements = [req.replace('\n', '') for req in requirements]

    return requirements

setup(
    name='ml_project',
    version='0.0.1',
    author='ayaz',
    author_email='ayazr@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
