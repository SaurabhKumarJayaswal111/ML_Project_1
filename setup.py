from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # Use strip() instead of replace("\n", "")
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name="ML_Project_1",
    version="0.0.1",
    author="Mr. Saurabh",
    author_email="saurabhkumarjayaswal@gmail.com",  # Fix: `author_email` instead of `author_mail`
    packages=find_packages(),  # Ensure it finds packages in the project
    install_requires=get_requirements('requirements.txt'),
)
