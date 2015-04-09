import decorator


def trampoline(f, *args, **kwargs):
    g = f(*args, **kwargs)
    while callable(g):
        g = g()
    return g

@decorator.decorator
def trampolined(f, *args, **kwargs):
    pass

