# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, with_statement

from nose.tools import assert_true as nose_assert_true
from nose.tools import assert_false as nose_assert_false

# pylint:disable=missing-docstring,redefined-outer-name,redefined-builtin
# pylint:disable=invalid-name

class AssertContextManager():
    def __init__(self, step):
        self.step = step

    def __enter__(self):
        pass

    def __exit__(self, type, value, traceback):
        step = self.step
        if traceback:
            if isinstance(value, AssertionError):
                error = AssertionError(self.step.sentence)
            else:
                sentence = "%s, failed because: %s" % (step.sentence, value)
                error = AssertionError(sentence)
            raise error, None, traceback


def assert_true(step, exp, msg=None):
    with AssertContextManager(step):
        nose_assert_true(exp, msg)


def assert_false(step, exp, msg=None):
    with AssertContextManager(step):
        nose_assert_false(exp, msg)