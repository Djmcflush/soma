from setuptools import setup, find_packages

setup(
    name='soma',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        # Add any dependencies here
    ],
    entry_points={
        'console_scripts': [
            'soma=soma.main:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A tool to stream data from one place to another',
    url='https://github.com/yourusername/soma',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
