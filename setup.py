from setuptools import setup, find_packages

setup(
    name='SICSS_Pkg',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    author='Timothy Loftus',
    author_email='tiloftus.4@gmail.com',
    description='A minimal example package for SICSS',
    url='https://github.com/tiloftus/SICSS_Pkg',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
