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
    assert(push("21.589225 Euros")==21.589225)

    
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
    assert(testo('{ "from" : "25 United States Dollars", "to" : "21.589225 Euros", "success" : true, "error" : "" }')==21.589225)
    assert(testo('{ "from" : "", "to" : "", "success" : false, "error" : "Source currency code is invalid." }')=='error:"Source currency code is invalid." ')
    

def exchange(currency_from, currency_to, amount_from):
    """In this exchange, the user is changing amount_from money in 
    currency currency_from to the currency currency_to. The value 
    returned represents the amount in currency currency_to."""

    ff=currency_from.upper()
    tt=currency_to.upper()
    aa=amount_from

    pstr="http://cs1110.cs.cornell.edu/2016fa/a1server.php?from="+ff+"&to="+tt+"&amt="+aa
    doc = urlopen(pstr)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    return(testo(jstr))


def test_exchange():
    assert(exchange("USD","EUR",25.0)==21.589225)
    assert(exchange("usd","eur",25)==21.589225)
    assert(exchange("usd","eur",25)==21.589225)
    assert(exchange("usa","ppp",40)=='error:"Source currency code is invalid." ')


def test_all():
    """test all cases"""
    test_push()
    test_testo()
    test_exchange()
    print("All tests passed")


def main():
    cf=input()
    ct=input()
    af=input()
    print(exchange(cf, ct, af))
    test_all()

if __name__ == '__main__':
    main()
