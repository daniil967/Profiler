import cProfile, pstats

def profileit(func):
    def wrapper(*args, **kwargs):
        datafn = func.__name__ + ".profile" # Name the data file sensibly
        prof = cProfile.Profile()
        retval = prof.runcall(func, *args, **kwargs)
        prof.dump_stats(datafn)
        stream = open('profile.txt', 'w');
        p = pstats.Stats(datafn, stream=stream)
        p.strip_dirs().sort_stats('time').print_stats()
        return retval


    return wrapper