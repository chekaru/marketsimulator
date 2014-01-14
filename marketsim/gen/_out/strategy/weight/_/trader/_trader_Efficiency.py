from marketsim import registry
from marketsim import IFunction
from marketsim import IAccount
from marketsim import IFunction
@registry.expose(["Strategy", "trader_Efficiency"])
class trader_Efficiency(IFunction[IFunction[float], IAccount]):
    """ 
    """ 
    def __init__(self):
        pass
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        
    }
    def __repr__(self):
        return "trader_Efficiency" % self.__dict__
    
    def __call__(self, trader = None):
        from marketsim.gen._out.observable.trader._SingleProxy import SingleProxy as _observable_trader_SingleProxy
        from marketsim.gen._out.strategy.weight._Efficiency import Efficiency
        trader = trader if trader is not None else _observable_trader_SingleProxy()
        
        return Efficiency(trader)
    