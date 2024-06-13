from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello():
	return render_template("index.html", myrange=range(3))

@app.route('/prompt', methods=['POST', 'GET'])
def prompt():
    prompt = request.form['prompt']
    print("user prompt received:", prompt)
    return render_template("index.html", myrange=range(3))

@app.route('/supersample', methods=['POST', 'GET'])
def supersample():
    tag = request.form['tag']
    print("save button", tag, "was clicked!!!")
    return render_template("index.html", myrange=range(3))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
    

