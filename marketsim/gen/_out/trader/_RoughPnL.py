from marketsim.ops._all import Observable
from marketsim import IAccount
from marketsim import registry
from marketsim import context
from marketsim import float
@registry.expose(["Trader", "RoughPnL"])
class RoughPnL_IAccount(Observable[float]):
    """   It takes into account only the best price of the order queue
    """ 
    def __init__(self, trader = None):
        from marketsim.ops._all import Observable
        from marketsim import _
        from marketsim import rtti
        from marketsim import event
        from marketsim import float
        from marketsim.gen._out.trader._singleproxy import SingleProxy as _trader_SingleProxy
        Observable[float].__init__(self)
        self.trader = trader if trader is not None else _trader_SingleProxy()
        rtti.check_fields(self)
        self.impl = self.getImpl()
        event.subscribe(self.impl, _(self).fire, self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'trader' : IAccount
    }
    def __repr__(self):
        return "RoughPnL(%(trader)s)" % self.__dict__
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    _internals = ['impl']
    def __call__(self, *args, **kwargs):
        return self.impl()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def getImpl(self):
        from marketsim.gen._out.orderbook._naivecumulativeprice import NaiveCumulativePrice as _orderbook_NaiveCumulativePrice
        from marketsim.gen._out.observable._float import Float as _observable_Float
        from marketsim.gen._out.ops._add import Add as _ops_Add
        from marketsim.gen._out.orderbook._oftrader import OfTrader as _orderbook_OfTrader
        from marketsim.gen._out.trader._position import Position as _trader_Position
        from marketsim.gen._out.trader._balance import Balance as _trader_Balance
        return _observable_Float(_ops_Add(_trader_Balance(self.trader),_orderbook_NaiveCumulativePrice(_orderbook_OfTrader(self.trader),_trader_Position(self.trader))))
    
def RoughPnL(trader = None): 
    from marketsim import IAccount
    from marketsim import rtti
    if trader is None or rtti.can_be_casted(trader, IAccount):
        return RoughPnL_IAccount(trader)
    raise Exception("Cannot find suitable overload")
