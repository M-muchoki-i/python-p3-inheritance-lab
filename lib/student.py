#!/usr/bin/env python

from user import User

class Student(User):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Initialize inherited attributes
        self.knowledge = []  # Initialize an empty knowledge list

    def learn(self, knowledge_str):
        """Add a string to the student's knowledge list."""
        self.knowledge.append(knowledge_str)