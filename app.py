from flask import Flask, render_template, request
from art.art1 import generate_art1
from art.art2 import generate_art2
from art.art3 import generate_art3
from visualization.visual1 import generate_visual1  # <-- move this here

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/art1', methods=["GET", "POST"])
def art1_view():
    image = None
    if request.method == "POST":
        num_shapes = int(request.form["num_shapes"])
        palette = request.form.get("palette", "random")
        image = generate_art1(num_shapes, palette)
    return render_template("art1.html", image=image)

@app.route('/art2', methods=["GET", "POST"])
def art2_view():
    image = None
    if request.method == "POST":
        num_shapes = int(request.form["num_shapes"])
        image = generate_art2(num_shapes)
    return render_template("art2.html", image=image)

@app.route('/art3', methods=["GET", "POST"])
def art3_view():
    image = None
    if request.method == "POST":
        num_shapes = int(request.form["num_shapes"])
        palette = request.form.get("palette", "random")
        image = generate_art3(num_shapes, palette)
    return render_template("art3.html", image=image)


@app.route('/visual1', methods=["GET", "POST"])
def visual1_view():
    image = None
    if request.method == "POST":
        image = generate_visual1()
    return render_template("visual1.html", image=image)


if __name__ == "__main__":
    app.run(debug=True)


