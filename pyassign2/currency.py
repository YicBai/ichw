"""A module for exchange rate query.You can use the function 'exchange'"""


from urllib.request import urlopen


def push(slice1):
    """get the amount in currency currency_to out as a float"""
    ret=""
    i=0
    for i in range(len(slice1)):
        if 46<=ord(slice1[i])<=57:
            ret=ret+slice1[i]
        else:
            pass
        i=i+1
    reret=float(ret)
    return reret 


def test_push():
    return(push("21.589225 Euros")==21.589225)


def testo(jstr):
    """test if the user's input is valid"""
    ft=jstr.find("to")
    fs=jstr.find("success")
    fe=jstr.find("error")
    slice1=jstr[ft+7:fs-4]
    slice2=jstr[fs+11:fe-3]
    slice3=jstr[fe+9:-1]
    if slice2=="true":
        return(push(slice1))
    else:
        reret="error:"+slice3
        return reret


def test_testo():
    pr1=testo('{ "from" : "25 United States Dollars", "to" : "21.589225 Euros", "success" : true, "error" : "" }')==21.589225
    pr2=testo('{ "from" : "", "to" : "", "success" : false, "error" : "Source currency code is invalid." }')=='error:"Source currency code is invalid." '
    return(pr1 and pr2)


def exchange(currency_from, currency_to, amount_from):
     """Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in 
    currency currency_from to the currency currency_to. The value 
    returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code

    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""

    ff=currency_from.upper()
    tt=currency_to.upper()
    aa=str(float(amount_from))

    pstr="http://cs1110.cs.cornell.edu/2016fa/a1server.php?from="+ff+"&to="+tt+"&amt="+aa
    doc = urlopen(pstr)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    return(testo(jstr))


def test_exchange():
    ex1=exchange("USD","EUR",25.0)==21.589225
    ex2=exchange("usd","eur",25)==21.589225
    ex3=exchange("usd","eur",25)==21.589225
    ex4=exchange("usa","ppp",40)=='error:"Source currency code is invalid." '
    return(ex1 and ex2 and ex3 and ex4)


def test_all():
    """test all cases"""
    t1=test_push()
    t2=test_testo()
    t3=test_exchange()
    if t1==False:
        print("test_push has not passed")
    elif t2==False:
        print("test_testo has not passed")
    elif t3==False:
        print("test_exchange has not passed")
    else:
        print("All tests passed")
