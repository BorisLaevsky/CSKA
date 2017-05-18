class Deck:

    def __init__(self):
        self.deck = []

    def add_first(self, element):
        self.deck.insert(0,element)

    def add_last(self, element):
        self.deck.append(element)

    def remove_last(self):
        try:
            last = self.deck[-1]
            self.deck = self.deck[:-1]
            return last
        except IndexError:
            raise IndexError('empty deck')

    def remove_first(self):
        try:
            first = self.deck[0]
            self.deck = self.deck[1:]
            return first
        except IndexError:
            raise IndexError('empty deck')

    def peak_last(self):
        try:
            return self.deck[-1]
        except IndexError:
            raise IndexError('empty deck')

    def peak_first(self):
        try:
            return self.deck[0]
        except IndexError:
            raise IndexError('empty deck')

    def __str__(self):
        return str(self.deck)

    def __iter__(self):
        return self

    def next(self):
        if len(self.deck) == 0:
            raise StopIteration
        return self.remove_first()

d = Deck()
d.add_first(1)
d.add_first(2)
d.add_last(3)
print d
for x in d:
    print x
print d
a = Deck()
a.peak_last()
