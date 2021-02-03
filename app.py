from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def hello():
	if request.method == 'POST':
		number = request.form.get('input_number')
		return render_template("index.html", number=str(number), factorial="")
	return render_template("index.html")


if __name__ == "__main__":
    app.run(host ='0.0.0.0', debug=True, port=80)