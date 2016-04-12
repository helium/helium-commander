import re
import ast
from setuptools import setup


setup(
    name='helium-commander',
    version='0.3.0-dev',
    url='http://github.com/helium/helium-commander/',
    license='BSD',
    author='Marc Nijdam',
    author_email='marc@helium.com',
    description='A CLI and service wrapper for the Helium API',
    long_description=__doc__,
    packages=['helium', 'helium.commands'],
    include_package_data=True,
    platforms='all',
    install_requires=[
        'requests>=2.9',
        'dpath>=1.4',
        'futures>=3.0',
        'tablib>=0.11',
        'click>=6.6',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        "Topic :: Utilities",
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    entry_points='''
        [console_scripts]
        helium=helium.cli:main
    '''
)