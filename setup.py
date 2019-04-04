from setuptools import setup

setup(
    name='tenma',
    version='0.1.0',
    description='Python package to control Tenma devices.',
    url='https://github.com/milescaples/PyTenma',
    author='Miles Caples',
    author_email='miles.caples@relectrify.com',
    license='MIT',
    packages=['tenma'],
    install_requires=[
        'pyserial'
    ]
)
