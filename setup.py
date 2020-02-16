from setuptools import setup, find_packages 
# make sure to run this pip install -e .

NAME = "toy-robot-on-table" 

VERSION = "0.1" 

REQUIRES = [ "click",
] 

 

setup( 
    name=NAME, 
    version=VERSION, 
    install_requires=REQUIRES, 
    packages=find_packages(), 
    python_requires=">=3.5.3", 
    include_package_data=True, 
    entry_points={"console_scripts": ["start = start:main"]}, 

) 