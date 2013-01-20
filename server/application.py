from flask import Flask, render_template
import sys, json
sys.path.append(r'..')

from marketsim import (strategy, orderbook, trader, order, 
                       scheduler, observable, veusz, mathutils, registry)

const = mathutils.constant

with scheduler.create() as world:
    
    book_A = orderbook.Local(tickSize=0.01, label="A")
    
    price_graph = veusz.Graph("Price")
     
    assetPrice = observable.Price(book_A)
    price_graph.addTimeSerie(assetPrice)
    
    avg = observable.avg
    trend = observable.trend
    
    price_graph.addTimeSerie(avg(assetPrice))
    
    t_A = trader.SASM(book_A, strategy.LiquidityProvider(volumeDistr=const(70.)))
    
    c_200 = const(200.)
    
    fv_200_12 = strategy.FundamentalValue(fundamentalValue=c_200, volumeDistr=const(12))
    
    trader_200 = trader.SASM(book_A, fv_200_12, "t200")
    
    fv_200 = fv_200_12.With(volumeDistr = const(1.))
     
    trader_200_1=trader.SASM(book_A, fv_200, "t200_1")    
    trader_200_2=trader.SASM(book_A, fv_200, "t200_2")
    
    trader_150 = trader.SASM(book_A, 
                             strategy.FundamentalValue(fundamentalValue=const(150.), 
                                                            volumeDistr=const(1.)), 
                             "t150")
    
    meanreversion = trader.SASM(book_A, 
                                strategy.MeanReversion(volumeDistr=const(1.)), 
                                "mr_0_15")
    
    avg_plus = trader.SASM(book_A, 
                           strategy.TwoAverages(average1=mathutils.ewma(0.15),
                                                average2=mathutils.ewma(0.015),
                                                volumeDistr=const(1.)),
                           label="avg+")

    avg_minus= trader.SASM(book_A, 
                           strategy.TwoAverages(average1=mathutils.ewma(0.015),
                                                average2=mathutils.ewma(0.15),
                                                volumeDistr=const(1.)),
                           label="avg-")
    
    v_fv200 = trader.SASM(book_A, 
                          strategy.TradeIfProfitable(fv_200), 
                          "v_fv200")
    def s_fv(fv):
        return strategy.TradeIfProfitable(fv_200.With(fundamentalValue=const(fv)))

    def fv_virtual(fv):
        return trader.SASM(book_A, s_fv(fv), "v"+str(fv))
        
    
    virtual_160 = fv_virtual(160.)
    virtual_170 = fv_virtual(170.)
    virtual_180 = fv_virtual(180.)
    virtual_190 = fv_virtual(190.)
    
    best = trader.SASM(book_A, 
                       strategy.chooseTheBest([s_fv(160.), 
                                               s_fv(170.), 
                                               s_fv(180.), 
                                               s_fv(190.),]), 
                       "best")

    eff_graph = veusz.Graph("efficiency")
    trend_graph = veusz.Graph("efficiency trend")
    pnl_graph = veusz.Graph("P&L")
    volume_graph = veusz.Graph("volume")
    
    def addToGraph(traders):
        for t in traders:
            e = observable.Efficiency(t)
            #eff_graph.addTimeSerie(e)
            #eff_graph.addTimeSerie(InstEfficiency(t))
            eff_graph.addTimeSerie(avg(e))
            trend_graph.addTimeSerie(trend(e))
            #trend_graph.addTimeSerie(trend(InstEfficiency(t)))
            pnl_graph.addTimeSerie(observable.PnL(t))
            volume_graph.addTimeSerie(observable.VolumeTraded(t))
    
    traders = [trader_150, trader_200, trader_200_1, trader_200_2, 
                best, 
#                tf, tf_0_15, tf_0_015, 
                meanreversion, avg_plus, avg_minus, v_fv200,
                virtual_160, virtual_170, virtual_180, virtual_190
               ]
    
    addToGraph(traders)
    
    for t in traders + [t_A]:
        registry.insert(t)
    
    for k,v in registry.dumpall().iteritems():
        print k, v
        
    fv_200 = trader_200.strategies[0]
    
    new = registry.new
    setAttr = registry.setAttr
    
    c = new('marketsim.mathutils.constant', {'value': '50.0'})

    interval = new('marketsim.mathutils.rnd.expovariate', {'Lambda': '+1.0'})
    
    setAttr(fv_200, 'orderFactory', order.Market.T)
    setAttr(fv_200, 'creationIntervalDistr', interval)
    setAttr(avg_plus.strategies[0], 'average1', new('marketsim.mathutils.ewma', {'alpha' : 0.15 }))
    setAttr(virtual_160.strategies[0], 'estimator', strategy.virtualWithUnitVolume)


app = Flask(__name__)

@app.route('/obj/<int:obj_id>')
def get_object(obj_id):
    return json.dumps(registry.instance.tojson(obj_id))

@app.route('/all')
def get_all():
    return json.dumps(registry.instance.tojsonall())

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)