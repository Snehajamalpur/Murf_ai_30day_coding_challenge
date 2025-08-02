from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/greet')
def greet():
    return jsonify(message="Hello from Sneha's Voice Agent!")

if __name__ == '__main__':
    app.run(debug=True)
