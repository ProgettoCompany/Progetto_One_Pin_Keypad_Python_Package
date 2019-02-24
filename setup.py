import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Progetto_One_Pin_Keypad",
    version="0.0.1",
    author="Progetto Company",
    author_email="progettocompany@gmail.com",
    description="Raspberry Pi compatible Python Package with examples for the One Pin Keypad.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ProgettoCompany/Progetto_One_Pin_Keypad_Python_Package",
    packages=setuptools.find_packages(),
    classifiers=[
        'Operating System :: POSIX :: Linux',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development',
        'Topic :: System :: Hardware',
    ],
)