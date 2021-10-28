<!-- <p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://" alt="Project logo"></a>
</p> -->

<h1 align="center">Flask flaat</h1>

<div align="center">

  ![Status](https://img.shields.io/badge/status-active-success.svg)
  ![GitHub commit activity](https://img.shields.io/github/commit-activity/y/BorjaEst/flask-flaat)
  ![GitHub issues](https://img.shields.io/github/issues/BorjaEst/flask-flaat)
  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---


# Table of Contents
- [About](#about)
- [Getting Started](#getting_started)
- [Testing](#tests)
- [Usage](#usage)
- [Built Using](#built_using)
- [Authors](#authors)

# About <a name = "about"></a>
Flask plug in which tries to solve the issue of sessions and authentication via tokens passed by `Authorization: Bearer`.

# Getting Started <a name = "getting_started"></a>
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

## Prerequisites
For production you need the basic requirements collected at `requirements.txt`. To install them you can use:

```
pip install -r requirements.txt
```

## Installing
Installation is done using 
[Setuptools](https://setuptools.readthedocs.io/en/latest/setuptools.html#)
package:

- For installation from sources: `setup.py install`  
- For simple installation: `pip install {name}`  

# Testing <a name = "tests"></a>
Explain how to run the automated tests for this system.

Tests run using 
[tox](https://tox.readthedocs.io/en/latest/)
package and 
[pytest](https://docs.pytest.org/en/stable/)

```sh
$ tox
...
py37: commands succeeded
py38: commands succeeded
```

# Usage <a name="usage"></a>
The repository contains a basic tested example of an application. 

# Built Using <a name = "built_using"></a>
- [Flask](https://github.com/pallets/flask) - Server Framework
- [flask-login](https://github.com/maxcountryman/flask-login) - Flask sessions
- [Flaat](https://github.com/indigo-dc/flaat) - Token Authentication

# Authors <a name = "authors"></a>
- [@marcvs](https://github.com/marcvs) - Flaat developer
- [@borjaEst](https://github.com/BorjaEst) - Adaptation to flask & sessions

See also the list of [contributors](https://github.com/BorjaEst/flask-flaat/contributors) who participated in this project.

