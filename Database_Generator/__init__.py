
from flask import Flask, render_template, request, redirect, url_for, send_file
import requests
import utils.api


app = Flask(__name__)










@app.route('/')
def index():
    print()
    return render_template('index.html')




# if __name__ == "__main__":
#     app.run(debug=True)