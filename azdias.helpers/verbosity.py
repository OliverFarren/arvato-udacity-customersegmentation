DEBUG = 100
HIGH = 75
MED = 50    
LOW = 25
NONE = 0

class VerbosityPrinter:
    '''
    Conditional printing based on supplied verbosity_level parameter.

    Where verbosity_level is a dynamic parameter, this class can be used to configure
    print outs to only occur at the desired level of verbosity.

    Verbosity levels are:

    DEBUG - Highest level, print all messages
    HIGH - High, print .high, .medium, .low and .none messages
    Med - Medium, print .medium, .low and .none messages
    Low - Low, print .low and .none messages
    NONE - None, print .none messages

    example:

    import verbosity as v

    def my_func(verbosity):

        vp = v.VerbosityPrinter(verbosity)

        vp.none("Running my_func.")
        vp.high("Hello World!")

    >> myfunc(v.DEBUG)
    >> Running my_func.
    >> Hello World!
    >> myfunc(v.LOW) 
    >> Running my_func.
    '''


    def __init__(self,verbosity_level):
        self.verbosity_level = verbosity_level

    @property
    def is_debug(self):
        return(self.verbosity_level >= DEBUG)
        
    def debug(self,*args,**kwargs):
        if self.is_debug:
            print(*args,**kwargs)
            
    @property
    def is_high(self):
        return(self.verbosity_level >= HIGH)
        
    def high(self,*args,**kwargs):
        if self.is_high:
            print(*args,**kwargs)

    @property
    def is_med(self):
        return(self.verbosity_level >= MED)
        
    def med(self,*args,**kwargs):
        if self.is_med:
            print(*args,**kwargs)

    @property
    def is_low(self):
        return(self.verbosity_level >= LOW)
        
    def low(self,*args,**kwargs):
        if self.is_low:
            print(*args,**kwargs)

    @property
    def is_none(self):
        return(self.verbosity_level >= NONE)

    def none(self,*args,**kwargs):
        if self.is_none:
            print(*args,**kwargs)