from setuptools import setup, find_packages

setup(
    name='bylance',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'matplotlib',
        # Fügen Sie hier weitere Abhängigkeiten hinzu
    ],
    entry_points={
        'console_scripts': [
            'bylance=bylance.app:main',
        ],
    },
)