# Problem Set 4A
# Name: Pat
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    permutations_of_sequence = []
    #define base case: sequence string len(1)
    if len(sequence) == 0:
        permutations_of_sequence += []
    if len(sequence) == 1:
        permutations_of_sequence += sequence    
    #recursively call get_permutations for sequence[1:n] until len(sequence[1:n])==0    
    if len(sequence) > 0:
        recursive_variable = get_permutations(sequence[1:])
    


        
    #write recursive case
    #for sequence of len(n), case is sequence[0] and sequence[1:n] 
    #appends permutations of len(n) to permutations_of_sequence
    if #something
        first_char = sequence[0]
        cutdown_sequence = sequence[1:]
        #concatenate sequence[0] along each position of sequence[1:n] 
        for i in range(len(cutdown_sequence)+1):
            holding_string = cutdown_sequence[:i] + first_char + cutdown_sequence[i:]
            permutations_of_sequence += [holding_string]
       

    return permutations_of_sequance
    
        
    pass #delete this line and replace with your code here

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    pass #delete this line and replace with your code here

