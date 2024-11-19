#setup.py
from setuptools import setup, find_packages
setup(
    name="mi_paquete",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'mi_paquete=mi_paquete.main:main',
        ],
    },
)
