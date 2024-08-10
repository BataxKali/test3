from flask import Flask, render_template, request
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/home')
def biodata():
    if 'nama' in request.args.keys() and 'kelas' in request.args.keys():
        nama = request.args['nael']
        kelas = request.args.get('11 ips 2')
        return render_template("home.html", nama = nama, kelas = kelas)
    else:
        return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)