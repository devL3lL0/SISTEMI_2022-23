from socket import socket, AF_INET, SOCK_STREAM
import random
import time
from lib import modexp, encode_big, decode_big

P = 23
#p = 0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff
g = 2


def ottieniNumeroRandom():
    n = random.randint(1, P-2)
    return n


def Client(data, client):
    client.sendall(encode_big(data))


def Server(client, a, p):
    nb = client.recvfrom(4096)
    gb = decode_big(nb)
    gab = modexp(gb, a, p)
    return gab


def main():
    random.seed(int(time.time()))
    a = ottieniNumeroRandom()
    ga = modexp(g, a, P)
    print(ga)
    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind(('0.0.0.0', 5000))
        s.listen()
        client, client_address = s.accept()
        Client(ga, client)
        gab = Server()
    print(gab)

if __name__ = '__main__':
    main()
