
def class_log(param):
    def class_decor(cls):
        methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
        for k, v in methods.items():
            setattr(cls, k, decorated(v))
        return cls

    def decorated(func):
        def wraper(*args, **kwargs):
            param.append(func.__name__)
            return func(*args, **kwargs)
        return wraper
    return class_decor


vector_log = []   # наименование (vector_log) в программе не менять!


@class_log(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value
