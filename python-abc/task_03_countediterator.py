#!/usr/bin/env python3


class CountedIterator:
    def __init__(self, iterator):
        self.iterator = iter(iterator)
        self.counted_iter = 0

    def get_count(self):
        return self.counted_iter

    def __next__(self):
        item = next(self.iterator)
        self.counted_iter += 1
        return item
