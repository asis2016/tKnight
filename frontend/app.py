from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/environ')
def environ():
    return render_template('environ.html')


@app.route('/processes')
def processes():
    return render_template('processes.html')


@app.route('/traceroute')
def trace_route():
    return render_template('traceroute.html')



@app.route('/get_route', methods=['GET'])
def get_data():
    try:
        # Read data from the JSON file
        with open('testing/test.json', 'r') as file:
            data = file.read()

        # You may want to parse the JSON data if further processing is needed
        # For example, if your JSON data is a list, you can use:
        # data = json.loads(data)

        return jsonify({'data': data})
    except FileNotFoundError:
        return jsonify({'error': 'File not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)