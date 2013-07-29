import sys

source = (file(sys.argv[1], 'r')).read()
destination = (file(sys.argv[2], 'w'))

index = 0
for char in source:
    if char == ':':
        tmp_str = ((source[index - 6]) + (source[index - 5]) + (source[index - 4]) 
                + (source[index - 3]) + (source[index - 2]) + (source[index - 1]))
        if tmp_str == 'mailto':

            right_index = index
            while (source[right_index] != '\"' and source[right_index] != ' '):
                right_index = right_index + 1
            
            email = ""
            iterator = index + 1
            while iterator < right_index:
                email = email + source[iterator]
                iterator = iterator + 1
            if email != "":
                destination.write(email + '\n')

    index = index + 1
