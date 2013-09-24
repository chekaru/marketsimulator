from types import *
import ops

from _impl import mathops 

defs = mathops.defs

@mathops.imported("Log/Pow", "exp")
class Exp:
    """ Return e**x """
    
    source = IFunction[float]()
    
