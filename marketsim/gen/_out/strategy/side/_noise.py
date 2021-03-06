# generated with class generator.python.constructor$Import
from marketsim import registry
from marketsim.gen._out.strategy.side._sidestrategy import SideStrategy
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
@registry.expose(["-", "Noise"])
class Noise_Float(SideStrategy):
    """ 
    """ 
    def __init__(self, side_distribution = None):
        from marketsim.gen._out.math.random._uniform import uniform_FloatFloat as _math_random_uniform_FloatFloat
        from marketsim import deref_opt
        self.side_distribution = side_distribution if side_distribution is not None else deref_opt(_math_random_uniform_FloatFloat(0.0,1.0))
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'side_distribution' : IFunctionfloat
    }
    
    
    def __repr__(self):
        return "Noise(%(side_distribution)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        self.side_distribution.bind_ex(self._ctx_ex)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        
        self.side_distribution.reset_ex(generation)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def typecheck(self):
        from marketsim import rtti
        from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
        rtti.typecheck(IFunctionfloat, self.side_distribution)
    
    def registerIn(self, registry):
        if self.__dict__.get('_id', False): return
        self.__dict__['_id'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        registry.insert(self)
        self.side_distribution.registerIn(registry)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.registerIn(registry)
        self.__dict__['_processing_ex'] = False
    

    @property
    def Side_distribution(self):
        from marketsim.gen._out.strategy.side._side_distribution import Side_distribution
        return Side_distribution(self)
    
    def Strategy(self, eventGen = None,orderFactory = None):
        from marketsim.gen._out.strategy.side._strategy import Strategy
        return Strategy(self,eventGen,orderFactory)
    
    @property
    def Side(self):
        from marketsim.gen._out.strategy.side._side import Side
        return Side(self)
    
    pass
Noise = Noise_Float
