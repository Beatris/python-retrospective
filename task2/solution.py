from functools import reduce


def groupby(func, seq):
    group = {}
    for item in seq:
        key = func(item)
        group.setdefault(key, []).append(item)
    return group


def iterate(func):
    counter = 0
    while True:
        if counter:
            compose = reduce(lambda f, g: lambda x: f(g(x)), [func]*counter)
            yield compose
        else:
            yield lambda *args, **kwargs: args if len(args) > 1 else args[0]
        counter += 1


def zip_with(func, *iterables):
    min_len = None
    for iterable in iterables:
        iter_len = len(iterable)
        if min_len is None or iter_len < min_len:
            min_len = iter_len

    for i in range(min_len):
        yield func(*[iterable[i] for iterable in iterables])


def cache(func, cache_size):
    func_cached = {}
    items_in_cache = []

    def cache_checker(*args, **kwargs):
        if args not in func_cached.keys():
            result = func(*args, **kwargs)
            func_cached[args] = result
            items_in_cache.append(args)

            if len(items_in_cache) > cache_size:
                key_to_delete = items_in_cache[0]
                del items_in_cache[0]
                del func_cached[key_to_delete]

            return result
        else:
            return func_cached[args]

    return cache_checker