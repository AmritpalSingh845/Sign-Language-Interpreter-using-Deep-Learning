#from crypt import methods
from flask import Flask, render_template, request
import subprocess, sys
from subprocess import Popen, PIPE, run  
import create_gestures

app = Flask(__name__)

@app.route('/')
def first():
    return render_template("index.html")

@app.route('/set_hist')
def run_script():
    # file = open(r'E:/VS Code Files/Final Year Project/Sign-Language-Interpreter-using-Deep-Learning/Code/Final.py', 'r').read()
    # return exec(file)
    run([sys.executable,'code/set_hand_histogram.py'],shell=False,stdout=PIPE)
    return render_template("index.html")

@app.route('/create_gesture')
def f1():
    return render_template("a.html")

@app.route('/create_gesture', methods=['GET','POST'])
def create_gest():
    # print("H")
    pid = request.form['fname']
    pname = request.form['lname']
    # file = open(r'E:/VS Code Files/Final Year Project/Sign-Language-Interpreter-using-Deep-Learning/Code/Final.py', 'r').read()
    # return exec(file)
    create_gestures.main_fun(pid,pname)
    run([sys.executable,'code/Rotate_images.py'],shell=False,stdout=PIPE)
    run([sys.executable,'code/load_images.py'],shell=False,stdout=PIPE)
    run([sys.executable,'code/cnn_model_train.py'],shell=False,stdout=PIPE)
    return render_template("index.html")

@app.route('/predict')
def pred():
    # file = open(r'E:/VS Code Files/Final Year Project/Sign-Language-Interpreter-using-Deep-Learning/Code/Final.py', 'r').read()
    # return exec(file)
    run([sys.executable,'code/final.py'],shell=False,stdout=PIPE)
    return render_template("index.html")

if __name__ == "__main__":
    # run([sys.executable,'E:\VS Code Files\Final Year Project\Sign-Language-Interpreter-using-Deep-Learning\Code\set_hand_histogram.py'],shell=False,stdout=PIPE)
    app.run(debug=True)