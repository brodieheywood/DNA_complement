# Brodie Heywood
# November 26, 2018

"""DNA Complement"""

import doctest


def complement(dna):
    """Return complementary DNA strand.

    Reads ssDNA and returns complementary basepairs.
    PARAM: dna, string containing only A, C, G, and T characters
    PRECONDITION: dna string must only contain characters A, C, G, and T and should contain at least one character
    POSTCONDITION: creates a new string of base pairs complementary to original dna where A and T are complementary and
    C and G are complementary.
    RETURN: string with equal length to given dna containing only A, C, G, and T characters
    >>> complement('A')
    'T'
    >>> complement('ATCG')
    'TAGC'
    """
    complementary_dna = ''

    for nucleotide in dna:  # cannot elegantly use replace() method (I tried)
        if nucleotide == 'A':
            complementary_dna += 'T'
        elif nucleotide == 'T':
            complementary_dna += 'A'
        elif nucleotide == 'C':
            complementary_dna += 'G'
        elif nucleotide == 'G':
            complementary_dna += 'C'
        else:  # invalid character in dna string
            print('Input DNA contains an invalid character (not a recognized nucleotide). Make sure all characters are '
                  'T, A, G, or C.')
            return

    return complementary_dna


def main():
    dna = 'TTTTTAAAAAAGGGGGGCCCCCC'
    print(complement(dna))


if __name__ == '__main__':
    main()
    doctest.testmod()
