'''
Tests NodeType class
'''

import Check
import NodeClass


def test_email():
    assert Check.isEmail("asd@gmail.com")
    assert Check.isEmail("fgdsd") == False
    assert Check.isEmail("rick@yahoo.co")
    assert Check.isEmail(4567899) == False
    print('all isEmail() test passed.')


def test_sex():
    assert Check.isSex('M') == True
    assert Check.isSex('Man') == False
    assert Check.isSex('Female')
    assert Check.isSex('feMale')
    assert Check.isSex('Men') == False
    print('all isSex() tests passed.')


def test_ssn():
    assert Check.isSSN("12-234-2888") == False
    assert Check.isSSN("123456734") == False
    assert Check.isSSN("725-36-7765")
    print("all isSSN checks passed")


test_email()
test_sex()
test_ssn()
