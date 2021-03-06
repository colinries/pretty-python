#!usr/bin/env python3
# Example 5-4 from Bioinformatics Programming

from GenBank import GenBankEntry, GenBankFeature


class GenBankParser:
    """Parse a genbank file, return GenBankEntry instance"""

    AttributePrefix = (21 * ' ') + '/'

    def __init__(self):
        self.line = None
        self.src = None

    # Predicates

    def is_at_version(self):
        return self.line and self.line.startswith('VERSION')

    def is_at_features(self):
        return self.line and self.line.startswith('FEATURES')

    def is_at_attribute_start(self):
        return self.line and self.line.startswith(self.AttributePrefix)

    def is_at_feature_start(self):
        return len(self.line) > 5 and self.line[5] != ' '

    def is_at_sequence_start(self):
        return self.line and self.line.startswith('ORIGIN')

    def is_at_sequence_end(self):
        return self.line and self.line.startswith('//')

    # Action Methods

    def parse(self, filename):
        """Parse filename and return GenbankEntry

        Use data file named filename to create and return instance of
        GenBankEntry
        """
        with open(filename) as self.src:
            accession, gid = self.get_ids()
            feature_generator = self.make_feature_generator()
            source = next(feature_generator)
            features = list(feature_generator)
            seq = self.get_sequence()
            return GenBankEntry(accession, gid, source, features, seq)

    # Support Methods

    def read_next_line(self):
        self.line = self.src.readline()

    def get_ids(self):
        """Return the accession and GenInfo IDs"""
        self.read_next_line()
        while not self.is_at_version():
            self.read_next_line()
        parts = self.line.split()
        giparts = parts[2].partition()
        return parts[1], giparts[2]

    def skip_intro(self):
        """Skip text that appears in self.src before the first feature"""
        self.read_next_line()
        while not self.is_at_features():
            self.read_next_line()

    def get_sequence(self):
        """Return sequence at the end of the file"""
        seq = ''
        self.read_next_line()
        while not self.is_at_sequence_end():
            seq += self.line[10:-1].replace(' ', '')
            self.read_next_line()
        return seq

    def make_feature_generator(self):
        """Return a generator that produces instances of GenBankFeature

        Return a generator that produces instances of GenBankFeature using the
        data found in the features section of the file
        """
        self.skip_intro()
        while not self.is_at_sequence_start():
            yield self.read_feature()

    def read_feature(self):
        """Return instance of GenBankFeature for a single feature

        Return an instance of GenBankFeature created from the data in the file
        for a single feature
        """
        feature_type, feature_locus = self.line.split()
        self.read_next_line()
        return GenBankFeature(feature_type, feature_locus,
                              self.read_qualifiers()
                              )

    def read_qualifiers(self):
        qualifiers = {}
        while not self.is_at_feature_start():
            parts = self.line.strip()[1:].split('=')
            key = parts[0]
            value = '' if len(parts) < 2 else parts[1]
            if value and value[0] == '"':
                value = value[1:]
            qualifiers[key] = self.read_qualifier_value(value)
        return  qualifiers

    def read_qualifier_value(self, value):
        """Return value of the qualifier"""
        self.read_next_line()
        while (not self.is_at_attribute_start() and
               not self.is_at_feature_start()):
            value += self.line.strip()
            self.read_next_line()
        if value and value[-1] == '"':
            value = value[:-1]
        return value
