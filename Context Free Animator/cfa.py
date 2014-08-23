##############################################################################
# cfa.py
##############################################################################
# Parses the command line input and executes the animator.
##############################################################################

import sys
import os
from optparse import OptionParser

from lib.parser import *
from lib.contextfree import *

##############################################################################
# CONSTANTS
##############################################################################

#CHANGE THIS PATH TO POINT TO YOUR INSTALLATION DIR FOR CONTEXT FREE
CF_PATH = os.path.join("C:\\","Users","Gary","AppData",
                       "Local","OzoneSoft","ContextFree","ContextFreeCLI.exe")

##############################################################################
# PRIVATE FUNCTIONS
##############################################################################
    
def _print_usage():

    usage_file = None
    
    try:
        usage_file = open("usage.txt")
    except:
        print("Error opening usage file!")
        raise
    
    for line in usage_file:
        print(line)
                   
    usage_file.close()

##############################################################################
# MAIN FUNCTION
##############################################################################

def main():
    
    #create the option parser
    parser = OptionParser()
    
    #parse the options and the arguments
    (options, args) = parser.parse_args()
    
    #validate args
    
    #check there are 3 arguments
    if not ((len(args) is 3) or (len(args) is 4)):
        print("There must be 3 or 4 arguments!")
        _print_usage()
        return 1
        
    #check that first argument is at least 6 chars long 'x.cfda'
    if not (len(args[0]) >= 6):
        print("Argument 1 is too short to be a .cfda file.")
        _print_usage()
        return 1
    
    #check that first argument is a cfda file
    if not (args[0][-5:] == ".cfda"):
        print("Argument 1 must be a '.cfda' file.")
        _print_usage()
        return 1
        
    #try load the file
    input_cfda = None
    
    try:
        input_cfda = open(args[0])
    except:
        print("Unable to open cfda file.")
        _print_usage()
        return 1
        
    #save contents of input file and close it
    input_lines = []
    
    for line in input_cfda:
        input_lines.append(line)
        
    input_cfda.close()    
        
    #check that second argument is a valid folder on file system
    if not os.path.isdir(args[1]):
        print("Output directory does not exist!")
        _print_usage()
        return 1
    
    #save the output directory for convenience
    output_dir = args[1]
    
    #check the num_frames argument is correct
    num_frames = 0
    
    try:
        num_frames = int(args[2])
    except:
        pass
        
    if num_frames<=0:
        print("Number of frames must be an int greater than zero.")
        _print_usage()
        return 1
        
    #save the Context Free options
    cf_options = None
    
    if(len(args) is 4):
        cf_options = args[3]
        
    #generate the animation frames
    
    for i in range(num_frames):
        
        #parse the input cfda
            
        try:
            parsed_input_file = parse_file(input_lines,i)
        except ParseException as e:
            print("Animator parse exception on line "+str(e.line_num)+".")
            return 1
            
        
        #name of current frame output file
        frame_file = str(i).zfill(len(str(num_frames))-1)+".png"
        
        #create the location for the output file for each frame
        output_path = os.path.join(output_dir,frame_file)
        output_path = os.path.abspath(output_path)
        
        #generate image with context free
        try:
            call_context_free(CF_PATH,parsed_input_file,output_path,
                              cf_options)
        except:
            print("An error occurred when trying to call Context Free!")
            print("Check the path to Context Free is correct.")
            return 1
    
    
    

##############################################################################
# MAIN EXECUTION
##############################################################################

if __name__ == "__main__":
    sys.exit(main())