from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/documentation')
def documentation():
    return render_template('documentation.html')


@app.route('/environ')
def environ():
    return render_template('environ.html')


@app.route('/ipscanner')
def ipscanner():
    return render_template('ipscanner.html')


@app.route('/scan-port')
def portscanner():
    # get ip query string
    hostname = request.args.get('hostname')
    return render_template('portscanner.html', hostname=hostname)


@app.route('/processes')
def processes():
    return render_template('processes.html')


@app.route('/systemctl/services/')
def systemctl_services():
    return render_template('systemctlservices.html')


@app.route('/traceroute')
def traceroute():
    return render_template('traceroute.html')


if __name__ == '__main__':
    app.run()