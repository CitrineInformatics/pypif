from setuptools import setup, find_packages

setup(name='pypif',
      version='1.0.19',
      url='http://github.com/CitrineInformatics/pypif',
      description='Python tools for working with the Physical Information File (PIF)',
      author='Kyle Michel',
      author_email='kyle@citrine.io',
      packages=find_packages(),
      install_requires=[
            'six==1.10.0'
      ])
