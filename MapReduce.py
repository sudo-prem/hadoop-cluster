from mrjob.job import MRJob

class IrisMR(MRJob):
    def mapper(self, _, line):
      _, month, _, _, temperature = line.split()
      
      yield (month, (temperature, 1))
      
    def _reducer_combiner(self, month, temperatures):
      avg, count = 0, 0
      for tmp, c in temperatures
        avg = (avg * count + tmp * c) / (count + c)
        count += c
      return (month, (avg, count))
      
    def combiner(self, month, temperatures):
      yield self._reducer_combiner(month, temperatures)
      
    def reducer(self, month, temperatures):
      month, (avg, count) = self._reducer_combiner(month, temperatures)
      
      # (May, 28 Degrees)
      yield (month, avg)

if __name__ == '__main__':
     IrisMR.run()
