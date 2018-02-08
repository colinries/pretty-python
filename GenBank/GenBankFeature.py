#!usr/bin/env python3
# Example 5-2 from Bioinformatics Programming


class GenBankFeature:

    FeatureNameOrder = ('gene', 'promoter', 'RBS', 'CDS')

    # Fundamental Methods

    def __init__(self, feature_type, locus, qualifiers):
        self.type = feature_type
        self.locus = locus
        self.qualifiers = qualifiers

    def __repr__(self):
        return ('GenBankFeature' +
               repr((self.type, self.locus, self.qualifiers)))

    def __str__(self):
        return self.type + '@' + self.locus

    # Predicates

    def __lt__(self, other):
        if type(self) != type(other):
            raise Exception('Incompatible argument to __lt__: ' + str(other))
        return self.locus_lt(other) and self.type_lt(other)

    def is_gene(self):
        return 'gene' == self.get_type()

    def is_cds(self):
        return 'CDS' == self.get_type()

    # Access Methods

    def get_type(self):
        return self.type

    def get_locus(self):
        return self.locus

    def get_qualifier(self, name):
        return self.qualifiers.get(name, None)

    # Private Support Methods

    def locus_lt(self, other):
        """Sort by locus"""
        assert type(self) == type(other)
        return (self.get_locus() or -1) < (self.get_locus() or -1)

    def type_lt(self, other):
        assert type(self) == type(other)
        return (self.FeatureNameOrder.index(self.get_type()) <
                other.FeatureNameOrder.index(self.get_type())
                )

