# Hash package interfaces
The Hash package function interfaces description.

## Introduction
Hash package is a functional package. It can offer different kind of hash algorithm interfaces. You can use this package to call hash calculate. Hash package based on the Python 'hash' package, it support multiple hash algorithms such as MD5, SHA1, SHA224, SHA256, SHA384, SHA512, SHA3_224, SHA3_256, SHA3_512, SHAKE128, SHAKE256, BLAKE2B, BLAKE2S, etc.

## Feature of package
The package is mainly used for hash calculate and checksum which has been realized by 'hash' package. You can refer to corresponding Python file.

#### Hash calculate and checksum
  * The hash package offer interfaces let program easy to realize hash calculate and checksum.
  * You can use the function 'hash_gen(s, t)' to generate a hash code, 's' indicate the original string which you want to calculate hash, 't' stand for hash algorithm like 'md5', 'sha1', etc.
  * You can use the function 'hash_check(s, r, t)' to checksum with hash code. If check success, it will return 'True', otherwise 'False'. So we can check file independence.
  * The package is useful and light.

## Usage of interfaces
There are many interfaces in this package. The hash package offer two function to generate hash code and check hash code called 'hash_gen' and 'hash_check'. Certainly, you can also use the others interface to realize more function. Now we support multiple hash algorithm like md5, sha1, sha224, sha256, sha384, sha512, sha3_224, sha3_256, sha3_384, sha3_512, shake2b, shake2s, hmac_md5, hmac_sha1, hmac_sha256, hmac_sha512, etc.

#### Generate hash code
You can call interface all like this. We exemplify 'md5' and 'sha1' to illustrate it.
```batch
    def test_hash_md5_encode(self):
        s = 'hello,world!'
        r = hash_gen(s, 'md5')
        print('hash md5 encode:', r)
    
    def test_hash_sha1_encode(self):
        s = 'hello,world!'
        r = hash_gen(s, 'sha1')
        print('hash sha1 encode:', r)
```

#### Check hash sum
You can call interface all like this. We exemplify 'md5' and 'sha1' to illustrate it.
```batch
    def test_hash_md5_check(self):
        s = 'hello,world!'
        r = 'c0e84e870874dd37ed0d164c7986f03a'
        self.assertTrue(hash_check(s, r, 'md5'))
        print('hash md5 check pass')
    
    def test_hash_sha1_check(self):
        s = 'hello,world!'
        r = '4518135c05e0706c0a34168996517bb3f28d94b5'
        self.assertTrue(hash_check(s, r, 'sha1'))
        print('hash sha1 check pass')
```