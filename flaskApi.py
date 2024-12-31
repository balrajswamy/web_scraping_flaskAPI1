from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

@app.route("/data", methods=["GET"])
def getAll_data():
    connection = sqlite3.connect("mydatabase.sqlite3")
    cursor = connection.cursor()

    result = cursor.execute("""SELECT * from flaskAPI_table""")
    data = result.fetchall()

    return jsonify({"data": data})

@app.route("/data/<int:id>", methods= ["GET"])
def get_record_by_id(id):
    connection = sqlite3.connect("mydatabase.sqlite3")
    cursor = connection.cursor()

    result = cursor.execute(f"SELECT * from flaskAPI_table where id = {id}")
    data = result.fetchone()

    return jsonify({"data": data})


if __name__ == "__main__":
    app.run(debug=True)