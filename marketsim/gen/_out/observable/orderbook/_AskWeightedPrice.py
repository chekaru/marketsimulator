from marketsim import registry
from marketsim import float
from marketsim.ops._all import Observable
from marketsim import IOrderBook
from marketsim import float
from marketsim import context
@registry.expose(["Orderbook", "AskWeightedPrice"])
class AskWeightedPrice(Observable[float]):
    """ 
    """ 
    def __init__(self, book = None, alpha = None):
        from marketsim import float
        from marketsim.ops._all import Observable
        from marketsim.gen._out.observable.orderbook._OfTrader import OfTrader
        from marketsim import _
        from marketsim import event
        Observable[float].__init__(self)
        self.book = book if book is not None else OfTrader()
        self.alpha = alpha if alpha is not None else 0.015
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'book' : IOrderBook,
        'alpha' : float
    }
    def __repr__(self):
        return "Ask_{%(alpha)s}^{%(book)s}" % self.__dict__
    
    _internals = ['impl']
    @property
    def attributes(self):
        return {}
    
    def getImpl(self):
        from marketsim.gen._out.observable.orderbook._WeightedPrice import WeightedPrice
        from marketsim.gen._out.observable.orderbook._Asks import Asks
        return WeightedPrice(Asks(self.book),self.alpha)
        
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    
