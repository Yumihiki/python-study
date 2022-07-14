
def try_except():
    print('---try_except start')
    try:
        print('try')
    except ZeroDivisionError:
        print('except')
    else:
        print('else')
    finally:
        print('finally')
    print('try_except finish---')


def eafp_style():
    """ EAFP Style

    認可をとるより許しを請う方が容易の意味。
    通常は有効なもの、と仮定して間違っていた場合に例外を捕捉するスタイル。
    """
    print('---eafp_style start')
    fruits = ['apple', 'banana', 'orange']
    try:
        fruits[4]
        print('try finish')
    except IndexError as e:
        print('IndexError!')
        print(e)
    print('eafp_style finish---')


def lbyl_style():
    """LBYL Style

    ころばぬ先の杖の意味。
    EAFP Styleとは異なり前提条件で判定をするスタイル。
    """
    print('---lbyl_style start')
    fruits_limit = 3
    fruits = ['apple', 'banana', 'orange']
    if fruits_limit == len(fruits):
        print('OK!')
    else:
        print('NG!')
    print('lbyl_style finish---')


if __name__ == "__main__":
    try_except()
    eafp_style()
    lbyl_style()
