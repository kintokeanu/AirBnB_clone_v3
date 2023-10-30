#!/usr/bin/python3
# from api.v1.views import app_views
from flask import Flask, jsonify, Blueprint
from models import storage


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

@app_views.route('/status')
def status():
    """Return status"""
    return jsonify({"status": "OK"})


@app_views.route('/stats')
def stats():
    """Return stats"""
    return jsonify({"amenities": storage.count("Amenity"),
                    "cities": storage.count("City"),
                    "places": storage.count("Place"),
                    "reviews": storage.count("Review"),
                    "states": storage.count("State"),
                    "users": storage.count("User")})
