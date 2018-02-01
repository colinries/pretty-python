#!usr/bin/env python3
# Example 5-1 from Bioinformatics Programming


class GenBankEntry:

    # Fundamental Methods

    def __init__(self):
        pass

    def __repr__(self):
        pass

    def __str__(self):
        pass

    # Predicates

    def __lt__(self, other):
        pass

    def is_base_sequence(self):
        """Predicate method; a boolean valued method

        Predicate method; a boolean valued method. Usually starts with 'is_' or
        'has_'
        """
        return set(self.get_sequence().lower()) <= {'a', 'c', 't', 'g'}

    # Access Methods

    def organism(self):
        return self.source[2].get('organism', None)

    def chromosome(self):
        return self.source[2].get('chromosome', None)

    def get_gi(self):
        return self.info['gi']

    def get_accession(self):
        return self.info['accession']

    def gc_content(self):
        return round((100 * ((self.sequence.count('g') +
                              self.sequence.count('c'))) / len(self.sequence)),
                     2)

    # Modification Methods

    # Action Methods

    # Support Methods


def test():
    pass


if __name__ == '__main__':
    test()


gb = GenBankEntry()

