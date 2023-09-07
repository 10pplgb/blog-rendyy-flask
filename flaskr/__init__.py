#import aplikasi flask untuk dipakai di web kita
from flask import Flask

#mengatur nama aplikasi
app = Flask(__name__)

#mengatur URI(universal resource identifier), dan apa yang ditampilkan jika URI tersebut diakses
@app.route('/') #ketika alamat http://127.0.0.1.5000/ dipanggil,maka server akan mengeksekusi fungsi hello()
def hello(): #function dengan nama hello
    return 'Hello, World!'


@app.route("/login")
def login():
    return 'halaman login'