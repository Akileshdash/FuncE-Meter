import inspect
import gui


def get_functions(module):
    functions = {}
    for name, obj in inspect.getmembers(module):
        print(name)
        if inspect.isfunction(obj):
            functions[name] = [
                param.name for param in inspect.signature(obj).parameters.values()]
    return functions


if __name__ == "__main__":
    gui.GUI(get_functions)
