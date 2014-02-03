from marketsim import registry
from marketsim import IOrderGenerator
from marketsim import float
from marketsim import IFunction
from marketsim import IFunction
from marketsim import float
from marketsim import IFunction
from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import IFunction
from marketsim import float
from marketsim import IFunction
from marketsim import float
@registry.expose(["Order", "Peg"])
class volume_price_Peg(IFunction[IFunction[IOrderGenerator,IFunction[float]],IFunction[float]]):
    """ 
      A peg order is a particular case of the floating price order
      with the price better at one tick than the best price of the order queue.
      It implies that if several peg orders are sent to the same order queue
      they start to race until being matched against the counterparty orders.
    """ 
    def __init__(self, proto = None):
        from marketsim.gen._out.order._curried._volume_price_Limit import volume_price_Limit as _order__curried_volume_price_Limit
        from marketsim import rtti
        self.proto = proto if proto is not None else _order__curried_volume_price_Limit()
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IFunction[IFunction[IOrderGenerator, IFunction[float]], IFunction[float]]
    }
    def __repr__(self):
        return "volume_price_Peg(%(proto)s)" % self.__dict__
    
    def __call__(self, volume = None):
        from marketsim.gen._out.order._curried._price_Peg import price_Peg
        proto = self.proto
        return price_Peg(proto(volume))
    
