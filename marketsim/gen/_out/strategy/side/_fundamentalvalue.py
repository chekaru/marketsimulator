# generated with class generator.python.constructor$Import
from marketsim import registry
from marketsim.gen._out.strategy.side._fundamentalvaluestrategy import FundamentalValueStrategy
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
@registry.expose(["-", "FundamentalValue"])
class FundamentalValue_Float(FundamentalValueStrategy):
    """ 
    """ 
    def __init__(self, fv = None):
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import deref_opt
        self.fv = fv if fv is not None else deref_opt(_constant_Float(200.0))
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'fv' : IFunctionfloat
    }
    
    
    def __repr__(self):
        return "FundamentalValue(%(fv)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        self.fv.bind_ex(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        
        self.fv.reset_ex(generation)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def typecheck(self):
        from marketsim import rtti
        from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
        rtti.typecheck(IFunctionfloat, self.fv)
    
    def registerIn(self, registry):
        if self.__dict__.get('_id', False): return
        self.__dict__['_id'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        registry.insert(self)
        self.fv.registerIn(registry)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.registerIn(registry)
        self.__dict__['_processing_ex'] = False
    

    @property
    def Fundamental_Value(self):
        from marketsim.gen._out.strategy.side._fundamental_value import Fundamental_Value
        return Fundamental_Value(self)
    
    @property
    def book(self):
        from marketsim.gen._out.strategy.side._book import book
        return book(self)
    
    @property
    def Side(self):
        from marketsim.gen._out.strategy.side._side import Side
        return Side(self)
    
    def Strategy(self, eventGen = None,orderFactory = None):
        from marketsim.gen._out.strategy.side._strategy import Strategy
        return Strategy(self,eventGen,orderFactory)
    
    @property
    def Fv(self):
        from marketsim.gen._out.strategy.side._fv import Fv
        return Fv(self)
    
    pass
FundamentalValue = FundamentalValue_Float
