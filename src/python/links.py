import numpy as np


class Link:
    def __init__(self):
        pass


class IdentityLink(Link):
    def __str__(self):
        return "identity"

    @staticmethod
    def f(x):
        return x

    @staticmethod
    def finv(x):
        return x


class LogitLink(Link):
    def __str__(self):
        return "logit"

    @staticmethod
    def f(x):
        return np.log(x/(1-x))

    @staticmethod
    def finv(x):
        return 1/(1+np.exp(-x))


def get_link_object(val):
    if isinstance(val, Link):
        return val
    else:
        assert False, "Passed link object must be a subclass of iml.Link"
