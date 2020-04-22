from multiprocessing import Pool
import time

CONTADOR = 50000000


def contagem_regressiva(n):
    while n > 0:
        n -= 1

if __name__ == '__main__':
    pool = Pool(processes=2)
    inicio = time.time()
    r1 = poll.apply_async