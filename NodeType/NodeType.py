'''
Purpose: Determine data type of data
'''
import re
import phonenumbers
from dateutil.parser import parse

#type class definitions
class NodeType(object):
    def __init__(self, value = None) -> None:
        value = value


class Address(NodeType):
    def __init__(self, value = None) -> None:
        value = value


class SSN(NodeType):
    def __init__(self, value = None) -> None:
        value = value


class Email_Address(NodeType):
    def __init__(self, value = None) -> None:
        value = value


class Phone_Number(NodeType):
    def __init__(self, value = None) -> None:
        value = value


class DateObj(NodeType):
    def __init__(self, value = None) -> None:
        value = value


class Sex(NodeType):
    def __init__(self, value = None) -> None:
        value = value


class CreditCard(NodeType):
    def __init__(self, value = None) -> None:
        value = value


'''
- Functions for checking data type
'''

def isEmail(data: any) -> bool:
    '''
    pass the regular expression
    and the string into the fullmatch() method
    Make a regular expression
    for validating an Email
    '''
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, data)):
        return True


def isPhoneNumber(data: any) ->bool:
    '''
    1) Begins with 0 or 91
    2) Then contains 7 or 8 or 9.
    3) Then contains 9 digits
    '''
    length = len(data)
    Pattern = re.compile("(0|91)?[7-9][0-9]{9}")


def isAddress(data: any) -> bool:
    '''
    Check if the data is an address using regex
    '''
    if re.match(r"(^[0-9]{1,5}\s)([A-Za-z]{1,}(\#\s|\s\#|\s\#\s|\s)){1,5}([A-Za-z]{1,}\,|[0-9]{1,}\,)(\s[a-zA-Z]{1,}\,|[a-zA-Z]{1,}\,)(\s[a-zA-Z]{2}\s|[a-zA-Z]{2}\s)([0-9]{5})"):
        return True
    elif re.match(r"(^[0-9]{1,5}\s)([A-Za-z]{1,}(\#\s|\s\#|\s\#\s|\s)){1,5}([A-Za-z]{1,}\,|[0-9]{1,}\,)(\s[a-zA-Z]{1,}\,|[a-zA-Z]{1,}\,)(\s[a-zA-Z]{2}\s|[a-zA-Z]{2,}\s)([0-9]{5})"):
        return True


def isSSN(data: any) -> bool:
    '''
    check if the object is an SSN
    '''
    if re.match(r"^(?!000|666)[0-8][0-9]{2}-(?!00)[0-9]{2}-(?!0000)[0-9]{4}$"):
        return True


def isSex(data: any) -> bool:
    '''
    Check if it is a valid sex.
    '''
    sexes = ["female", "male"]
    if data == 'M' or data == 'F':
        return True
    elif data.lower() in sexes:
        return True


def isDateObj(data: any) -> bool:
    """
    Return whether the string can be interpreted as a date.

    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    try: 
        parse(data, fuzzy=False)
        return True

    except ValueError:
        return False
    

def isCreditCard(data: any) -> bool:
    pass


def typeOfNode(data: any) -> NodeType:
    # Test data for type
    if isEmail(data):
        return Email_Address(value=data)
    elif isPhoneNumber(data):
        return Phone_Number(value=data)
    elif isCreditCard(value=data):
        return CreditCard(value=data)
    elif isAddress(data):
        return Address(value=data)
    elif isDateObj(data):
        return DateObj(value=data)
    elif isSex(data):
        return Sex(value=data)
    elif isSSN(data):
        return SSN(value=data)

