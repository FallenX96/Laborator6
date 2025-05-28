from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

def get_connection():
    return psycopg2.connect(
        host="db",
        database="postgres",
        user="postgres",
        password="postgres"
    )

@app.route("/", methods=["GET"])
def index():
    return "Aceasta este o aplicație Flask pentru gestionarea notițelor."

@app.route("/notita", methods=["POST"])
def add_note():
    content = request.json["notita"]
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO notite (continut) VALUES (%s)", (content,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"status": "Notiță adăugată!"})

@app.route("/notita", methods=["GET"])
def get_notes():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT continut FROM notite")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([r[0] for r in rows])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)