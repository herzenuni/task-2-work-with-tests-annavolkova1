import json

filename = 'data.json'
def read(filename):
    """
    >>> read('data.json')
    ***************************************************************
    company: PARCOE
    email: muriellott@parcoe.com
    phone: +1 (983) 418-2041
    address: 623 Hoyt Street, Waverly, Washington, 4681
    ***************************************************************
    company: COMTOURS
    email: reedlogan@comtours.com
    phone: +1 (801) 482-3149
    address: 334 Batchelder Street, Worcester, Massachusetts, 2966
    ***************************************************************
    company: APPLICA
    email: bobbiemathews@applica.com
    phone: +1 (966) 405-3143
    address: 991 Sackman Street, Caron, Maine, 5334
    ***************************************************************
    company: BOILICON
    email: gilmorehendrix@boilicon.com
    phone: +1 (978) 536-2130
    address: 917 Minna Street, Emerald, District Of Columbia, 4497
    ***************************************************************
    company: PERMADYNE
    email: stellaworkman@permadyne.com
    phone: +1 (997) 448-3432
    address: 696 Brightwater Avenue, Welda, Mississippi, 9203
    'data'
    """

    with open(filename, encoding='utf-8') as data_file:
        data = json.load(data_file)

    for tmp in data:
        print("***************************************************************")
        print("company: {}".format(tmp["company"]))
        print("email: {}".format(tmp["email"]))
        print("phone: {}".format(tmp["phone"]))
        print("address: {}".format(tmp["address"]))

    return "data"

if __name__ == '__main__':   
    import doctest
    doctest.testmod()