import inspect

def func_name():
    '''Returns the name of the function which called this function
        i.e.
        def foo():
            print(f'This function is named: {func_name()}')

        >> foo()
        >> This function is named: foo
    '''
    return (inspect.getouterframes(inspect.currentframe())[1].function)