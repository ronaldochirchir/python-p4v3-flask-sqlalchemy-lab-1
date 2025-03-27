#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Earthquake

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///earthquakes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return jsonify({'message': 'Flask SQLAlchemy Lab 1'}), 200

# Get earthquake by ID
@app.route('/earthquakes/<int:id>')
def earthquakes(id):
    earthquake = db.session.get(Earthquake, id)  # Fixed deprecated query
    if earthquake:
        return jsonify(earthquake.to_dict()), 200
    return jsonify({"message": f"Earthquake {id} not found."}), 404

# Get earthquakes by minimum magnitude
@app.route('/earthquakes/magnitude/<float:magnitude>')  # Fixed route type
def get_magnitude(magnitude):
    earthquakes = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()
    quake_list = [eq.to_dict() for eq in earthquakes]

    return jsonify({
        "count": len(quake_list),
        "quakes": quake_list
    }), 200

if __name__ == '__main__':
    app.run(port=5555, debug=True)
