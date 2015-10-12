data = {
    "message": "like",
    "cod": "200",
    "count": 1,
    "list": [
        {
            "id": 5419384,
            "name": "Denver",
            "coord": {
                "lon": -104.984703,
                "lat": 39.739151
            },
            "main": {
                "temp": 300.41,
                "pressure": 1015,
                "humidity": 18,
                "temp_min": 296.48,
                "temp_max": 303.15
            },
            "dt": 1444599249,
            "wind": {
                "speed": 6.7,
                "deg": 320,
                "gust": 9.8
            },
            "sys": {
                "country": "US"
            },
            "clouds": {
                "all": 40
            },
            "weather": [
                {
                    "id": 802,
                    "main": "Clouds",
                    "description": "scattered clouds",
                    "icon": "03d"
                }
            ]
        }
    ]
}


def main():
    print(data['list'][0]['coord']['lat'], data['list'][0]['coord']['lon'])

if __name__ == '__main__':
    main()