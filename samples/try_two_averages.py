import sys
sys.path.append(r'..')

from marketsim import (signal, strategy, trader, orderbook, 
                       timeserie, scheduler, observable, veusz, mathutils)

from common import run

const = mathutils.constant

def TwoAverages(ctx):

    ctx.volumeStep = 30
    
    alpha_slow = 0.015
    alpha_fast = 0.15

    slow = lambda: mathutils.ewma(alpha = alpha_slow)
    fast = lambda: mathutils.ewma(alpha = alpha_fast)

    linear_signal = signal.RandomWalk(initialValue=200, 
                                      deltaDistr=const(-1), 
                                      label="200-t")
    
    demo = ctx.addGraph('demo')
    myVolume = lambda: [(observable.VolumeTraded(), demo)]
    myAverage = lambda alpha: [(observable.avg(observable.Price(orderbook.OfTrader()), alpha), demo)]
    
    return [
        ctx.makeTrader_A(strategy.LiquidityProvider(volumeDistr=const(10)),
                         "liquidity"),

        ctx.makeTrader_A(strategy.Signal(linear_signal,
                                         volumeDistr=const(3)), 
                        "signal", 
                        [(linear_signal, ctx.amount_graph)]),
            
        ctx.makeTrader_A(strategy.TwoAverages(average1 = slow(), 
                                              average2 = fast()), 
                        'avg+', 
                        myAverage(alpha_slow) + myAverage(alpha_fast) + myVolume()),

        ctx.makeTrader_A(strategy.TwoAverages(average1 = fast(), 
                                              average2 = slow()), 
                         'avg-',
                         myVolume()),

        ctx.makeTrader_A(strategy.TwoAveragesEx(average1 = slow(), 
                                                average2 = fast()), 
                         'avg_ex+',
                         myVolume()),

        ctx.makeTrader_A(strategy.TwoAveragesEx(average1 = fast(), 
                                                average2 = slow()), 
                         'avg_ex-',
                         myVolume())
    ]

if __name__ == '__main__':
    run("two_averages", TwoAverages)