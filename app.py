from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Nikhilesh! Now to check the change in cluster second time"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


