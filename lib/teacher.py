#!/usr/bin/env python

from user import User

import random

class Teacher(User):
     knowledge = [
        "str is a data type in Python",
        "programming is hard, but it's worth it",
        "JavaScript async web request",
        "Python function call definition",
        "object-oriented teacher instance",
        "programming computers hacking learning terminal",
        "pipenv install pipenv shell",
        "pytest -x flag to fail fast",
    ]

     def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Initialize inherited attributes
        self.knowledge = Teacher.knowledge.copy()  # Instance attribute copy

     def teach(self):
        # Choose a random index in the range 0 to len(self.knowledge) - 1
        index = random.randint(0, len(self.knowledge) - 1)
        return self.knowledge[index]
    