#    @on_trait_change('low', 'high', 'step')
    def _update_outputs(self):
        """ Update outputs based on changes in low, high and step
            Different scenarios to be dealt with:
            1. low < high, step > 0: should return [low, low+step, ..., high]
            2. low < high, step < 0: should return [high, high+step, ..., low]
            3. low = high, step = Any: should return [low]
            4. low > high, step < 0: should return [low, low+step, ..., high]
            5. low > high, step > 0: should return [high, high+step, ..., low]
            6. low != high, step = 0: should return [input_value]
        """
        if self.step == 0:
            if self.high == self.low:
                self.output_list = [self.low]
            else:
                self.output_list = [self.input_value]
        else:
            low, high, step = self.low, self.high, self.step
            # Set the values for calculating range correctly.
            if (low < high and step < 0) or (low > high and step > 0):
                low, high = high, low
            if low != high:
                if isinstance(self.input_value, int):
                    self.output_list = range(low, high, step)
                else:
                    self.output_list = (numpy.arange(low, high, step)).tolist()
                # Add the extremum value if not included.
                if self.output_list[-1] != high:
                    self.output_list.append(high)
            else:
                self.output_list = [low]
        return
