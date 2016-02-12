'''
itemtype(type,subtype1,subtype2)
'''
def itemtype(Type, subtype1 = None, subtype2 = None):
    NewFiltered = []
    global Filtered
    print "Applying Filter : itemtype(%s,%s,%s)" %(Type,subtype1,subtype2)
    print "Initial Count = %i" %(len(Filtered))
    if subtype1 == None and subtype2 == None:
        for item in Filtered:
            if TypeSubtypes[item[u'data_id']][0] == Type:
                NewFiltered.append(item)
    elif subtype1 <> None and subtype2 == None:
        for item in Filtered:
            if TypeSubtypes[item[u'data_id']][0] == Type and TypeSubtypes[item[u'data_id']][1] == subtype1:
                NewFiltered.append(item)
    elif subtype1 == u'Any' and subtype2 <> None:
        for item in Filtered:
            if TypeSubtypes[item[u'data_id']][0] == Type and TypeSubtypes[item[u'data_id']][2] == subtype2:
                NewFiltered.append(item)
    
    elif subtype1 <> None and subtype2 <> None:
        for item in Filtered:
            if TypeSubtypes[item[u'data_id']][0] == Type and TypeSubtypes[item[u'data_id']][1] == subtype1 and TypeSubtypes[item[u'data_id']][2] == subtype2:
                NewFiltered.append(item)
    print "New Count = %i\nNumber Eliminated = %i" %(len(NewFiltered),len(Filtered)-len(NewFiltered))
    Filtered = NewFiltered


                
            
