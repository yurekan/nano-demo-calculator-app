from flask import Flask, request

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello World!'

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.json
    if "a" in data and "b" in data:
        a = data["a"]
        b = data["b"]
        result = a + b
        return result = {"result" : result}
    else:
        return result = {"result" : "Missing values"}

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.json
    if "a" in data and "b" in data:
        a = data["a"]
        b = data["b"]
        result = a - b
        return result = {"result" : result}
    else:
        return result = {"result" : "Missing values"}

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
