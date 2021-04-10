#Function 1: Checks whether the string is a valid employee ID

def validate(employee_id):
    #initializes character and digit tracker
    char_count = 0
    dig_count = 0

    #creates a e_id list with the values from the employee_id
    e_id = [val for val in employee_id]

    #counts each character and digit in the e_id list
    for val in e_id:
        if val.isalpha():
            char_count += 1
        elif val.isdigit():
            dig_count += 1

    #conditions for employee_id
    if char_count >= 6 and char_count <= 10 and dig_count == 2 and e_id[-1].isdigit(
    ) and e_id[-2].isdigit():
        return True
    else:
        return False

# Validate
assert(validate('AbcdEf00'))
assert(validate('$0RQLpCHz49') == False)
print("Function 1: Asserts Completed Successfully")



#Function 2: Create a function that intakes a string, creates a dictionary with the characters
#          from the string (keys) and the probablity of the characters (values)


def dna_prob1(sequence):
    #collections module
    from collections import Counter

    #creates the dictionary of key,value pairs (character, count)
    counter = Counter(sequence)
    
    #initializes new dictionary
    probablity_dict = {}

    #total of values
    total = sum(counter.values())

    #loops through the key values in counter and adds them to the probability_dict
    for key, value in counter.items():
        probablity_dict[key] = value / total

    #returns probability dict
    return probablity_dict


#Validate
tbl = dna_prob1('ATCGATTGAGCTCTAGCG')
assert(tbl['T'] == 5/18)
assert(tbl['G'] == 5/18)
assert(tbl['C'] == 4/18)
print("Function 2: Asserts Completed Successfully")



#Function 3: Given a string representing a sequence of DNA bases, returns the paired sequence, 
#            also as a string, where A is always paired with T and C with G, i.e., replace A 
#            with T, T with A, ...

def dna_bp(sequence):
    #initialize new sequence
    new_seq = []

    #reverse the order of A / T and G / C
    for char in sequence:
        if char == 'A':
            T = 'T'
            new_seq.append(T)
        elif char == 'T':
            A = 'A'
            new_seq.append(A)
        elif char == 'G':
            C = 'C'
            new_seq.append(C)
        elif char == 'C':
            G = 'G'
            new_seq.append(G)

    #changes the list into a string
    return ''.join(new_seq)


#Validate
assert(dna_bp('ATCGATTGAGCTCTAGCG') == 'TAGCTAACTCGAGATCGC')
print("Function 3: Asserts Completed Successfully")


#Bonus Function: 
def dna_prob2(sequence):



# #Validate
# tbl = dna_prob2('ATCGATTGAGCTCTAGCG')
# assert(tbl['T']['T'] == 0.2)
# assert(tbl['G']['A'] == 0.5)
# assert(tbl['C']['G'] == 0.5)
# print("Bonus: Asserts Completed Successfully")









