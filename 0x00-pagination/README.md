# Project Name

## Contents

- [Resources](#resources)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Setup](#setup)

## Resources

### Read or watch:

- [REST API Design: Pagination](https://restfulapi.net/pagination/)
- [HATEOAS (Hypertext As The Engine Of Application State)](https://restfulapi.net/hateoas/)

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- How to paginate a dataset with simple page and page_size parameters
- How to paginate a dataset with hypermedia metadata
- How to paginate in a deletion-resilient manner

## Requirements

- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle style (version 2.5.*)
- The length of your files will be tested using `wc`
- All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your functions should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class, or method (the length of it will be verified)
- All your functions and coroutines must be type-annotated.

## Setup

### Data File

Use the provided data file `Popular_Baby_Names.csv` for your project.


## TASKS - mandatory

1. Write a function named index_range that takes two integer arguments page and page_size.
2. Simple pagination.
3. 2. Hypermedia pagination
