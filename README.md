# AirBnb - An exercise in full-stack development at Holberton School.

This REST API project is written in Python. We will be using Flask, React, Peewee, NodeJS, and MySQL. This is currently a work in progress. As we progress through development we will update code and this README.

## Functional Requirements

1. Create persistent storage for service data using MySQL
1. Have three working environments (development, production & test)
1. Isolate each environment, each with it's own variables
1. Create link between Python application and database
1. Create all tables from script `migrate.py`
1. Create Flask application making it global to Python app using `__init__.py`
1. Serialize all models
1. Verify all POST/PUT data parameters
1. Using TDD write tests and validate code with `unittest`
1. Prevent REST API consumption from another site using Flask-CORS.


## Features (Soon to come)

1. `User` may include a message with the rental request
1. `User` may include the date they want to rent a home
1. `User` may search home based upon dates available
1. `User` may search homes by location (Hint: use
   [graticule](https://github.com/collectiveidea/graticule))

## Learning Goals

1. Creating secure user registration and login
1. Build a full-stack web application
1. Collaborating with and contributing to open source developers

## Getting Started
1. Fork and clone this repo
1. cd into it
1. Run `$ python api/app.py`
