# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    """
    assumes sequence is a non-empty string
    returns a list of strings, representing all the permutations of sequence
    note: do not depend on the order of permutations
    e.g >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    """
    # initialize holding variables
    permutations_of_sequence = []
    permutations_of_cutdown_sequence = []

    # define recursive behaviour
    # for sequence of len(n), case is sequence[0] and sequence[1:n]
    if len(sequence) > 1:
        first_char_sequence = sequence[0]
        cutdown_sequence = sequence[1:]

        # find recursions of cutdown_sequence
        if len(cutdown_sequence) > 1:
            permutations_of_cutdown_sequence = get_permutations(sequence[1:])

        # base case
        # add first_char_sequence to all recursions of cutdown_sequence
        for i in range(len(sequence)):
            holding_string = cutdown_sequence[:i] + first_char_sequence + cutdown_sequence[i:]
            permutations_of_sequence += [holding_string]

        # loop over each item in permutations_of_cutdown_sequence
        if len(permutations_of_cutdown_sequence) > 1:
            for ele in range(len(permutations_of_cutdown_sequence)):
                new_cutdown_sequence = permutations_of_cutdown_sequence[ele]
                for i in range(len(sequence)):
                    holding_string = new_cutdown_sequence[:i] + first_char_sequence +\
                        new_cutdown_sequence[i:]
                    permutations_of_sequence += [holding_string]

    # remove duplicates from permutations_of_sequence
    return list(dict.fromkeys(permutations_of_sequence))


print(get_permutations("cat"))

if __name__ == '__main__':
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    print("-------------")
    example_input = 'xyz'
    print('Input:', example_input)
    print('Expected Output:', ['xyz', 'xzy', 'yzx', 'yxz', 'zxy', 'zyx'])
    print('Actual Output:', get_permutations(example_input))
    print("-------------")
    example_input = 'pr'
    print('Input:', example_input)
    print('Expected Output:', ['pr', 'rp'])
    print('Actual Output:', get_permutations(example_input))
