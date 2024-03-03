import utils.weather as weather
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/temperature", methods=["GET"])
def temperature():
    # Extract query parameters
    latitude = request.args.get("x", type=float)
    longitude = request.args.get("y", type=float)
    forecast_days = request.args.get("prevision_jours", type=int)

    # Ensure all parameters are provided
    if latitude is None or longitude is None or forecast_days is None:
        return jsonify({"error": "Missing parameters"}), 400

    # Call the weather_average function with the parameters
    try:
        average_temperature = weather.weather_average(latitude, longitude, forecast_days)
        # Updated response format as per the requirement
        return jsonify({"Temperature": {"temperature_moyenne": [average_temperature]}})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/parapluie", methods=["GET"])
def parapluie():
    # Extract query parameters for latitude and longitude
    latitude = request.args.get("x", type=float)
    longitude = request.args.get("y", type=float)

    # Ensure both parameters are provided
    if latitude is None or longitude is None:
        return jsonify({"error": "Missing parameters"}), 400

    # The forecast is fixed to 2
    forecast_days = 2

    # Call the need_umbrella function with the parameters
    try:
        times_list = weather.need_umbrella(latitude, longitude, forecast_days)
        # Format the response as specified
        return jsonify({"sort_ton_parapluie": times_list})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
