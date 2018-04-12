
# import pytest

# return the number of spaces in the string
def numberOfSpaces(someString):
    count = 0
    for s in someString:
        if s==" ":
           count += 1
    return count

def test_numberOfSpaces_1():
    assert numberOfSpaces("UCSB")==0
    
def test_numberOfSpaces_2():
    assert numberOfSpaces("UC San Diego")==2
    
    
def test_numberOfSpaces_3():
    assert numberOfSpaces("Cal Poly")==1

def test_numberOfSpaces_ten_spaces():
    assert numberOfSpaces("          ")==10

def test_numberOfSpaces_space_begin_and_end():
    assert numberOfSpaces(" x ")==2
   
