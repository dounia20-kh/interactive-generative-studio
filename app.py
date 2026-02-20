from flask import Flask, render_template, request
from art.art1 import generate_art1
from art.art2 import generate_art2
from art.art3 import generate_art3
from visualization.visual1 import generate_visual1 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/art1', methods=["GET", "POST"])
def art1_view():
    image = None
    if request.method == "POST":
        try:
            num_shapes = int(request.form.get("num_shapes", 50))
            if num_shapes < 1: 
                num_shapes = 50
        except ValueError:
            num_shapes = 50
        palette = request.form.get("palette", "sunset")  # "sunset" par défaut si vide
        image = generate_art1(num_shapes, palette)

    return render_template("art1.html", image=image)
from flask import send_file

@app.route('/art1_ajax')
def art1_ajax():
    num_shapes = int(request.args.get("num_shapes", 50))
    palette = request.args.get("palette", "random")
    filename = generate_art1(num_shapes, palette)  # make sure art1.py supports palette
    return send_file(filename, mimetype='image/png')

@app.route('/art2', methods=["GET", "POST"])
def art2_view():
   
    if request.method == "POST":
        num_shapes = int(request.form.get("num_shapes", 50))
        palette = request.form.get("palette", "sunset")
    else:
        num_shapes = 50
        palette = "sunset"

   
    image = generate_art2(num_shapes, palette)
    return render_template("art2.html", image=image)

from flask import send_file

@app.route('/art2_ajax')
def art2_ajax():
    num_shapes = int(request.args.get("num_shapes", 50))
    palette = request.args.get("palette", "sunset")
    filename = generate_art2(num_shapes, palette)
    return send_file(filename, mimetype='image/png')

@app.route('/art3', methods=["GET", "POST"])
def art3_view():
    image = None
    if request.method == "POST":
        num_shapes = int(request.form["num_shapes"])
        palette = request.form.get("palette", "sunset")
        image = generate_art3(num_shapes, palette)
    return render_template("art3.html", image=image)

@app.route('/visual1', methods=["GET", "POST"])
def visual1_view():
    image = None
    if request.method == "POST":
        image = generate_visual1()
        if image is None:
            return "<h2>Error: Could not generate visualization. Check CSV data.</h2>"
    return render_template("visual1.html", image=image)

@app.route('/plot1.png')
def plot1():
    fig, ax = plt.subplots(figsize=(6,4))
    ax.plot(df['x'], df['y'], color='cyan', linewidth=3)
    ax.set_facecolor('#1f2937')  # dark background
    fig.patch.set_facecolor('#1f2937')
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', facecolor=fig.get_facecolor())
    buf.seek(0)
    return send_file(buf, mimetype='image/png')

@app.route('/plot2.png')
def plot2():
    fig, ax = plt.subplots(figsize=(6,4))
    ax.bar(df['x'], df['y'], color='magenta')
    ax.set_facecolor('#1f2937')
    fig.patch.set_facecolor('#1f2937')
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', facecolor=fig.get_facecolor())
    buf.seek(0)
    return send_file(buf, mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True)


