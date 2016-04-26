# Given an enum, write all aliases for it.
# (no longer necessary for new style code, but still used for old code.
def WriteAliasesForItem(item, aliasItems, stream):
  for alias in aliasItems.itervalues():
    if item.doc and alias.aliasDoc and (alias.aliasDoc[0]==item.doc[0]):
      alias.WriteAliasItem(aliasItems, stream)
