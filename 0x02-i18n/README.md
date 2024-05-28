# Flask i18n Project

This project involves internationalization (i18n) in Flask, focusing on displaying different languages, inferring the correct locale, and localizing timestamps. Below is a detailed overview of the project requirements, learning objectives, and resources to help you succeed.

## Resources

### Read or Watch:
- [Flask-Babel](https://pythonhosted.org/Flask-Babel/)
- [Flask i18n Tutorial](https://flask.palletsprojects.com/en/2.0.x/patterns/l10n/)
- [pytz](https://pytz.sourceforge.net/)

## Learning Objectives
1. **Parametrize Flask templates to display different languages:**
   - Learn how to use Flask-Babel to make your application multilingual.
   - Understand how to create translation files and manage multiple languages.

2. **Infer the correct locale based on URL parameters, user settings, or request headers:**
   - Learn methods to determine the user's locale and serve content accordingly.
   - Implement functions to handle locale inference in your Flask application.

3. **Localize timestamps:**
   - Use `pytz` and Flask-Babel to display dates and times in the user's local timezone.
   - Understand how to format timestamps for different locales.

## Requirements

### General
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3 (version 3.7).
- All your files should end with a new line.
- A `README.md` file at the root of the project folder is mandatory.
- Your code should use the `pycodestyle` style (version 2.5).
- The first line of all your files should be exactly `#!/usr/bin/env python3`.
- All your `*.py` files should be executable.

### Documentation
- All your modules should have documentation (checked using `python3 -c 'print(__import__("my_module").__doc__)'`).
- All your classes should have documentation (checked using `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`).
- All your functions and methods should have documentation (checked using `python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`).
- Documentation should be more than a single word; it should be a complete sentence explaining the purpose of the module, class, or method. The length of the documentation will be verified.
- All your functions and coroutines must be type-annotated.

## Example of Documentation

### Module Documentation
```python
"""
This module provides functionality for internationalizing a Flask application.
It includes functions for setting up Flask-Babel, inferring locales, and formatting timestamps.
"""
```

### Class Documentation
```python
class MyClass:
    """
    This class handles user settings related to locale preferences.
    It provides methods to get and set the user's preferred language and timezone.
    """
```

### Function Documentation
```python
def my_function():
    """
    This function determines the user's locale based on request headers and URL parameters.
    It returns the appropriate locale string to be used for translations.
    """
```

## Projects:

0. Basic Flask app:
    First you will setup a basic Flask app in 0-app.py. Create a single / route and an index.html template that simply outputs “Welcome to Holberton” as page title (<title>) and “Hello world” as header (<h1>).


1. Basic Babel setup:
    In order to configure available languages in our app.
    you will create a Config class that has a LANGUAGES class attribute equal to ["en", "fr"].

2. Get locale from request
    Create a get_locale function with the babel.localeselector decorator.
    Use request.accept_languages to determine the best match with our supported languages.
