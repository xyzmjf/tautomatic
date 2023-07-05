#/usr/bin/bash


# if using with Flask app then note the following
# run flask app after conda activate tautomatic 
# note that tautomatic environment should now have flask installed as well. 
# test this with 
# export FLASK_APP=flask_tautomers
# export FLASK_ENV=development
# 	flask run
# then browse to localhost:5000 
# note URL given in response and try that


# this script tautomerise.sh takes quoted "smiles name" as 1 argument
# example tautomerish.sh "Oc1nccc(O)n1 uracil"
# NB some possible issues with \ and / characters in bash arguments to be
# worked out

array1=($1)
smiles=${array1[0]}
name=${array1[1]}
filename1="temp_$name.smi"
filename2="temp_tautomers_$name.smi"
filename3="temp_scores_$name.txt"
filename4="temp_relative_$name.txt"
filename5="temp_scores_$name.svg"
#echo "smiles = $smiles"
#echo "name=$name"
#echo "filename1= $filename1"
#echo "filename2= $filename2"
#echo "filename3= $filename3"
#echo "filename4= $filename4"
#echo "filename5= $filename5"
#exit

# setup smiles input file 

echo $1 $2 > $filename1 
#pwd
python3 generate_tautomers.py $filename1 > $filename2
python3 score_tautomers.py $filename2 > $filename3 
python3 relative_scores.py $filename3 > $filename4
obabel -ismi $filename4 -osvg > $filename5 
cat $filename5 

