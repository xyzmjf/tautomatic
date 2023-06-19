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


#------------------------------------------------------------
# function find_xtb_energy
# file open close handled internally
# ----------------------------------------------------------
def find_xtb_energy(filename):
# conversion factors from Hartree to Kcal/mol and Kj/mol
    hartree_kcal=627.509    
    hartree_kj=2625.499	
    command="grep TOTAL "+filename+" | awk '{ print $4 }' > temp_energy.txt"
    #print("command=",command); 
    os.system(command)
    file2="temp_energy.txt"
    filehandle=open(file2,'r')
    for line in filehandle.readlines():
        #print("line=",line)
        line.rstrip()
        energy=float(line)
        #print("Hartrees=",energy)
        kcal=energy*hartree_kcal
        #print("Kcal=",kcal)
    return(kcal)
    filehandle.close()



# ------------------start of main program----------------------

# command line arguments
# programname=sys.argv[0]
#print 'Number of arguments = ',len(sys.argv)
if len(sys.argv)<2:
	print('Usage: score_tautomers.py.py file.smi')
	print('e.g. score_tautomers.py uracil.smi')
	print('or')
	print('Usage: score_tautomers.py file.smi solvent')
	print('e.g. score_tautomers.py uracil.smi water') 
	sys.exit(1)
	


filename=sys.argv[1]
# print('SMILEs Filename = ',filename)
#

solvent_xtb=''
if (len(sys.argv)==3):
    solvent=sys.argv[2]
    print("solvent=",solvent)   
    solvent_xtb=" --alpb "+solvent
#sys.exit(1) 


file1=open(filename,'r')
# loop over lines in space separated smiles name file
# create comma separated smiles,name file 
for line in file1.readlines():
	# print line
    ##print ("line=",line)
    list1=line.split(" ")
    smiles=list1[0]
# name has carriage return on the end - strip that off
    name=list1[1].rstrip()
    #writeme=smiles+","+name
    #print("smiles=",smiles," name=",name)
    
    # create temporary files for use by obabel and xtb
    temp_smiles_filename="temp_smiles_"+name+".smi"
    temp_xyz_filename="temp_"+name+".xyz";
    temp_xtb_output="temp_xtb_"+name+".out";
    
    # write out temporary smiles file - to be used by OB 
    file2=open(temp_smiles_filename,"w")
    writeme=smiles+" "+name   
    file2.write(writeme)
    file2.close()
    # generate xyz coordinate file from smiles file using OB
    command1="obabel -ismi "+temp_smiles_filename+" -oxyz --gen3D > "+temp_xyz_filename
    #print("command1=",command1)
    os.system(command1)
    # now generate command to run xtb 
    command2="xtb ./"+temp_xyz_filename+" --opt "+solvent_xtb+" > "+temp_xtb_output
    print("command2=",command2)
    os.system(command2)
        # extract xtb energy value
    energy_kcal=find_xtb_energy(temp_xtb_output)
    print("%s %s %8.2f" % (smiles,name,energy_kcal))
    
file1.close()

