def modexp(a,b,n):
    acc = 1
    while b > 0:
        if b % 2 == 1:
            acc = (acc *a) % n
        a = (a*a) % n
        b = b // 2
    return acc

def encode_big(n):
    return str(n).encode('utf8')

def decode_big(s):
    return  int(s.decode('utf8'))