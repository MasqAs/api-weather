# Weather API

## Context

As part of an exercise, the idea is to be able to retrieve information via [open-meteo](https://open-meteo.com/en/docs).  
The statement is as follows:  

### First part  

**Endpoint :** <https://open-meteo.com/en/docs#hourly=temperature_2m>

- **Objective:** Develop an endpoint that returns the average temperature over a specified period.  
- **Request:** `GET /temperature?x=[X]&y=[Y]&prevision_jours=[prevision_jours]`
- **Parameters:** X and Y represent GPS coordinates.  

**Expected output:**

```json
"Temperature": {
  "average_temperature": ["Calculated average value"]
}
```

### Second part  

**Endpoint:** <https://open-meteo.com/en/docs#hourly=precipitation_probability>

- **Objective:** Create an endpoint that indicates, for the next 2 days, the time slots when it's advisable to go out with an umbrella, based on the probability of precipitation.
- **Request:** `GET /umbrella?x=[X]&y=[Y]`
- **Parameters:** X and Y represent GPS coordinates.
- **How it works:** If precipitation_probability is greater than 50%, these hours are marked as requiring an umbrella.

**Expected output:**

```json
{
  "sort_ton_parapluie": ["List of time slots"]
}
```

## Install and execution

```bash
git clone https://github.com/MasqAs/weather-api.git
python -m venv .venv 
source .venv/bin/activate
pip install -r requierement.txt
python3 api.py
```

To call API endpoint :  

```bash
❯ curl  -X GET 'http://127.0.0.1:5000/temperature?x=52.12&y=13.4&prevision_jours=3'
{
  "Temperature": {
    "temperature_moyenne": [
      7.68
    ]
  }

curl  -X GET 'http://127.0.0.1:5000/parapluie?x=52.12&y=13.4&prevision_jours=3'
{
  "sort_ton_parapluie": []
}
```

## Technical Debt

- Handle "," as the decimal separator
- Add logs
