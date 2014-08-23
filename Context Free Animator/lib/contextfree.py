##############################################################################
# contextfree.py
##############################################################################
# Provides the methods and classes used to talk with Context Free.
##############################################################################

import os
import subprocess

##############################################################################
# CONSTANTS
##############################################################################

TEMP_FILE_NAME = "CFAtemp.cfdg"

##############################################################################
# CALL CONTEXT FREE
##############################################################################

def call_context_free(cf_path, input_file, output_path, cf_options):
    print("Calling Context Free")
    
    print(cf_path)
    
    #split up options via space
    if cf_options is not None:
        cf_options = cf_options.split(" ")
    
    #create temporary file to pass to context free
    temp_file = open(TEMP_FILE_NAME,"w")
    
    for line in input_file:
        temp_file.write(line)
        
    temp_file.close()
    
    #get absolute path to temp input file
    input_path = os.path.abspath(TEMP_FILE_NAME)
        
    print("====Calling Context Free===")
    
    #build the arguments to pass to call
    call_args = []
    
    if not cf_options is None:
        call_args = [cf_path]+cf_options+[input_path,output_path]
    else:
        call_args = [cf_path,input_path,output_path]
    
    #try make a call to context free
    try:
        subprocess.call(call_args)
    except:
        raise
    
    #delete temp file
    os.remove(TEMP_FILE_NAME)
    
    
    