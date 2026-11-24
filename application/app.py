from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder="../templates")

workouts = []

@app.route("/")
def index():
    return render_template("index.html", workouts=workouts)

@app.route("/add", methods=["POST"])
def add_workout():
    workout = request.form.get("workout", "").strip()
    duration = request.form.get("duration", "").strip()

    if workout and duration:
        workouts.append({
            "workout": workout,
            "duration": duration
        })

    return redirect(url_for("index"))

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
