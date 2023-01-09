def arithmetic(a1:float,a2:float,sym:str):
    """Easy calculator
    + -, - -. * multiple, / split
    :param float a1: First number
    :param float a2: Second number
    :param str sym: Doing
    :rtype: var unknown format
    """
    if sym in ["+","-","/","*"]:
        if sym=='/' and a2==0:
            answ='Div/0'
        else:
            answ=eval(str(a1)+sym+str(a2))
    else:
        answ="Uknown move!"
    return answ

def is_year_leap(a:int):
    """
    Leap year or not
    insert year to check it
    :param int
    :rtype: bool
    """
    a=int(a)
    if a%4==0:
        b=True
    else:
        b=False
    return b

from math import *
def square(a:float):

    """
    insert square side
    give back Psquare, Ssquare, dSquare
    :param float
    :rtype:float
    """
    a=float(a)
    Psquare=a*4
    Ssquare=a*a
    dSquare=sqrt(a)
    return Psquare, Ssquare, dSquare

def season(a:int):
    """
    insert month number
    give back year season of that month.
    :param int
    :rtype: str
    """
    a=int(a)
    if a in range(3,6):
        a="Spring"
    elif a in range(6,9):
        a="Summer"
    elif a in range(9,12):
        a='Autumn'
    elif a==12 or a==1 or a==2:
        a='Winter'
    else:
        print('Not correct month number')
    return a

def bank(a:float, years:int):
    """
    Bank interest rates function
    return summ with percents
    :param a float: start summ
    :param years int: for how many years
    :rtype: float
    """
    a=float(a)
    years=int(years)

    S=a*(1+0.1)**years
    return S

def is_prime(a:int):
    """
    Enter number from 0 to 1000
    Return True if prime number and False if not
    :param float a: entered number
    :rtype: bool
    """
    a=int(a)
    for i in range(1, a+1):
        if a%i==0:
            b=False
        else:
            b=True
    