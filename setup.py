from setuptools import setup, find_packages

setup(
    name='forex-python',
    version='0.1.0',
    author='Carrington Muleya',
    author_email='mcm96m@gmail.com',
    description='Python Currency Converter and Forex Engine',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/carrington-dev/forex-python',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        # List your package dependencies here, e.g.,
        'requests',
    ],
)
