from setuptools import find_packages,setup
from typing import List


def get_requirments()->List[str]:
    """
    This function will return list of requirments
    
    """
    requirment_list: List[str]=[]

    """

    write a code to read requirments.txt file and append each requirments in requirment_list variable.
    """
    return requirment_list


setup(
name='sensor',
version="0.0.1",
author="143biswajit",
authour_email="gochhayatbiswajit253@gmail.com",
packages=find_packages(),
install_requires=get_requirments()



) 