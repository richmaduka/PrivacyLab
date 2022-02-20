"""
gencc: A simple program to generate credit card numbers that pass the
MOD 10 check (Luhn formula).
Usefull for testing e-commerce sites during development.
by ..:: crazyjunkie ::.. 2014
"""

from random import Random, random
import copy

class Fake_Credit_Card:
    generator = Random()
    generator.seed()        # Seed from current time

    visaPrefixList = [
            ['4', '5', '3', '9'],
            ['4', '5', '5', '6'],
            ['4', '9', '1', '6'],
            ['4', '5', '3', '2'],
            ['4', '9', '2', '9'],
            ['4', '0', '2', '4', '0', '0', '7', '1'],
            ['4', '4', '8', '6'],
            ['4', '7', '1', '6'],
            ['4']]

    mastercardPrefixList = [
            ['5', '1'], ['5', '2'], ['5', '3'], ['5', '4'], ['5', '5']]

    amexPrefixList = [['3', '4'], ['3', '7']]

    discoverPrefixList = [['6', '0', '1', '1']]

    dinersPrefixList = [
            ['3', '0', '0'],
            ['3', '0', '1'],
            ['3', '0', '2'],
            ['3', '0', '3'],
            ['3', '6'],
            ['3', '8']]

    enRoutePrefixList = [['2', '0', '1', '4'], ['2', '1', '4', '9']]

    jcbPrefixList = [['3', '5']]

    voyagerPrefixList = [['8', '6', '9', '9']]


    def completed_number(self, prefix, length):
        """
        'prefix' is the start of the CC number as a string, any number of digits.
        'length' is the length of the CC number to generate. Typically 13 or 16
        """

        ccnumber = prefix

        # generate digits

        while len(ccnumber) < (length - 1):
            digit = str(self.generator.choice(range(0, 10)))
            ccnumber.append(digit)

        # Calculate sum

        sum = 0
        pos = 0

        reversedCCnumber = []
        reversedCCnumber.extend(ccnumber)
        reversedCCnumber.reverse()

        while pos < length - 1:

            odd = int(reversedCCnumber[pos]) * 2
            if odd > 9:
                odd -= 9

            sum += odd

            if pos != (length - 2):

                sum += int(reversedCCnumber[pos + 1])

            pos += 2

        # Calculate check digit

        checkdigit = ((sum / 10 + 1) * 10 - sum) % 10

        ccnumber.append(str(checkdigit))

        return ''.join(ccnumber)


    def credit_card_number(self, cc_type, length):
        if cc_type == "mastercard":
            prefixList = self.mastercardPrefixList
        elif cc_type == "visa":
            prefixList = self.visaPrefixList
        elif cc_type == "amex":
            prefixList = self.amexPrefixList
        elif cc_type == "discover":
            prefixList = self.discoverPrefixList
        elif cc_type == "diners":
            prefixList = self.dinersPrefixList
        elif cc_type == "enroute":
            prefixList = self.enRoutePrefixList
        elif cc_type == "jcb":
            prefixList = self.jcbPrefixList
        elif cc_type == "voyoger":
            prefixList = self.voyagerPrefixList

        ccnumber = copy.copy(self.generator.choice(prefixList))
        
        return cc_type, str(self.completed_number(ccnumber, length))[:-2] , self.generator.randint(100,999), str(self.generator.randint(1,12))+"/"+str(self.generator.randint(22,30))



