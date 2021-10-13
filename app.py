from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
  app.run(debug=True, port=5000, host='0.0.0.0')