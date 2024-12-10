from flask import Flask, request, render_template, jsonify

app = Flask(__name__)
data_store = []

@app.route("/")
def index():
    return render_template("index.html", data=data_store)

@app.route("/data", methods=["POST"])
def receive_data():
    global data_store
    data = request.json
    if data:
        data_store.append(data)
        if len(data_store) > 20:
            data_store.pop(0)  # Mantén solo los últimos 20 datos
    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(debug=True)
