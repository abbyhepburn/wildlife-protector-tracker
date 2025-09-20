#Import the Flask framework and helper functions
from flask import Flask, render_template, request, jsonify
# Create the Flask app
app = Flask(__name__)

# Temporary storage for user actions (in memory only, not a database)
actions = []

# Map each action type to an animal 🐢🐦🐬
animal_map = {
    "Recycle": "Turtle",
    "Bike": "Bird",
    "Save Water": "Dolphin"
}

# ---- ROUTES ----

# Homepage (simple text to confirm the server is running)
@app.route("/")
def home():
    return "Wildlife Protector Tracker is running!"

# Tracker page → serves the HTML form we made in templates/index.html
@app.route("/tracker")
def tracker():
    return render_template("index.html")

# API endpoint for actions (both GET and POST supported)
@app.route("/api/actions", methods=["GET", "POST"])
def handle_actions():
    if request.method == "POST":
        # Parse JSON data sent from the frontend
        data = request.json

        # Add the matching animal (using our animal_map dictionary)
        data["animal"] = animal_map.get(data.get("type"), "Unknown")

        # Save this action into our in-memory list
        actions.append(data)

        # Send back confirmation + all actions so far
        return jsonify({"status": "ok", "actions": actions})

    # If it's a GET request → just return all actions
    return jsonify(actions)

# ---- START THE APP ----
if __name__ == "__main__":
    # debug=True → auto-restarts the server when you make code changes
    app.run(debug=True)
