def StopLoss(proto = None,maxloss = None): 
    from marketsim.gen._out._ifunction._ifunctionifunctioniobservableiorder_from_ifunctionfloat_from_ifunctionfloat import IFunctionIFunctionIObservableIOrder_from_IFunctionfloat_from_IFunctionfloat
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim.gen._out.order._curried._volume_price_stoploss import volume_price_StopLoss_FloatFloatIObservableIOrderFloat as _order__curried_volume_price_StopLoss_FloatFloatIObservableIOrderFloat
    from marketsim import rtti
    if proto is None or rtti.can_be_casted(proto, IFunctionIFunctionIObservableIOrder_from_IFunctionfloat_from_IFunctionfloat):
        if maxloss is None or rtti.can_be_casted(maxloss, IFunctionfloat):
            return _order__curried_volume_price_StopLoss_FloatFloatIObservableIOrderFloat(proto,maxloss)
    raise Exception('Cannot find suitable overload for StopLoss('+str(proto) +':'+ str(type(proto))+','+str(maxloss) +':'+ str(type(maxloss))+')')
