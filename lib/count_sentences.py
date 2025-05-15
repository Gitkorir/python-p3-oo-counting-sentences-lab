#!/usr/bin/env python3
import re

class MyString:
    def __init__(self, value=""):
        # Ensure value is a string
        if isinstance(value, str):
            self._value = value
        else:
            raise ValueError("Value must be a string")
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")
            self._value=""

    def is_sentence(self):
        """Returns True if value ends with a period."""
        return self.value.endswith(".")

    def is_question(self):
        """Returns True if value ends with a question mark."""
        return self.value.endswith("?")

    def is_exclamation(self):
        """Returns True if value ends with an exclamation mark."""
        return self.value.endswith("!")

    def count_sentences(self):
        """Counts number of sentences ending in ., !, or ?"""
        # Use regex to split on sentence-ending punctuation
        sentences = re.split(r'[.!?]+', self.value.strip())
        # Filter out any empty strings
        sentences = [s for s in sentences if s.strip()]
        return len(sentences)
