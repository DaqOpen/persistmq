from setuptools import setup, find_packages

setup(
    name="robustmq",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "paho-mqtt",
    ],
    author="Michael Oberhofer",
    author_email="info@pqopen.com",
    description="A on-top library for robust MQTT with file system message caching",
    #long_description=open('README.md').read(),
    #long_description_content_type="text/markdown",
    url="https://github.com/daqopen/robustmq",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Linux/Unix",
    ],
    python_requires='>=3.7',
)