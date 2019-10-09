from setuptools import setup

with open('README.rst', 'r') as readme_fd:
    long_description = readme_fd.read()

try:
    from gwio.devtools.utils import make_calver

    __VERSION__ = make_calver()
except ImportError:
    __VERSION__ = '0.0.0a0'

setup(
    name='gwio-dynamorm',
    version=__VERSION__,
    description='DynamORM is a Python object & relation mapping library for Amazon\'s DynamoDB service.',
    long_description=long_description,
    author='Evan Borgstrom',
    author_email='evan@borgstrom.ca',
    url='https://github.com/NerdWalletOSS/DynamORM',
    license='Apache License Version 2.0',

    install_requires=[
        'marshmallow==3.0.0rc6',
        'blinker>=1.4,<2.0',
        'boto3>=1.3,<2.0',
        'six',
    ],
    packages=['dynamorm', 'dynamorm.types'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Topic :: Database',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries'
    ]
)
