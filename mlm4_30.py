#!usr/bin/env python3
# Example 4-30 from Bioinformatics Programming


def get_items_from_file(filename, testfn=None):
    """Return all the items in the file named filename

    Return all the items in the file named filename; if testfn then include
    only those items for which testfn is true

    Args:
        filename: The uri for the source FASTA file
        testfn (optional): Only items for which testfn is true are returned.
            Default is None.

    Returns:
        list: A list of FASTA entries in filename

    Raises:
        # TODO: FIll in possible errors that can be raised
    """
    with open(filename) as file:
        return get_items(file, testfn)


def find_item_in_file(filename, testfn=None):
    """Returns the first item in the file named filename

    Returns the first item in the file named filename; if testfn then return
    the first item for which testfn is true.

    Args:
        filename: The uri for the source FASTA file
        testfn (optional): Only items for which testfn is true are returned.
            Default is None.

    Returns:
        list: A FASTA entry in filename

    Raises:
        # TODO: FIll in possible errors that can be raised
    """
    with open(filename) as file:
        return find_item(file, testfn)


def find_item(src, testfn):
    """Return the first item in src

    Return the first item in src; if testfn then return the first item for
    which testfn is true

    Args:
        src: The file object of a FASTA file
        testfn (optional): Only items for which testfn is true are returned.
            Default is None.

    Returns:
        str: A FASTA entry
    """
    gen = item_generator(src)
    item = next(gen)

    if not testfn:
        return item
    else:
        try:
            while not testfn(item):
                item = next(gen)
            return item
        except StopIteration:
            return None


def get_items(src, testfn=None):
    """Return all the items in src;

    Return all the items in src; if testfn then include only those items for
    which testfn is true
    """
    return [item for item in item_generator(src) if not testfn or testfn(item)]


def item_generator(src):
    """Return a generator that produces FASTA sequences from src

    Return a generator that produces a FASTA sequence from src each time its
    called
    """
    skip_intro(src)

    seq = ''
    description = src.readline().split('|')
    line = src.readline()

    while line:
        while line and line[0] != '>':
            seq += line
            line = src.readline()
        yield (description, seq)
        seq = ''
        description = src.readline().split('|')
        line = src.readline()


def skip_intro(src):
    pass


def test():
    pass


if __name__ == '__main__':
    test()

