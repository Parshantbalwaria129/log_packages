from loggers.mylog import enable_error_logging

@enable_error_logging
def func5():
    print('func5')
    raise EOFError

@enable_error_logging
def func1():
    @enable_error_logging
    def func4():
        print('hello')
        func5()
        raise BufferError
    
    print("Next Level")
    func4()
    print("Please run")

    raise ConnectionRefusedError

@enable_error_logging
class Hello:
    def __init__(self) -> None:
        pass

    @enable_error_logging
    def my_func2(self):
        # print(2/0)
        print('****************************')
        raise ValueError




@enable_error_logging
class MyClass:
    
    def __init__(self) -> None:
        pass

    def my_method(self):
        print("my_method")
        a = Hello()
        a.my_func2()
        print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
        func1()
        print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
        a.my_func2()
        print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')

        

        return "HIIII"

    def my_func(self):
        print('helloWorld')
        raise ZeroDivisionError


@enable_error_logging
class Hello2(MyClass):


    def __init__(self) -> None:
        super().__init__()
    
    def my_func3(self):
        print('my_func3')
        raise TypeError


if __name__ == "__main__":
    
    print('start')
    obj = MyClass()
    print('obj.my_method()::',obj.my_method())
    obj.my_func()
    a = Hello2()
    a.my_func3()
    print("================================================")