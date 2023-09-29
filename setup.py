from setuptools import setup, find_packages
from typing import List


PROJECT_NAME="sensor-data-pipeline"
VERSION= "0.0.1"
AUTHOR = "Kiran Bagade"
DESCRIPTION="This is a data pipeline which will produce data from sensors and publish it to Kafka topics and consumers will consume data from respective Kafka topics and storing it to the Mongo DB database"
REQUIREMENT_FILE_NAME="requirements.txt"
HYPHEN_E_DOT= "-e ."

def get_requirements_list() ->List[str]:
    """
    Description : This function is going to return a list of name of libraries 
    mention in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as file:
        requirement_list= file.readlines()
        requirement_list=[name.replace("\n","") for name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list




setup(
    name = PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages= find_packages(),
    install_requires = get_requirements_list()
)