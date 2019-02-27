import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Progetto_One_Pin_Keypad",
    version="0.0.2",
    author="Progetto Company",
    author_email="progettocompany@gmail.com",
    license='MIT'
    description="Raspberry Pi compatible Python Package with examples for the One Pin Keypad.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ProgettoCompany/Progetto_One_Pin_Keypad_Python_Package",
    packages=setuptools.find_packages(),
    dependency_links  = ['https://github.com/adafruit/Adafruit_CircuitPython_ADS1x15/archive/1.0.2.tar.gz'],
    install_requires  = ['adafruit-circuitpython-ads1x15>=1.0.2'],
    classifiers=[
        'Operating System :: POSIX :: Linux',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development',
        'Topic :: System :: Hardware',
    ],
)
