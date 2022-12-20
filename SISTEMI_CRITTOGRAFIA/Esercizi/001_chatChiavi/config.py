import random
from socket import socket, AF_INET, SOCK_STREAM

P = 0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff
G = 5

def ottieniNumeroRandom():
    n = random.randint(1, P-2)
    return n

def modexp(a,b,n):
    acc = 1
    while b > 0:
        if b % 2 == 1:
            acc = (acc * a) % n
        a = (a*a) % n
        b = b // 2
    return acc

def encode_big(n):
    return str(n).encode('utf8')

def decode_big(s):
    return int(s[0].decode('utf8'))


def Client(data):
    addres = str(input("Inserire l'ip del server: "))
    with socket(AF_INET, SOCK_STREAM) as s:
        address = (addres, 5000)
        s.connect(address)
        s.sendall(encode_big(data))
        s.close()

def Server():
    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind(('0.0.0.0', 5000))
        s.listen()
        print("In ascolto: ")
        client, client_address = s.accept()
        n = client.recvfrom(4096)
        g = decode_big(n)
        print(g)
        s.close()
    return g
    
