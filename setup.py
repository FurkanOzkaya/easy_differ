from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'easy_differ',
  packages = ['easy_differ'],
  version = '0.1',
  license='MIT',
  description = "Compare Text line by line. When your texts has different place in file you can't use beyond compare totaly so you may need to compare line by line.",   # Give a short description about your library
  author = 'Furkan Ozkaya',
  author_email = 'furkanozkaya45@gmail.com',
  url = 'https://github.com/FurkanOzkaya/easy_differ',
  download_url = 'https://github.com/FurkanOzkaya/easy_differ/archive/0.1.tar.gz',
  keywords = ['DIFFER', 'COMPARE', 'TEXT COMPARE', "ARRAY COMPARE"],
  long_description=long_description,
  long_description_content_type='text/markdown',
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)