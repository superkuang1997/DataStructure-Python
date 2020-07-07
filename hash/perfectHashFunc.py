import hashlib

code1 = hashlib.md5('hello_world'.encode('utf-8')).hexdigest()
code2 = hashlib.sha1('hello_world'.encode('utf-8')).hexdigest()

m = hashlib.md5()
m.update('hello'.encode('utf-8'))
m.update('_world'.encode('utf-8'))

print(code1)
print(code2)
print(m.hexdigest())