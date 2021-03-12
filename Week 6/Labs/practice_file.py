def text_counter(file_name):
	import re

	from_count = 0

	mbox_file = open(file_name)
	for word in mbox_file:
		if re.search('From:', word):
			from_count += 1
	mbox_file.close()

	return from_count


answer = text_counter('mbox.txt')
print(f"The number of times 'From:' is in the text is {answer} times")



def num_extract(file_name):
    import re 
    
    match_list = []
    extract = 0
    count = 0
    
    mbox_file = open(file_name)
    for word in mbox_file:
        if re.findall(r'New Revision:', word):
            match_list.append(word)
    
    for item in match_list:
        for num in item.split():
            if str(num).isdigit():
                extract += int(num)
                count += 1
    
    average = extract / count
    
    return f"The average of the numbers is: {round(average, 2)}"

    mbox_file.close()

answer = num_extract('mbox.txt')
print(answer)



text = "any machine with more than 6 GHz and 500 GB of disk space for less than $999.99"

def str_extract(text):
    import re
    
    matches = re.findall(r"(\d+\s[Gg][Hh]z|\d+\s[Gg][Bb]|Mac|\$\d+(?:\.\d+)?)", text)
    
    return matches

answer = str_extract(text)
answer