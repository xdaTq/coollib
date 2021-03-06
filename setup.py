from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='coollib',
  version='0.0.1',
  description='Nothing & Everything Library',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='aTq_',
  author_email='',
  license='MIT', 
  classifiers=classifiers,
  keywords='cool', 
  packages=find_packages(),
  install_requires=[''] 
)