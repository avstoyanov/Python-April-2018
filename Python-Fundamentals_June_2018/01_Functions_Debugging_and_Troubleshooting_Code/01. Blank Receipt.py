
def header():
    return "CASH RECEIPT\n------------------------------"


def body():
    return "Charged to____________________\nReceived by___________________"


def footer():
    return "------------------------------\n\u00A9 SoftUni"


def receipt():
    print(header())
    print(body())
    print(footer())


receipt()
