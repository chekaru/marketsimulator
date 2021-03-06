# generated with class generator.python.random$Import
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
@registry.expose(["Random", "paretovariate"])
class paretovariate_Float(IFunctionfloat):
    """ **Pareto distribution**
    
    
    Parameters are:
    
    **Alpha**
    	 |alpha| is the shape parameter
    """ 
    def __init__(self, Alpha = None):
        self.Alpha = Alpha if Alpha is not None else 1.0
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'Alpha' : float
    }
    
    
    def __repr__(self):
        return "paretovariate(%(Alpha)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        
        
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        
        
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def typecheck(self):
        from marketsim import rtti
        rtti.typecheck(float, self.Alpha)
    
    def registerIn(self, registry):
        if self.__dict__.get('_id', False): return
        self.__dict__['_id'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        registry.insert(self)
        
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.registerIn(registry)
        self.__dict__['_processing_ex'] = False
    
    def __call__(self, *args, **kwargs):
        import random
        return random.paretovariate(self.Alpha)
    
    def _casts_to(self, dst):
        return paretovariate_Float._types[0]._casts_to(dst)
    
def paretovariate(Alpha = None): 
    from marketsim import rtti
    if Alpha is None or rtti.can_be_casted(Alpha, float):
        return paretovariate_Float(Alpha)
    raise Exception('Cannot find suitable overload for paretovariate('+str(Alpha) +':'+ str(type(Alpha))+')')
