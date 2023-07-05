#!/usr/bin/env python3


# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or (at
# your option) any later version.
# THIS PROGRAM IS MADE AVAILABLE FOR DISTRIBUTION WITHOUT ANY FORM OF WARRANTY TO THE
# EXTENT PERMITTED BY APPLICABLE LAW. THE COPYRIGHT HOLDER PROVIDES THE PROGRAM AS IS
# WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE. THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM LIES
# WITH THE USER. SHOULD THE PROGRAM PROVE DEFECTIVE IN ANY WAY, THE USER ASSUMES THE
# COST OF ALL NECESSARY SERVICING, REPAIR OR CORRECTION. THE COPYRIGHT HOLDER IS NOT
# RESPONSIBLE FOR ANY AMENDMENT, MODIFICATION OR OTHER ENHANCEMENT MADE TO THE PROGRAM
# BY ANY USER WHO REDISTRIBUTES THE PROGRAM SO AMENDED, MODIFIED OR ENHANCED.

# IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING WILL THE
# COPYRIGHT HOLDER BE LIABLE TO ANY USER FOR DAMAGES, INCLUDING ANY GENERAL, SPECIAL,
# INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OR INABILITY TO USE THE
# PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE
# OR LOSSES SUSTAINED BY THE USER OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO
# OPERATE WITH ANY OTHER PROGRAMS), EVEN IF SUCH HOLDER HAS BEEN ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGES.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

import sys
import os

# ------------------start of main program----------------------

# command line arguments
# programname=sys.argv[0]
#print 'Number of arguments = ',len(sys.argv)
if len(sys.argv)!=2:
	print('Usage generat_tautomers.py.py file.smi')
	print('e.g. generate_tautomers.py uracil.smi')
	sys.exit(1)
	
## temporary files used 
temp_csv_filename="my_temp_file.csv"

# executables used
ambit_path="./"
ambit_exe="ambit-tautomers-2.0.0-SNAPSHOT.jar"
	
filename=sys.argv[1]
# print('SMILEs Filename = ',filename)
file1=open(filename,'r')
file2=open(temp_csv_filename,'w')
file2.write("SMILES,name\n")

# loop over lines in space separated smiles name file
# create comma separated smiles,name file 
for line in file1.readlines():
	# print line
    ##print ("line=",line)
    # split with no arguments splits on white space
    list1=line.split()
    smiles=list1[0]
# name has carriage return on the end - but that is fine. 
    name=list1[1]
    writeme=smiles+","+name
    ##print("smiles=",smiles," name=",name)
    file2.write(writeme)
file1.close()
file2.close() 
    
#
# define temporary file for output from ambit tautomer
#
temp_output="temp_output.csv"
#
# run Ambit tautomer
#
command="java -jar "+ambit_path+ambit_exe+" -f "+temp_csv_filename+" -t all -o "+temp_output
# print("command=",command)
os.system(command)

#
# convert temp CSV output file to a SMILEs format - ignore rankings
# write space separated smiles and tautomer name to STDOUT
#
file3=open(temp_output,'r')
linecount=0;
for line in file3.readlines():
    linecount=linecount+1
    if (linecount==1):
        #print("linecount = ",linecount,"line = ",line)
# split line into takens using comma as separator  
        tokens=line.split(",")
# find which position or column contains string SMILES
# find which position or column contains string name 
        for i, token in enumerate(tokens):
            if token == 'SMILES':
                #print("SMILES at position=",i)
                smilesposition=i
            if token == 'name':
                #print("name at position=",i)
                nameposition=i                
    if (linecount>1):
# if line includes phrase Original structure 
# then use this to find original structure name      
        tokens=line.split(",")
	#
	# this string is not ALWAYS at position 0 hence a weak method
        #if (tokens[0] == 'Original structure'):    
	#
	# better to use the find method
	#
        if (line.find('Original structure')>=0):
            compoundname=tokens[nameposition]
            #print("compound=",compoundname)
            tautomer_count=1
            smiles=tokens[smilesposition]
# print smiles and compound name to STDOUT
            print(smiles,compoundname)
        else:
            tautomer_count=tautomer_count+1;
            tokens=line.split(",")
            smiles=tokens[smilesposition]
            tautomer_name=compoundname+"_"+str(tautomer_count)
# print smiles and tautomer name to STDOUT
            print(smiles,tautomer_name)
file3.close()               



