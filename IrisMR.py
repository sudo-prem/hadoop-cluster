from mrjob.job import MRJob
from mrjob.step import MRStep

choice = "sepal_length"


class IrisMR(MRJob):
    def step(self):
        return [MRStep(mapper=self.mapper, reducer=self.reducer)]

    def mapper(self, _, line):
        (sl, sw, pl, pw, category) = line.split(',')
        if choice == "sepal_length":
            yield (category, (float(sl), 1))
        elif choice == "sepal_width":
            yield (category, (float(sw), 1))
        elif choice == "petal_length":
            yield (category, (float(pl), 1))
        else:
            yield (category, (float(pw), 1))

    def _reducer_combiner(self, category, value_count):
        avg, cnt = 0, 0
        for val, c in value_count:
            avg = (avg * cnt + val * c) / (cnt + c)
            cnt += c
        return (category, (avg, cnt))

    def combiner(self, category, value_count):
        yield self._reducer_combiner(category, value_count)

    def reducer(self, category, value_count):
        category, (avg, count) = self._reducer_combiner(category, value_count)
        yield (category, avg)


if __name__ == '__main__':
    IrisMR.run()
