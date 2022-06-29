def hello():
    print('Hello my friend')


def sabaiydee():
    print('ສະບາຍດີໝູ່')


def nihao():
    print('ໜີຫ້າວ')


def xincao():
    print('ສິນຈ້າວ')


while True:
    friend = input('Where are you from? : ')

    if friend == 'England':
        hello()
    elif friend == 'Laos':
        sabaiydee()
    elif friend == 'Vietnam':
        xincao()

    else:
        nihao()
