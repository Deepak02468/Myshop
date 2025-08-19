from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy   # ✅ database ke liye

app = Flask(__name__)

# ✅ Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


# Routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/products")
def products():
    return render_template("products.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)

