from setuptools import setup, find_packages

setup(
    name='jdol_celery_utils',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'celery',
        'pandas'
    ],
)