"""Contains Fisher class
"""
from icecream import ic
from pythontemplate.common import BaseLearner


class Fisher(BaseLearner):
    """fisher algorithm
    """

    def __init__(self):
        BaseLearner.__init__(self)
        ic("fisher.init")
