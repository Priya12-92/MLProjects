from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT= '-e.'
def get_requirement(file_name:str)->List[str]:
    '''
    this function returm requirements
    '''

    requirements =[]
    with open(file_name) as fp:
        requirements = fp.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(
    name= 'mlproject',
    version='0.0.1',
    author='Priya Ramkumar',
    author_email='priyadhiman121992@gmail.com',
    packages =find_packages,
    install_requires = get_requirement('requirements.txt')


)