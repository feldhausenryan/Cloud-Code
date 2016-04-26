# Define the 'VirtualValue' property:
def _get_virtual_data ( self, name ):
    return self.data_name.items[
               self.trait( name ).index ].data_name_item_choice.choice_value
