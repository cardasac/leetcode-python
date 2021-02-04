from setuptools import setup, find_packages

setup(name="solutions",
      version="1.0",
      licence="MIT",
      author="Alexandru Cardas",
      description='A useful module',
      author_email='calexc95@gmail.com',
      packages=find_packages(exclude=["tests", "envs"]))
