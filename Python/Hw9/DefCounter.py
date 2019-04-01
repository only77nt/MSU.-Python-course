import collections

class DefCounter(collections.Counter):
    miss = -1
    def __init__(self, *args, **seq):
        size = len(seq)
        #print(size)
        #print(seq)
        if "missing" in seq.keys():
            self.miss = seq.pop("missing")
        else:
            self.miss = -1
        #print(self.miss)
        #print(args)
        if not args:
            collections.Counter.__init__(self, seq)
        else:
            collections.Counter.__init__(self, args[0])
    def __str__(self):
        return super().__str__()
    def __getitem__(self, index):
        if self.__contains__(index):
            item = super().__getitem__(index)
            return item
        else:
            return self.miss


