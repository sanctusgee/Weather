
w_data = {
    "response": {
        "version": "0.1",
        "termsofService": "http://www.wunderground.com/weather/api/d/terms.html",
        "features": {
            "conditions": 1
        },
        "results": [
            {
                "name": "Denver",
                "city": "Denver",
                "state": "CO",
                "country": "US",
                "country_iso3166": "US",
                "country_name": "USA",
                "zmw": "80202.1.99999",
                "l": "/q/zmw:80202.1.99999"
            },
            {
                "name": "Denver",
                "city": "Denver",
                "state": "IL",
                "country": "US",
                "country_iso3166": "US",
                "country_name": "USA",
                "zmw": "62321.3.99999",
                "l": "/q/zmw:62321.3.99999"
            },
            {
                "name": "Denver",
                "city": "Denver",
                "state": "IN",
                "country": "US",
                "country_iso3166": "US",
                "country_name": "USA",
                "zmw": "46926.1.99999",
                "l": "/q/zmw:46926.1.99999"
            },
            {
                "name": "Denver",
                "city": "Denver",
                "state": "IA",
                "country": "US",
                "country_iso3166": "US",
                "country_name": "USA",
                "zmw": "50622.1.99999",
                "l": "/q/zmw:50622.1.99999"
            },
            {
                "name": "Denver",
                "city": "Denver",
                "state": "KY",
                "country": "US",
                "country_iso3166": "US",
                "country_name": "USA",
                "zmw": "41222.3.99999",
                "l": "/q/zmw:41222.3.99999"
            },
            {
                "name": "Denver",
                "city": "Denver",
                "state": "MO",
                "country": "US",
                "country_iso3166": "US",
                "country_name": "USA",
                "zmw": "64441.1.99999",
                "l": "/q/zmw:64441.1.99999"
            },
            {
                "name": "Denver",
                "city": "Denver",
                "state": "NY",
                "country": "US",
                "country_iso3166": "US",
                "country_name": "USA",
                "zmw": "12421.1.99999",
                "l": "/q/zmw:12421.1.99999"
            },
            {
                "name": "Denver",
                "city": "Denver",
                "state": "NC",
                "country": "US",
                "country_iso3166": "US",
                "country_name": "USA",
                "zmw": "28037.1.99999",
                "l": "/q/zmw:28037.1.99999"
            },
            {
                "name": "Denver",
                "city": "Denver",
                "state": "PA",
                "country": "US",
                "country_iso3166": "US",
                "country_name": "USA",
                "zmw": "17517.1.99999",
                "l": "/q/zmw:17517.1.99999"
            },
            {
                "name": "Denver",
                "city": "Denver",
                "state": "TN",
                "country": "US",
                "country_iso3166": "US",
                "country_name": "USA",
                "zmw": "37134.2.99999",
                "l": "/q/zmw:37134.2.99999"
            }
        ]
    }
}

def main():
    # condition = ["{} {} {}".format(w_data['current_observation']["display_location"]['state_name'],
    #                                w_data['current_observation']["display_location"]['country'], w_data['current_observation']['temp_f'])]
    #              # for d in w_data['current_observation'] ]
    cities = w_data["response"]["results"]
    print(cities)
    # for item in cities:
    a = [ [item["state"], item["city"]] for item in cities]
    print(a)
    # print("{}, {}".format(d["state"], d["city"]) for d in cities )
    # print("{}, {}".format(w_data["current_observation"]["display_location"]["state_name"],
    #                       w_data["current_observation"]["display_location"]["country"]))
    # print w_data["current_observation"]["temp_f"]


if __name__ == '__main__':
    main()
