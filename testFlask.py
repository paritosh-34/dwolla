from flask import Flask, render_template
from utilFunctions import get_iav_token

app = Flask(__name__)


@app.route("/")
def home():
    customer_url = 'https://api-sandbox.dwolla.com/customers/6c15acaf-3a13-483f-8d03-dfb3915d4a68'
    t = get_iav_token(customer_url)
    return render_template("index.html", env='sandbox', token=t, phone='8146990621')


app.run()
