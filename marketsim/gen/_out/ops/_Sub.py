# generated with class generator.python.intrinsic_observable$Import
from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._intrinsic.ops import Sub_Impl
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
@registry.expose(["Ops", "Sub"])
class Sub_IObservableFloatIObservableFloat(Observablefloat,Sub_Impl):
    """ 
    """ 
    def __init__(self, x = None, y = None):
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import deref_opt
        Observablefloat.__init__(self)
        self.x = x if x is not None else deref_opt(_const_Float(1.0))
        self.y = y if y is not None else deref_opt(_const_Float(1.0))
        Sub_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IObservablefloat,
        'y' : IObservablefloat
    }
    
    
    def on_x_set(self, value):
        from marketsim import event
        event.subscribe_field(self, 'x', value)
    
    
    
    def on_y_set(self, value):
        from marketsim import event
        event.subscribe_field(self, 'y', value)
    
    def __repr__(self):
        return "({%(x)s}-{%(y)s})" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.bind_ex(self.__dict__['_ctx_ex'])
                else:
                    v.bind_ex(self.__dict__['_ctx_ex'])
        self.x.bind_ex(self._ctx_ex)
        self.y.bind_ex(self._ctx_ex)
        self.bind_impl(self.__dict__['_ctx_ex'])
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.reset_ex(generation)
                else:
                    v.reset_ex(generation)
        self.x.reset_ex(generation)
        self.y.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def typecheck(self):
        from marketsim import rtti
        from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
        rtti.typecheck(IObservablefloat, self.x)
        rtti.typecheck(IObservablefloat, self.y)
    
    def registerIn(self, registry):
        if self.__dict__.get('_id', False): return
        self.__dict__['_id'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        registry.insert(self)
        self.x.registerIn(registry)
        self.y.registerIn(registry)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.registerIn(registry)
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.registerIn(registry)
                else:
                    v.registerIn(registry)
        self.__dict__['_processing_ex'] = False
    
    def bind_impl(self, ctx):
        Sub_Impl.bind_impl(self, ctx)
    
    def reset(self):
        Sub_Impl.reset(self)
    
# generated with class generator.python.intrinsic_observable$Import
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim.gen._intrinsic.ops import Sub_Impl
@registry.expose(["Ops", "Sub"])
class Sub_FloatIObservableFloat(Observablefloat,Sub_Impl):
    """ 
    """ 
    def __init__(self, x = None, y = None):
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import deref_opt
        from marketsim.gen._out._const import const_Float as _const_Float
        Observablefloat.__init__(self)
        self.x = x if x is not None else deref_opt(_constant_Float(1.0))
        self.y = y if y is not None else deref_opt(_const_Float(1.0))
        Sub_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IFunctionfloat,
        'y' : IObservablefloat
    }
    
    
    
    
    
    def on_y_set(self, value):
        from marketsim import event
        event.subscribe_field(self, 'y', value)
    
    def __repr__(self):
        return "({%(x)s}-{%(y)s})" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.bind_ex(self.__dict__['_ctx_ex'])
                else:
                    v.bind_ex(self.__dict__['_ctx_ex'])
        self.x.bind_ex(self._ctx_ex)
        self.y.bind_ex(self._ctx_ex)
        self.bind_impl(self.__dict__['_ctx_ex'])
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.reset_ex(generation)
                else:
                    v.reset_ex(generation)
        self.x.reset_ex(generation)
        self.y.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def typecheck(self):
        from marketsim import rtti
        from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
        from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
        rtti.typecheck(IFunctionfloat, self.x)
        rtti.typecheck(IObservablefloat, self.y)
    
    def registerIn(self, registry):
        if self.__dict__.get('_id', False): return
        self.__dict__['_id'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        registry.insert(self)
        self.x.registerIn(registry)
        self.y.registerIn(registry)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.registerIn(registry)
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.registerIn(registry)
                else:
                    v.registerIn(registry)
        self.__dict__['_processing_ex'] = False
    
    def bind_impl(self, ctx):
        Sub_Impl.bind_impl(self, ctx)
    
    def reset(self):
        Sub_Impl.reset(self)
    
# generated with class generator.python.intrinsic_observable$Import
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
from marketsim.gen._intrinsic.ops import Sub_Impl
@registry.expose(["Ops", "Sub"])
class Sub_IObservableFloatFloat(Observablefloat,Sub_Impl):
    """ 
    """ 
    def __init__(self, x = None, y = None):
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim.gen._out._const import const_Float as _const_Float
        from marketsim import deref_opt
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        Observablefloat.__init__(self)
        self.x = x if x is not None else deref_opt(_const_Float(1.0))
        self.y = y if y is not None else deref_opt(_constant_Float(1.0))
        Sub_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IObservablefloat,
        'y' : IFunctionfloat
    }
    
    
    def on_x_set(self, value):
        from marketsim import event
        event.subscribe_field(self, 'x', value)
    
    
    
    
    def __repr__(self):
        return "({%(x)s}-{%(y)s})" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.bind_ex(self.__dict__['_ctx_ex'])
                else:
                    v.bind_ex(self.__dict__['_ctx_ex'])
        self.x.bind_ex(self._ctx_ex)
        self.y.bind_ex(self._ctx_ex)
        self.bind_impl(self.__dict__['_ctx_ex'])
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.reset_ex(generation)
                else:
                    v.reset_ex(generation)
        self.x.reset_ex(generation)
        self.y.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def typecheck(self):
        from marketsim import rtti
        from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
        from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
        rtti.typecheck(IObservablefloat, self.x)
        rtti.typecheck(IFunctionfloat, self.y)
    
    def registerIn(self, registry):
        if self.__dict__.get('_id', False): return
        self.__dict__['_id'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        registry.insert(self)
        self.x.registerIn(registry)
        self.y.registerIn(registry)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.registerIn(registry)
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.registerIn(registry)
                else:
                    v.registerIn(registry)
        self.__dict__['_processing_ex'] = False
    
    def bind_impl(self, ctx):
        Sub_Impl.bind_impl(self, ctx)
    
    def reset(self):
        Sub_Impl.reset(self)
    
# generated with class generator.python.intrinsic_observable$Import
from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
from marketsim.gen._intrinsic.ops import Sub_Impl
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
@registry.expose(["Ops", "Sub"])
class Sub_FloatFloat(Observablefloat,Sub_Impl):
    """ 
    """ 
    def __init__(self, x = None, y = None):
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        from marketsim import deref_opt
        Observablefloat.__init__(self)
        self.x = x if x is not None else deref_opt(_constant_Float(1.0))
        self.y = y if y is not None else deref_opt(_constant_Float(1.0))
        Sub_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IFunctionfloat,
        'y' : IFunctionfloat
    }
    
    
    
    
    
    
    def __repr__(self):
        return "({%(x)s}-{%(y)s})" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        self.__dict__['_ctx_ex'] = ctx.updatedFrom(self)
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.bind_ex(self.__dict__['_ctx_ex'])
                else:
                    v.bind_ex(self.__dict__['_ctx_ex'])
        self.x.bind_ex(self._ctx_ex)
        self.y.bind_ex(self._ctx_ex)
        self.bind_impl(self.__dict__['_ctx_ex'])
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.reset_ex(generation)
                else:
                    v.reset_ex(generation)
        self.x.reset_ex(generation)
        self.y.reset_ex(generation)
        self.reset()
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def typecheck(self):
        from marketsim import rtti
        from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
        rtti.typecheck(IFunctionfloat, self.x)
        rtti.typecheck(IFunctionfloat, self.y)
    
    def registerIn(self, registry):
        if self.__dict__.get('_id', False): return
        self.__dict__['_id'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        registry.insert(self)
        self.x.registerIn(registry)
        self.y.registerIn(registry)
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.registerIn(registry)
        if hasattr(self, '_internals'):
            for t in self._internals:
                v = getattr(self, t)
                if type(v) in [list, set]:
                    for w in v: w.registerIn(registry)
                else:
                    v.registerIn(registry)
        self.__dict__['_processing_ex'] = False
    
    def bind_impl(self, ctx):
        Sub_Impl.bind_impl(self, ctx)
    
    def reset(self):
        Sub_Impl.reset(self)
    
def Sub(x = None,y = None): 
    from marketsim.gen._out._iobservable._iobservablefloat import IObservablefloat
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, IObservablefloat):
        if y is None or rtti.can_be_casted(y, IObservablefloat):
            return Sub_IObservableFloatIObservableFloat(x,y)
    if x is None or rtti.can_be_casted(x, IFunctionfloat):
        if y is None or rtti.can_be_casted(y, IObservablefloat):
            return Sub_FloatIObservableFloat(x,y)
    if x is None or rtti.can_be_casted(x, IObservablefloat):
        if y is None or rtti.can_be_casted(y, IFunctionfloat):
            return Sub_IObservableFloatFloat(x,y)
    if x is None or rtti.can_be_casted(x, IFunctionfloat):
        if y is None or rtti.can_be_casted(y, IFunctionfloat):
            return Sub_FloatFloat(x,y)
    raise Exception('Cannot find suitable overload for Sub('+str(x) +':'+ str(type(x))+','+str(y) +':'+ str(type(y))+')')
