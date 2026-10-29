import hmac
import os

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Demo-only credentials for the proof-of-concept login page. Nothing is stored,
# logged, or sent anywhere; the comparison happens in-process and is discarded.
DEMO_USERNAME = os.environ.get("DEMO_USERNAME", "demo")
DEMO_PASSWORD = os.environ.get("DEMO_PASSWORD", "demo")


@app.get("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    message = None
    ok = False

    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")

        user_matches = hmac.compare_digest(username, DEMO_USERNAME)
        pass_matches = hmac.compare_digest(password, DEMO_PASSWORD)

        if user_matches and pass_matches:
            ok = True
            message = "Demo login accepted. This is a mock page — no session was created."
        else:
            message = "Demo login rejected. Use the demo credentials shown above."

    return render_template(
        "login.html",
        message=message,
        ok=ok,
        demo_username=DEMO_USERNAME,
        demo_password=DEMO_PASSWORD,
    )


@app.get("/health")
def health():
    return jsonify(status="ok")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "5000")))
