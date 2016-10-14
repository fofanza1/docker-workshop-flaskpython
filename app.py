from flask import Flask
from flask import render_template,request, send_from_directory

import socket


app = Flask(__name__, static_url_path='')

@app.route("/")
def index():
    return render_template('helloworld.html',hostname=socket.gethostname())


if __name__ == "__main__":
    app.run(host='0.0.0.0')
