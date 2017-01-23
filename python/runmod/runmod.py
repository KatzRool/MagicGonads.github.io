def time(*funcs_args,rep=1,num=1):
    """Evaluate execution time for a set of functions
    *funcs_args is of the form (function,'*args')"""
    import timeit
    timeit._runmod = get(__file__)
    for func in funcs_args:
        exec('timeit._runmod.'+func[0].__name__+'= func[0]')
        print(timeit.repeat(number=num,repeat=rep,stmt='_runmod.'+func[0].__name__+'('+func[1]+')'))
    del timeit._runmod
def get(path):
    'Return module reference from file path'
    import sys
    path = path.split('\\')
    sys.path.insert(0, '\\'.join(path[:-1]))
    module = path[-1].split('.')[0]
    exec('import '+module)
    return eval(module)
def set(module):
    'Natively import a module reference'
    globals()[module.__name__]=module
def merge(module,newmod):
    'Merges global variables from a new module into another'
    for var in newmod.__dir__():
        if var[0] != '_':
            exec(module.__name__+'.'+var+'=newmod.'+var)
def call(*funcs_args):
    result = {}
    for func in funcs_args:
        call = func[0].__name__+str(func[1:])
        result[call] = eval(call)
    return result
