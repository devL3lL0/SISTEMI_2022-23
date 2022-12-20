import random
import time
import config as conf


def main():
    random.seed(int(time.time()))
    b = conf.ottieniNumeroRandom()
    gb = conf.modexp(conf.G, b, conf.P)
    ga = conf.Server()
    conf.Client(gb)
    print(f"Numero {gb} inviato!")
    gab = conf.modexp(ga, b, conf.P)
    print(f"Il numero segreto è {gab}")


if __name__ == '__main__':
    main()
