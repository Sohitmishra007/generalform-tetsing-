from flask import Flask, request, render_template_string
import pymysql
import os

app = Flask(__name__)

def get_connection():
    return pymysql.connect(
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASS'],
        unix_socket=f"/cloudsql/{os.environ['INSTANCE_CONNECTION_NAME']}",
        db=os.environ['DB_NAME']
    )

@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form["name"]
        conn = get_connection()
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
            conn.commit()
        conn.close()
        return "Saved successfully!"
    return render_template_string("""
        <form method="post">
            Name: <input name="name">
            <input type="submit">
        </form>
    """)

# Add this block for local testing and Cloud Run compatibility
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
