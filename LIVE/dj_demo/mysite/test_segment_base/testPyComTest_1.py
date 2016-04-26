# Test everything which can be tested using both the "dynamic" and "generated"
# COM objects (or when there are very subtle differences)
def TestCommon(o, is_generated):
    progress("Getting counter")
    counter = o.GetSimpleCounter()
    TestCounter(counter, is_generated)
    progress("Checking default args")
    rc = o.TestOptionals()
    if  rc[:-1] != ("def", 0, 1) or abs(rc[-1]-3.14)>.01:
        print rc
        raise error("Did not get the optional values correctly")
    rc = o.TestOptionals("Hi", 2, 3, 1.1)
    if  rc[:-1] != ("Hi", 2, 3) or abs(rc[-1]-1.1)>.01:
        print rc
        raise error("Did not get the specified optional values correctly")
    rc = o.TestOptionals2(0)
    if  rc != (0, "", 1):
        print rc
        raise error("Did not get the optional2 values correctly")
    rc = o.TestOptionals2(1.1, "Hi", 2)
    if  rc[1:] != ("Hi", 2) or abs(rc[0]-1.1)>.01:
        print rc
        raise error("Did not get the specified optional2 values correctly")
    progress("Checking getting/passing IUnknown")
    check_get_set(o.GetSetUnknown, o)
    progress("Checking getting/passing IDispatch")
    if not isinstance(o.GetSetDispatch(o), o.__class__):
        raise error("GetSetDispatch failed: %r" % (o.GetSetDispatch(o),))
    progress("Checking getting/passing IDispatch of known type")
    if o.GetSetInterface(o).__class__ != o.__class__:
        raise error("GetSetDispatch failed")
    progress("Checking misc args")
    check_get_set(o.GetSetVariant, 4)
    check_get_set(o.GetSetVariant, "foo")
    check_get_set(o.GetSetVariant, o)
    # signed/unsigned.
    check_get_set(o.GetSetInt, 0)
    check_get_set(o.GetSetInt, -1)
    check_get_set(o.GetSetInt, 1)
    check_get_set(o.GetSetUnsignedInt, 0)
    check_get_set(o.GetSetUnsignedInt, 1)
    check_get_set(o.GetSetUnsignedInt, 0x80000000)
    if o.GetSetUnsignedInt(-1) != 0xFFFFFFFF:
    # -1 is a special case - we accept a negative int (silently converting to
    # unsigned) but when getting it back we convert it to a long.
        raise error("unsigned -1 failed")
    check_get_set(o.GetSetLong, 0)
    check_get_set(o.GetSetLong, -1)
    check_get_set(o.GetSetLong, 1)
    check_get_set(o.GetSetUnsignedLong, 0)
    check_get_set(o.GetSetUnsignedLong, 1)
    check_get_set(o.GetSetUnsignedLong, 0x80000000)
    # -1 is a special case - see above.
    if o.GetSetUnsignedLong(-1) != 0xFFFFFFFF:
        raise error("unsigned -1 failed")
    # We want to explicitly test > 32 bits.  py3k has no 'maxint' and
    # 'maxsize+1' is no good on 64bit platforms as its 65 bits!
    big = 2147483647 # sys.maxint on py2k
    for l in big, big+1, 1 << 65:
        check_get_set(o.GetSetVariant, l)
    progress("Checking structs")
    r = o.GetStruct()
    assert r.int_value == 99 and str(r.str_value)=="Hello from C++"
    assert o.DoubleString("foo") == "foofoo"
    progress("Checking var args")
    o.SetVarArgs("Hi", "There", "From", "Python", 1)
    if o.GetLastVarArgs() != ("Hi", "There", "From", "Python", 1):
        raise error("VarArgs failed -" + str(o.GetLastVarArgs()))
    progress("Checking arrays")
    l=[]
    TestApplyResult(o.SetVariantSafeArray, (l,), len(l))
    l=[1,2,3,4]
    TestApplyResult(o.SetVariantSafeArray, (l,), len(l))
    TestApplyResult(o.CheckVariantSafeArray, ((1,2,3,4,),), 1)
    # and binary
    TestApplyResult(o.SetBinSafeArray, (str2memory('foo\0bar'),), 7)
    progress("Checking properties")
    o.LongProp = 3
    if o.LongProp != 3 or o.IntProp != 3:
        raise error("Property value wrong - got %d/%d" % (o.LongProp,o.IntProp))
    o.LongProp = o.IntProp = -3
    if o.LongProp != -3 or o.IntProp != -3:
        raise error("Property value wrong - got %d/%d" % (o.LongProp,o.IntProp))
    # This number fits in an unsigned long.  Attempting to set it to a normal
    # long will involve overflow, which is to be expected. But we do
    # expect it to work in a property explicitly a VT_UI4.
    check = 3 *10 **9
    o.ULongProp = check
    if o.ULongProp != check:
        raise error("Property value wrong - got %d (expected %d)" % (o.ULongProp, check))
    TestApplyResult(o.Test, ("Unused", 99), 1) # A bool function
    TestApplyResult(o.Test, ("Unused", -1), 1) # A bool function
    TestApplyResult(o.Test, ("Unused", 1==1), 1) # A bool function
    TestApplyResult(o.Test, ("Unused", 0), 0)
    TestApplyResult(o.Test, ("Unused", 1==0), 0)
    assert o.DoubleString("foo") == "foofoo"
    TestConstant("ULongTest1", ensure_long(0xFFFFFFFF))
    TestConstant("ULongTest2", ensure_long(0x7FFFFFFF))
    TestConstant("LongTest1", ensure_long(-0x7FFFFFFF))
    TestConstant("LongTest2", ensure_long(0x7FFFFFFF))
    TestConstant("UCharTest", 255)
    TestConstant("CharTest", -1)
    # 'Hello Loraine', but the 'r' is the "Registered" sign (\xae)
    TestConstant("StringTest", u"Hello Lo\xaeaine") 
    progress("Checking dates and times")
    if issubclass(pywintypes.TimeType, datetime.datetime):
        # For now *all* times passed must be tz-aware.
        now = win32timezone.now()
        # but conversion to and from a VARIANT loses sub-second...
        now = now.replace(microsecond=0)
        later = now + datetime.timedelta(seconds=1)
        TestApplyResult(o.EarliestDate, (now, later), now)
    else:
        # old PyTime object
        now = pythoncom.MakeTime(time.gmtime(time.time()))
        later = pythoncom.MakeTime(time.gmtime(time.time()+1))
        TestApplyResult(o.EarliestDate, (now, later), now)
        # But it can still *accept* tz-naive datetime objects...
        now = datetime.datetime.now()
        expect = pythoncom.MakeTime(now)
        TestApplyResult(o.EarliestDate, (now, now), expect)
    progress("Checking currency")
    # currency.
    pythoncom.__future_currency__ = 1
    if o.CurrencyProp != 0:
        raise error("Expecting 0, got %r" % (o.CurrencyProp,))
    for val in ("1234.5678", "1234.56", "1234"):
        o.CurrencyProp = decimal.Decimal(val)
        if o.CurrencyProp != decimal.Decimal(val):
            raise error("%s got %r" % (val, o.CurrencyProp))
    v1 = decimal.Decimal("1234.5678")
    TestApplyResult(o.DoubleCurrency, (v1,), v1*2)
    v2 = decimal.Decimal("9012.3456")
    TestApplyResult(o.AddCurrencies, (v1, v2), v1+v2)
    TestTrickyTypesWithVariants(o, is_generated)
    progress("Checking win32com.client.VARIANT")
    TestPyVariant(o, is_generated)
