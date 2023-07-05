#
# Simple Flask web application to run tautomer generation and scoring pipeline 
# If using route URL localhost:5000 This will give a sensible usage example.
#
import subprocess

from flask import Flask
app = Flask(__name__)

def run_command(command1):
    return subprocess.Popen(command1, shell=True, stdout=subprocess.PIPE).stdout.read()

@app.route('/')
def index():
	return'<h3> Try URL localhost:5000/tautomerise/"Oc1nccc(O)n1  Uracil" </h3>'

# allow for 2 URLs 
# one for index (see above) and one to run bash script tautomerise.sh

#
# To enable tatutomatic related tools and flask use 
#       conda activate tautomatic 
#	NB This environment has openbabel, xtb and flask installed 
# To set up flask set envieonment variables as follows in the shell
#       export FLASK_APP=flask_tautomers
#       export FLASK_ENV=development
# Then start Flask application with 
#        run flask
# use this by browing to (say) http://localhost:5000/tautomerise/"Oc1nccc(O)n1 Uracil"
#
@app.route('/tautomerise/<smilesspacename>')
def tautomerise(smilesspacename):
	string1='bash tautomerise.sh '+smilesspacename
	return run_command(string1)

