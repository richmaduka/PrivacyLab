'''
Purpose: Determine data type of data
'''
import re
import phonenumbers
from dateutil.parser import parse

# type class definitions


class NodeType(object):
    def __init__(self, value=None) -> None:
        value = object.value


class Address(NodeType):
    def __init__(self, value=None) -> None:
        value = value


class SSN(NodeType):
    def __init__(self, value=None) -> None:
        value = value


class Email_Address(NodeType):
    def __init__(self, value=None) -> None:
        value = value


class Phone_Number(NodeType):
    def __init__(self, value=None) -> None:
        value = value


class DateObj(NodeType):
    def __init__(self, value=None) -> None:
        value = value


class Sex(NodeType):
    def __init__(self, value=None) -> None:
        value = value


class CreditCard(NodeType):
    def __init__(self, value=None) -> None:
        value = value
