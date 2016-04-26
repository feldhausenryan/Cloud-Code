# Given a default value passed by a type library, return a string with
# an appropriate repr() for the type.
# Takes a raw ELEMDESC and returns a repr string, or None
# (NOTE: The string itself may be '"None"', which is valid, and different to None.
# XXX - To do: Dates are probably screwed, but can they come in?
def MakeDefaultArgRepr(defArgVal):
  try:
    inOut = defArgVal[1]
  except IndexError:
    # something strange - assume is in param.
    inOut = pythoncom.PARAMFLAG_FIN
  if inOut & pythoncom.PARAMFLAG_FHASDEFAULT:
    # times need special handling...
    val = defArgVal[2]
    if isinstance(val, datetime.datetime):
      # VARIANT <-> SYSTEMTIME conversions always lose any sub-second
      # resolution, so just use a 'timetuple' here.
      return repr(tuple(val.utctimetuple()))
    if type(val) is TimeType:
      # must be the 'old' pywintypes time object...
      year=val.year; month=val.month; day=val.day; hour=val.hour; minute=val.minute; second=val.second; msec=val.msec
      return "pywintypes.Time((%(year)d, %(month)d, %(day)d, %(hour)d, %(minute)d, %(second)d,0,0,0,%(msec)d))" % locals()
    return repr(val)
  return None
