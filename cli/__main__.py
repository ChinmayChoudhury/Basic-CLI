import sys
from .classmodule import MyClass
from .funcmodule import my_function
from .helpmodule import show_help
from . import __version__
def main():
    print("in main")
    args = sys.argv[1:]
    print(args[0])
    #help
    if args[0] == "-h" or args[0] == "--help":
        show_help()
        exit()
    elif args[0] == "-v" or args[0] == "--version":
        print(f"chinmaycli v{__version__}")
    else:
        print("count of args :: {}".format(len(args)))
        for arg in args:
            print('passed argument :: {}'.format(arg))
    
    # my_function("fromfun_hello world")

    # my_obj = MyClass("from_obj")
    # my_obj.say_name()


if __name__ == '__main__':
    main()