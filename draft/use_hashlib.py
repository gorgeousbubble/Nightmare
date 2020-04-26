import hashlib


def test_hashlib_md5():
    md5 = hashlib.md5()
    md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
    print(md5.hexdigest())


def test_hashlib_sha1():
    sha1 = hashlib.sha1()
    sha1.update('how to use sha1 in '.encode('utf-8'))
    sha1.update('python hashlib?'.encode('utf-8'))
    print(sha1.hexdigest())


if __name__ == '__main__':
    test_hashlib_md5()
    test_hashlib_sha1()
