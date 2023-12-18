from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/environ')
def environ():
    return render_template('environ.html')


@app.route('/ipscanner')
def ipscanner():
    return render_template('ipscanner.html')


@app.route('/processes')
def processes():
    return render_template('processes.html')


@app.route('/traceroute')
def trace_route():
    return render_template('traceroute.html')


if __name__ == '__main__':
    app.run(debug=True)