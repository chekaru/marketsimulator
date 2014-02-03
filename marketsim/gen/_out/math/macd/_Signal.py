from marketsim import registry
from marketsim import float
from marketsim.ops._function import Function
from marketsim import IObservable
from marketsim import float
from marketsim import float
from marketsim import float
from marketsim import float
from marketsim import float
from marketsim import context
@registry.expose(["MACD", "Signal"])
class Signal(Function[float]):
    """ 
    """ 
    def __init__(self, x = None, slow = None, fast = None, timeframe = None, step = None):
        from marketsim.gen._out._const import const as _const
        from marketsim import rtti
        self.x = x if x is not None else _const()
        self.slow = slow if slow is not None else 26.0
        self.fast = fast if fast is not None else 12.0
        self.timeframe = timeframe if timeframe is not None else 9.0
        self.step = step if step is not None else 1.0
        rtti.check_fields(self)
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : IObservable[float],
        'slow' : float,
        'fast' : float,
        'timeframe' : float,
        'step' : float
    }
    def __repr__(self):
        return "Signal^{%(timeframe)s}_{%(step)s}(MACD_{%(fast)s}^{%(slow)s}(%(x)s))" % self.__dict__
    
    _internals = ['impl']
    def getImpl(self):
        from marketsim.gen._out.math.EW._Avg import Avg as _math_EW_Avg
        from marketsim.gen._out.observable._OnEveryDt import OnEveryDt as _observable_OnEveryDt
        from marketsim.gen._out.math.macd._MACD import MACD as _math_macd_MACD
        return _math_EW_Avg(_observable_OnEveryDt(self.step,_math_macd_MACD(self.x,self.slow,self.fast)),(2/((self.timeframe+1))))
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    
