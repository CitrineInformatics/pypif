from setuptools import setup, find_packages

setup(name='pypif',
      version='2.1.2',
      url='http://github.com/CitrineInformatics/pypif',
      description='Python tools for working with the Physical Information File (PIF)',
      author='Citrine Informatics',
      packages=find_packages(),
      install_requires=[
            'six>=1.10.0,<2',
            'numpy'
      ])
