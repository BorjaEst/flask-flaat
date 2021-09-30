from setuptools import setup

about = {}
with open('flask_flaat/__about__.py') as f:
    exec(f.read(), about)


with open("README.md", "rt") as f:
    readme_text = f.read()

setup(name=about['__title__'],
      version=about['__version__'],
      url=about['__url__'],
      license=about['__license__'],
      author=about['__author__'],
      author_email=about['__author_email__'],
      description=about['__description__'],
      long_description=readme_text,
      long_description_content_type='text/markdown',
      packages=['flask_flaat'],
      zip_safe=False,
      platforms='any',
      install_requires=['Flask', 'Flaat', 'Flask-login'],
      classifiers=[
    # 'Development Status :: x - xxxx',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
])
