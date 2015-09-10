#!/usr/bin/env python3
# This is a simple 4 banger calculator

LICENSE = """DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                    Version 2, December 2004

 Copyright (C) 2015 Arti Zirk <arti.zirk@gmail.com>

 Everyone is permitted to copy and distribute verbatim or modified
 copies of this license document, and changing it is allowed as long
 as the name is changed.

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. You just DO WHAT THE FUCK YOU WANT TO.
"""

"""
# Calculator

This program can calculate numbers

# Examples

>>> c = Calculator()
>>> print(c.calculate("1+1"))
2
>>>

# Tests

$ python3 -m unittest main.py

"""

import re
import unittest

class EvalCalculator():
    """Calculator class implementing a simple calculator using python built in
    `eval` function to make my life easier"""

    input_filter = re.compile(r"^[0-9\+\-\\\*\(\)\.]*$")
    def calculate(self, input_string):
        if not self.input_filter.match(input_string):
            raise SyntaxError("Input string contains invalid characters")
        result = eval(input_string)  # CHEATING
        return result

class Calculator(EvalCalculator):
    """This is a propper calculator.
    It will in theory convert string to a list of numbers and operands and then
    use reverse polish notation to calculate everything"""

    def parse_to_list(self, input_string):
        """Converts input_string to list of numbers and """
        the_list = []
        a_number = []
        for char in input_string:
            if char.isdigit():
                a_number.append(char)
            elif char == ".":
                a_number.append(char)
            elif char in ("()*/+-"):
                if a_number:
                    number = "".join(a_number)
                    if "." in number:
                        number = float(number)
                    else:
                        number = int(number)
                    the_list.append(number)
                    number = None
                the_list.append(char)

    def convert_to_rpn(self, input_list):
        """Converts list generated by `parse_to_list` to
           reverse polish notation  (lisp?)"""
        raise NotImplemented("http://andreinc.net/2010/10/05/converting-infix-to-rpn-shunting-yard-algorithm/")

    def calculate(self, input_string):
        if not self.input_filter.match(input_string):
            raise SyntaxError("Input string contains invalid characters")
        the_list = self.parse_to_list(input_string)
        rpn_list = self.convert_to_rpn(the_list)
        raise NotImplemented("Can't yet calculate this")


class TestEvalCalculator(unittest.TestCase):
    """Tests for calculator class using `eval`"""

    def setUp(self):
        self.calculator = EvalCalculator()

    def calc(self, input_string, output_val):
        self.assertEqual(self.calculator.calculate(input_string), output_val)

    def test_1p1(self):
        self.calc("1+1", 2)

    def test_2t2(self):
        self.calc("2*2", 4)

    @unittest.expectedFailure
    def test_syntax(self):
        self.calc("1+1a", 2)

class TestCalculator(TestEvalCalculator):
    """Tests for calculator class using real parsing"""

    def setUp(self):
        self.calculator = Calculator()


if __name__ == "__main__":
    calc = EvalCalculator()
    result = calc.calculate("1+1")
    print(result)
