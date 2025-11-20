import json
import requests

def handler(event, context):
    # Get query parameters (or default to New York)
    params = event.get('queryStringParameters') or {}
    lat = params.get('lat', '40.71')
    lon = params.get('lon', '-74.01')
    
    # Open-Meteo API (Free, no key required)
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    
    try:
        response = requests.get(url)
        data = response.json()
        current_temp = data['current_weather']['temperature']
        
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Success",
                "location": f"Lat: {lat}, Lon: {lon}",
                "temperature": f"{current_temp} C",
                "source": "Deployed via AWS CodeBuild & GitHub"
            })
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }