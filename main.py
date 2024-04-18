from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("html/index.html")

@app.route("/operacaoV2")
def operacaoV2():
  return render_template("html/operacaoV2.html")