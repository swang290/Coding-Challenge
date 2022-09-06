from time import perf_counter
import tracemalloc

def log_it(function):
    def wrapper(*args, **kwargs):
        try:
            tracemalloc.start()
            before = perf_counter()
            var = function(*args, **kwargs)
            current, peak = tracemalloc.get_traced_memory()
            after = perf_counter()
            signature = ", ".join([str(arg) for arg in args])
            t = type(signature)
            with open("log report.txt", "a") as file:
                file.write("[LOG] function name: "+ f"{function.__name__}, argument: {signature}, Result: {var}, Type: {t}, Function took: {after - before:.6f} seconds, Memory usage: {current/10**6} MB, Peak memory usage: {peak/10**6} MB, Error: None "+"\n")
            tracemalloc.stop()
        except Exception as error:
            signature = ", ".join([str(arg) for arg in args])
            t = type(signature)
            with open("log report.txt", "a") as file:
                file.write("[LOG] function name: "+ f"{function.__name__}, argument: {signature}, Result: None, Type: {t}, Error: {str(error)}"+"\n")
            raise error
        return var
    return wrapper
    
@log_it
def cat_file(path):
    with open(path) as filehandle: 
            contents = filehandle.read()
    return contents


@log_it
def add(a,b):
    return a + b


add(1,10)
cat_file("names.txt")
cat_file("cat.txt")