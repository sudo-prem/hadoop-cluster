from mrjob.job import MRJob
from mrjob.step import MRStep

class IrisBreakdown(MRJob):
    def mapper(self, _, line):
        (s_length, s_width, p_length, p_width, category) = line.split(',')
        yield (category, (s_length, 1))

    def iris_reducer(self, category, values):
        average = 0
        count = 0
        for v, c in values:
            average = (average * count + v * c) / (count + c)
            count += c
        yield (category, (average, count))

    def combiner(self, category, values):
        yield self.iris_reducer(category, values)

    def reducer(self, category, values):
        cateogory, (average, count) = self.iris_reducer(category, values)
        yield (category, average)

if __name__ == '__main__':
    IrisBreakdown.run()
