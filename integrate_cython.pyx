def integrate_c(object f, double a, double b, *, int n_iter=100000):
    cdef double step = (b - a) / n_iter
    cdef double acc = f(a) + f(b)
    cdef int i

    for i in range(1, n_iter, 2):
        acc += 4 * f(a + i * step)
    for i in range(2, n_iter, 2):
        acc += 2 * f(a + i * step)
        
    return acc * step / 3
