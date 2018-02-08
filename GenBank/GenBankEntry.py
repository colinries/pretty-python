#!usr/bin/env python3
# Example 5-1 from Bioinformatics Programming


class GenBankEntry:
    """Store and represent a GenBank entry"""

    Instances = {}

    # Class Methods

    @classmethod
    def InstanceCount(cls):
        return len(cls.Instances)

    @classmethod
    def GetInstances(cls):
        return (value for value in cls.Instances.keys())

    @classmethod
    def Get(cls, target):
        """Return the instance whose GID is target"""
        return cls.Instances.get(target,None)

    # Fundamental Methods

    def __init__(self, accession,  gid, source, sequence, features):
        self.accession = accession
        self.gid = gid
        self.sequence = sequence
        self.features = features
        self.source = source
        self.Instances[self.gid] = self

    def __repr__(self):
        return 'GenBankEntry-' + self.get_gid()

    def __str__(self):
        return "<GenBankEntry {} {} '{}'>".format(self.get_gid(),
                                                  self.get_accession(),
                                                  self.organism()
                                                  )

    #  Predicates

    def __lt__(self, other):
        if type(self) != type(other):
            raise Exception('Incompatible argument to __lt__: ' + str(other))
        return self.get_gid() < other.get_gid()

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

    def get_accession(self):
        return self.accession

    def get_gid(self):
        return self.gid

    def get_sequence(self):
        return self.sequence

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


