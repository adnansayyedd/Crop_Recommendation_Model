from setuptools import setup, find_packages

with open("requirements.txt", "r") as f:
    install_requires = f.read().splitlines()

    setup(
        name='Crop Recommendation Model',
        version="1.0.0",
        description="This is a crop recommendation model Based on weather.",
        author="Adnan Sayyed"
    )

    