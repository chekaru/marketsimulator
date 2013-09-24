from types import *
import ops

from _impl import mathops 

defs = mathops.defs

@mathops.imported("Log/Pow", "exp", "e^{%(x)s}")
class Exp:
    """ Return e**x """
    
    x = IFunction[float]()
    
