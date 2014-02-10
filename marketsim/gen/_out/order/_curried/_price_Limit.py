from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import Side
from marketsim import registry
from marketsim import float
@registry.expose(["Order", "Limit"])
class Limit_SideIFunctionFloatIFunctionFloat(IFunction[IOrderGenerator, IFunction[float]]):
    """ 
      Limit orders ask to buy or sell some asset at price better than some limit price.
      If a limit order is not competely fulfilled
      it remains in an order book waiting to be matched with another order.
    """ 
    def __init__(self, side = None, volume = None):
        from marketsim.gen._out.side._sell import Sell as _side_Sell
        from marketsim.gen._out._constant import constant as _constant
        from marketsim import rtti
        self.side = side if side is not None else _side_Sell()
        self.volume = volume if volume is not None else _constant(1.0)
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'side' : IFunction[Side],
        'volume' : IFunction[float]
    }
    def __repr__(self):
        return "Limit(%(side)s, %(volume)s)" % self.__dict__
    
    def __call__(self, price = None):
        from marketsim.gen._out._constant import constant as _constant
        from marketsim.gen._out.order._limit import Limit
        price = price if price is not None else _constant(100.0)
        side = self.side
        volume = self.volume
        return Limit(side, price, volume)
    
def price_Limit(side = None,volume = None): 
    from marketsim import Side
    from marketsim import IFunction
    from marketsim import float
    from marketsim import rtti
    if side is None or rtti.can_be_casted(side, IFunction[Side]):
        if volume is None or rtti.can_be_casted(volume, IFunction[float]):
            return Limit_SideIFunctionFloatIFunctionFloat(side,volume)
    raise Exception("Cannot find suitable overload")
