from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.network.urlrequest import UrlRequest
import json


class AddLocationForm(BoxLayout):
    search_input = ObjectProperty()
    search_results = ObjectProperty()
    current_location = ObjectProperty()
    search_button = ObjectProperty()

    def test_method(self):
        if self.current_location.state == 'down':
            print("Button down!!!")
            print(self.current_location.state)

    def search_location(self):

        # OPenWeatherMap API implementation
        search_template = "http://api.openweathermap.org/data/2.5/find?q={}&" \
                          "type=like&APPID=xxxxxxxxxxxxxxxxxxxxxx"

        # WeatherUnderground (http://www.wunderground.com) API implementation
        # search_template = "http://api.wunderground.com/api/xxxxxxxxxxxxxxxxx/conditions/q/{}.json"
        search_url = search_template.format(self.search_input.text)
        request = UrlRequest(search_url, self.found_location)

    def found_location(self, request, data):

        # WeatherUnderground (http://www.wunderground.com) API implementation
        # data = json.loads(data.decode()) if not isinstance( data, dict) else data
        # cities = [ "{}-{}, ({})".format(d["city"], d["state"], d["country"]) for d in data["response"]["results"]]
        # self.search_results.item_strings = cities

        # check which button pressed:
        # if self.search_button.state == 'down':    # 'search location' button pressed
        #     # OPenWeatherMap API implementation
        #     cities = ["{} ({})". format(d['name'], d['sys']['country']) for d in data['list']]
        #     self.search_results.item_strings = cities
        # if self.current_location.state == 'down':
        #     cities = ["{} - Lat: {}, Long: {}".format(d['name'], d['coord']['lat'], d['coord']['lon'])
        #               for d in data['list']]
        #     self.search_results.item_strings = cities
        data = json.loads(data.decode()) if not isinstance(data, dict) else data
        cities = ["{} ({})". format(d['name'], d['sys']['country']) for d in data['list']]
        self.search_results.item_strings = cities

        self.search_results.adapter.data.clear()
        self.search_results.adapter.data.extend(cities)
        self.search_results._trigger_reset_populate()


class WeatherRoot(BoxLayout):
    pass

class WeatherApp(App):
    pass

if __name__ == '__main__':
    WeatherApp().run()
