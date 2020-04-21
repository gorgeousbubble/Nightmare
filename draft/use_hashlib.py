import hashlib


def test_hashlib_md5():
    md5 = hashlib.md5()
    md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
    print(md5.hexdigest())


if __name__ == '__main__':
    test_hashlib_md5()
