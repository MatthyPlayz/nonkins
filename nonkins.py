from flask import render_template, Flask, redirect, url_for
from subprocess import Popen
from os import chdir
app = Flask(__name__)
title = "Nonkins Base"
buildc = 0
amt = 1
class buildtools:
    def buildp(amt, btrli):
        global buildc
        buildc+=amt
        for i in range(0,len(btrli)):
            try:
                Popen(btrli[i])
            except Exception as err:
                print("Error: " + str(err) + " on string " + btrli[i])
try:
    Popen("git clone https://github.com/MatthyPlayz/MatthysChedibles")
    Popen("gradlew setupDecompWorkspace")
except:
    print("Pre-build failed")
@app.route('/')
def index():
    global title, buildc
    user = {'title': 'Nonkins Base'}
    try:
        chdir("MatthysChedibles")
    except:
        pass
    return render_template("index.html", buildc=buildc, submit=buildtools, title=user["title"], btr=["gradlew.bat build"]) #user["btr"]
#render_template('index.html', title=user['title'], user=user, submit=inc(buildc), buildc=buildc)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)

