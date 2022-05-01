# first install pytst module 
# pip install pytest
# make sure to start the test file with test_ or end with _test


def testLogin():
    print("Login Successful")

def testLogOff():
    print("LogOff Successful")

def testCalculation():
    assert 2+2 == 4