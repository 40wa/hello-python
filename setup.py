from setuptools import setup, find_packages


setup(
    name="hello-python",
    version="0.1",
    packages=find_packages(),
    install_requires=[ 'termcolor' ],
    entry_points={
        'console_scripts': [
            'hello=hello.__main__:main',
        ],
    },
)
