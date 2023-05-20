import pyqrcode


def qr():
    s = 'paste any link, number, words here to convert to qr code '
    d = pyqrcode.create(s)
    d.png('hello.png', scale=6)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    qr()
