from flask import Flask
from subprocess import check_output
app = Flask(__name__)

@app.route('/')
def factron():
    facterdata = check_output(["facter", "-j"])    
    return facterdata 

@app.route('/<fact>')
def factron_fact(fact):
    facterdata = check_output(["facter", "-j", fact])    
    return facterdata 
