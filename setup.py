from setuptools import find_packages, setup
from typing import list

HYPHEN_E_DOTS = '-e .'
def get_requirements(file_path : str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("/n"," ")  for req in requirements]

        if HYPHEN_E_DOTS in requirements:
            requirements.remove(HYPHEN_E_DOTS)

    return requirements




setup(
    name = 'NEW_ML_PROJECTS',
    version= '0.0.1',
    author = 'Aditya',
    author_email= 'adityapanchbhai4@gmail.com',
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')

)