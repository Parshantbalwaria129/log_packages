from setuptools import setup, find_packages

setup(
    name='PySmartLog',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Add any dependencies your package may have
    ],
    entry_points={
        'console_scripts': [
            # Add any console scripts if needed
        ],
    },
    author='Parshant Bawlaria',
    author_email='parshantbalwaria@gmail.com',
    description='A Smart Python logging package',
    long_description='''\
        Your detailed description of the package.
    ''',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
