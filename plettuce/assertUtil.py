# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, with_statement

from nose.tools import assert_true as nose_assert_true
from nose.tools import assert_false as nose_assert_false


import logging
logger = logging.getLogger(__name__)
# pylint:disable=missing-docstring,redefined-outer-name,redefined-builtin
# pylint:disable=invalid-name

def _encode(content):
    if isinstance(content, unicode):
        return content.encode('utf-8')
    else:
        return content

class AssertContextManager():
    def __init__(self, step):
        self.step = step

    def __enter__(self):
        pass

    def __exit__(self, type, value, traceback):
        step = self.step
        if traceback:
            if isinstance(value, AssertionError):
                error = AssertionError("feature> %s, scenario> %s: %s, failed because: %s" % \
                    (_encode(self.step.scenario.feature.name), _encode(self.step.scenario.name), _encode(self.step.sentence), _encode(value.message)))
            else:
                sentence = "feature> %s, scenario> %s: %s, failed because: %s" % \
                    (_encode(self.step.scenario.feature.name), _encode(self.step.scenario.name), _encode(self.step.sentence), _encode(str(value)))
                error = AssertionError(sentence)
            raise error, None, traceback


def assert_true(step, exp, msg=None):
    with AssertContextManager(step):
        nose_assert_true(exp, msg)


def assert_false(step, exp, msg=None):
    with AssertContextManager(step):
        nose_assert_false(exp, msg)
