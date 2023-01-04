# Testing Assignment

This assigment will introduce you to the pytest framework. We will 
be implementing some tests for the [pydantic](https://docs.pydantic.dev/)
package, a very popular python package for data modeling, parsing, and validation,
so be sure to install it first. Looking over a basic pydantic tutorial (such as
[this one](https://towardsdatascience.com/how-to-make-the-most-of-pydantic-aa374d5c12d))
may also be helpful.

## Task 1: Basic Test Features (10 points)

Look at test_task_1.py and fill in the test functions.

## Task 2: Fixtures (10 points)

Look at test_task_2.py and fill in the fixtures. Don't modify the tests.

## Task 3: Marks and Configuration (5 points)

Look at test_task_3.py and perform required actions. Create a custom mark called 
"long_running" and a pyproject.toml or pytest.ini file in which the mark is registered.
See: https://docs.pytest.org/en/7.1.x/how-to/mark.html#registering-marks


Next, passed the pytest command line flags to run *only* tests marked with 'long-running':


Next, the command line flags to skip tests marked with 'long-running':



## Acknowledgements
Data from [devstronomy](https://devstronomy.com/). 
