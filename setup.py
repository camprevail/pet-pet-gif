import os
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='pet-pet-gif',
    version='1.0.2',
    packages=['petpetgif'],
    keywords=['petpet', 'petthe', 'gif'],
    url='https://github.com/camprevail/pet-pet-gif',
    license='MIT',
    author='camprevail',
    author_email='cam.anderson573@gmail.com',
    description='Generate a petting gif from a static image (known as "petpet", "Pet the X", or "PETTHE").',
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["pillow"],
    package_data={"petpetgif": ["img/*"]}
)
