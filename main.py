from kivy.factory import Factory
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.network.urlrequest import UrlRequest
import json
from config.api_keys import api_keys
from kivy.uix.listview import ListItemButton


class WeatherRoot(BoxLayout):
    def show_current_weather(self, location):

        self.clear_widgets()
        current_weather = Factory.CurrentWeather()
        current_weather.location = location
        self.add_widget(current_weather)


class LocationButton(ListItemButton):
    pass


class AddLocationForm(BoxLayout):
    open_weather_id = api_keys['OPEN_WEATHER_MAP']

    search_input = ObjectProperty()
    search_results = ObjectProperty()
    current_location = ObjectProperty()
    search_button = ObjectProperty()

    def search_location(self):
        # OpenWeatherMap (http://openweathermap.org/) API implementation
        search_template = "http://api.openweathermap.org/data/2.5/find?q={}&" \
                          "type=like&APPID={}"

        # WeatherUnderground (http://www.wunderground.com) API implementation
        # search_template = "http://api.wunderground.com/api/xxxxxxxxxxxxxxxxx/conditions/q/{}.json"

        search_url = search_template.format(self.search_input.text, self.open_weather_id)
        request = UrlRequest(search_url, self.found_location)

    def found_location(self, request, data):

        # WeatherUnderground (http://www.wunderground.com) API implementation
        # data = json.loads(data.decode()) if not isinstance(data, dict) else data
        # cities = [ "{}-{}, ({})".format(d["city"], d["state"], d["country"]) for d in data["response"]["results"]]
        # self.search_results.item_strings = cities

        # OpenWeatherMap (http://openweathermap.org/) API implementation
        data = json.loads(data.decode()) if not isinstance(data, dict) else data
        cities = ["{} ({})". format(d['name'], d['sys']['country']) for d in data['list']]
        self.search_results.item_strings = cities

        # Python 3 syntax
        #self.search_results.adapter.data.clear()
        # Python 2.x syntax
        del self.search_results.adapter.data[:]
        self.search_results.adapter.data.extend(cities)
        self.search_results._trigger_reset_populate()


class WeatherApp(App):
    pass


if __name__ == '__main__':
    WeatherApp().run()
