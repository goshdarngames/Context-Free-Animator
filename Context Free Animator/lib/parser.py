##############################################################################
# parser.py
##############################################################################
# Methods and classes that relate to cfda parsing.
##############################################################################

##############################################################################
# EXCEPTIONS
##############################################################################

class ParseException(Exception):

    def __init__(self,line_num):
        self.line_num = line_num
        
##############################################################################
# PARSE FILE
##############################################################################

def parse_file(lines,step):
    print("Parsing CFDA file.")
    
    #this will hold the lines after parsing
    parsed_lines = []
    
    #loop through each line
    for i in range(len(lines)):
        
        #this line will be built as file is parsed
        parsed_line = ""
        
        #split the line into chunks according to # separator
        split_line = lines[i].split("#")
        
        #if there is only one part just add the line
        if(len(split_line) <= 1):
            parsed_lines.append(lines[i])
            continue
        
        #loop through each chunk
        for j in range(len(split_line)):
        
            #even numbered sections will be plain text
            if j%2 is 0:
                parsed_line += split_line[j]
                
            #odd numbered sections will be special text
            else:
                special_parts = split_line[j].split(",")
                
                operation = special_parts[0].strip()
                
                if operation == "add":
                    try:
                        start_num = float(special_parts[1].strip())
                        inc_num = float(special_parts[2].strip())
                        
                        parsed_line+=str(start_num + inc_num*step)
                        
                    except:
                        #return line where error occurred
                        raise ParseException(i+1)
                
                #no valid operation found
                else:
                    raise ParseException(i+1)
        
        #add the constructed line
        parsed_lines.append(parsed_line)
        
    return parsed_lines