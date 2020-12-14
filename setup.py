from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='pygazebo_ros',
    description='Control Gazebo using ROS topics and services',
    author='Quentin GALLOUÉDEC',
    author_email='gallouedec.quentin@gmail.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/qgallouedec/pygazebo_ros',
    packages=find_packages(),
    version='0.0.0'
)
