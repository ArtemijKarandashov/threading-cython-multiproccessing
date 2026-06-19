
import math
import timeit
import integrate_cython

if __name__=="__main__":
    from task import integrate_with_threads, integrate_with_processes, integrate

    _N_ITER = 1_000_00
    _TIMEIT_ITERATIONS = 100
    _INTEGRATE_ARGS = f"math.sin, 0, math.pi, n_iter={_N_ITER}"

    print(f"Установлены аргументы для integrate: ({_INTEGRATE_ARGS})")

    print("Замеряю вермя работы функции без оптимизации...")
    default_time = timeit.timeit(stmt=f"integrate({_INTEGRATE_ARGS})",
                                 number=_TIMEIT_ITERATIONS,
                                 globals=globals())
    
    print("Замеряю вермя работы функции с использованием потоков...")
    time_with_threads = timeit.timeit(stmt=f"integrate_with_threads({_INTEGRATE_ARGS})", 
                                      number=_TIMEIT_ITERATIONS, 
                                      globals=globals())
    
    print("Замеряю вермя работы функции с использованием процессов...")
    time_with_processes = timeit.timeit(stmt=f"integrate_with_processes({_INTEGRATE_ARGS})", 
                                        number=_TIMEIT_ITERATIONS,
                                        globals=globals())


    print("Замеряю вермя работы Cython функции...")
    c_default_time = timeit.timeit(stmt=f"integrate_cython.integrate_c({_INTEGRATE_ARGS})", 
                                   number=_TIMEIT_ITERATIONS, 
                                   globals=globals())

    print("Замеряю вермя работы Cython функции с потоками...")
    c_threads_time = timeit.timeit(stmt=f"integrate_with_threads({_INTEGRATE_ARGS}, integrate = integrate_cython.integrate_c)", 
                                   number=_TIMEIT_ITERATIONS, 
                                   globals=globals())
    
    print("Замеряю вермя работы Cython функции с процессами...")
    c_processes_time = timeit.timeit(stmt=f"integrate_with_processes({_INTEGRATE_ARGS}, integrate = integrate_cython.integrate_c)", 
                                   number=_TIMEIT_ITERATIONS, 
                                   globals=globals())


    print(f"\n{"-"*50}")
    print(f"Без оптимизаций: {default_time}")
    print(f"Общее время используя потоки: {time_with_threads}")
    print(f"Общее время используя процессы: {time_with_processes}")
    print(f"Cython: {c_default_time}")
    print(f"Cython + потоки: {c_threads_time}")
    print(f"Cython + процессы: {c_processes_time}")

