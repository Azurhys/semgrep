from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Hello, World!</h1>"

@app.route('/evaluate', methods=['POST'])
def evaluate_data():
    data = request.form.get('data')
    if data is None:
        return "Error: No data provided", 400
    
    return "ok"

if __name__ == '__main__':
    app.run(debug=True)
