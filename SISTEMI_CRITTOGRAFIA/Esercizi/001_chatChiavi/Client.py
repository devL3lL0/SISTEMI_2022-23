import random
import time
import config as conf

def main():
    random.seed(int(time.time()))
    a = conf.ottieniNumeroRandom()
    ga = conf.modexp(conf.G, a, conf.P)
    conf.Client(ga)
    print(f"Numero {ga} inviato!")
    gb = conf.Server()
    gab = conf.modexp(gb, a, conf.P)
    print(f"Il numero segreto è {gab}")

if __name__ == '__main__':
    main()