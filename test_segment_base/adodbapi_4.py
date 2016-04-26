# ------- utilities for converting python data to ADO data
def pyTypeToADOType(d):
    tp=type(d)
    try:
        return typeMap[tp]
    except KeyError:
        if isinstance(d,datetime.datetime):
            return adc.adDBTimeStamp
        if isinstance(d,datetime.time):
            return adc.adDBTime
        if tp in dateconverter.types:
            return adc.adDate
        if isinstance(d,decimal.Decimal):
            return adc.adDecimal
    raise DataError('cannot convert "%s" (type=%s) to ADO'%(repr(d),tp))
