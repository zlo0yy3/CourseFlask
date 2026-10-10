from flask import Flask, render_template

app = Flask(__name__)

# Головна сторінка
@app.route("/")
def home():
    return render_template("index.html")

# Сторінка зі списком 
@app.route("/books")
def books():
    my_books = ["1984", "Brave New World", "The Hobbit", "Dune"]
    return render_template("items.html", items=my_books, title="My Favorite Books")

# Сторінка "Про мене"
@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
