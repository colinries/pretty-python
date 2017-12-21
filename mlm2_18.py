#!/usr/bin/env python3
# Example 2-18 from Bioinformatics Programming (mlm)


# Constants
DNAbases = set("TCAGtcag")
RNAbases = set("UCAGucag")


def validate_base_sequence(base_sequence, RNAflag=False):
    """Return True if valid nucleotide sequence, otherwise False

    Return True if the string base_sequence contains only upper- or lowercase
    T (or U, if RNAflag), C, A, and G characters, otherwise False
    """
    return set(base_sequence) <= (RNAbases if RNAflag else DNAbases)  # from example 3-1

    # or, as in the original example,
    #
    # seq = base_sequence.upper()
    # return len(seq) == (seq.count('U' if RNAflag else 'T') +
    #                     seq.count('C') + seq.count('A') + seq.count('G'))


def gc_content(base_seq, RNAflag=False):  # Added RNAflag optional parameter
    """Return the percentage of bases in base_seq that are C or G"""
    assert validate_base_sequence(base_seq, RNAflag), 'arg has invalid characters'
    seq = base_seq.upper()
    return (seq.count('G') + seq.count('C')) / len(seq)


def recognition_site(base_seq, recognition_seq):
    """Return first position of recognition_seq in base_seq

    Return the first position in base_seq where recognition_seq occurs, or -1
    if not found
    """
    return base_seq.find(recognition_seq)


def test():
    assert validate_base_sequence("ATCG")
    assert validate_base_sequence("")
    assert not validate_base_sequence('ACUG')

    assert validate_base_sequence('ACUG', True)  # In book it's RNAflag=False
    assert not validate_base_sequence('ACUG', False)
    # Line from example omitted

    assert 0.5 == gc_content('ATCG')
    assert 1.0 == gc_content("CCGG")
    assert .25 == gc_content("ACTA")

    assert 4 == recognition_site('GCCTACTA', 'ACT')  # Added to example

    print("All tests passed.")


def arbitrary_function():
    """Perform some arbitrary task"""
    pass


print(gc_content('ttcccgg'))
test()
