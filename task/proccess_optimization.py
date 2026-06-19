from .integrate import integrate

import concurrent.futures as ftres
from functools import partial

import math


def integrate_with_processes(f, a, b, *, n_jobs=4, n_iter=1000, integrate: callable = integrate):
    """
      - аннотировать аргументы
      - реализовать аналогичную функцию для вычисления с процессами (ProcessPoolExecutor)
      - оценить время работы программ с потоками и процессами и зафиксировать значения (2, 4, 6, 8(?))
    """

    executor = ftres.ProcessPoolExecutor(max_workers=n_jobs)
    spawn = partial(executor.submit, integrate, f, n_iter = n_iter // n_jobs)
    step = (b - a) / n_jobs
    #for i in range(n_jobs):
    #  print(f"Работник {i}, границы: {a + i * step}, {a + (i + 1) * step}")


    fs = [spawn(a + i * step, a + (i + 1) * step) for i in range(n_jobs)]

    return sum(list(f.result() for f in ftres.as_completed(fs)))

if __name__=="__main__":
    print(integrate_with_processes(math.sin, 0, math.pi))