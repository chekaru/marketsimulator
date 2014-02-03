from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import Order
from marketsim.ops._all import Observable
from marketsim import Side
from marketsim import IFunction
from marketsim import IFunction
from marketsim import float
@registry.expose(["Order", "FixedBudget"])
class FixedBudget(IOrderGenerator, Observable[Order]):
    """ 
      Fixed budget order acts like a market order
      but the volume is implicitly given by a budget available for trades.
      Internally first it sends request.EvalVolumesForBudget
      to estimate volumes and prices of orders to sent and
      then sends a sequence of order.ImmediateOrCancel to be sure that
      cumulative price of trades to be done won't exceed the given budget.
    """ 
    def __init__(self, side = None, budget = None):
        from marketsim import Order
        from marketsim.ops._all import Observable
        from marketsim.gen._out.side._Sell import Sell as _side_Sell
        from marketsim import event
        from marketsim import types
        from marketsim.gen._out._constant import constant as _constant
        from marketsim import event
        from marketsim import types
        from marketsim import rtti
        Observable[Order].__init__(self)
        self.side = side if side is not None else _side_Sell()
        if isinstance(side, types.IEvent):
            event.subscribe(self.side, self.fire, self)
        self.budget = budget if budget is not None else _constant(1000.0)
        if isinstance(budget, types.IEvent):
            event.subscribe(self.budget, self.fire, self)
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'side' : IFunction[Side],
        'budget' : IFunction[float]
    }
    def __repr__(self):
        return "FixedBudget(%(side)s, %(budget)s)" % self.__dict__
    
    def __call__(self, *args, **kwargs):
        from marketsim.gen._intrinsic.order.meta.fixed_budget import Order_Impl
        side = self.side()
        if side is None: return None
        
        budget = self.budget()
        if budget is None: return None
        
        return Order_Impl(side, budget)
    
