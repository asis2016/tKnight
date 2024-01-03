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
    return render_template('environ.html', page_title='Environment Variables')


@app.route('/ipscanner')
def ipscanner():
    return render_template('ipscanner.html', page_title="IP Scanner", display="d-none")


@app.route('/lsof')
def lsof():
    return render_template('lsof.html', page_title="List of Open Files")


@app.route('/scan-port')
def portscanner():
    # get ip query string
    hostname = request.args.get('hostname')
    return render_template('portscanner.html', hostname=hostname)


@app.route('/processes')
def processes():
    return render_template('processes.html', page_title='Processes')


@app.route('/systemctl/services/')
def systemctl_services():
    return render_template('systemctlservices.html', page_title="Systemctl Services")


@app.route('/syslog/')
def syslog():
    return render_template('syslog.html', page_title="tKnight Sys Log", display='d-none')


@app.route('/traceroute')
def traceroute():
    return render_template('traceroute.html')


if __name__ == '__main__':
    app.run()