from kivy.factory import Factory
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, ListProperty, StringProperty, NumericProperty
from kivy.network.urlrequest import UrlRequest
import json
from config.api_keys import api_keys
from kivy.uix.listview import ListItemButton

OPEN_WEATHER_ID = api_keys['OPEN_WEATHER_MAP']


class WeatherRoot(BoxLayout):
    current_weather = ObjectProperty()

    def show_current_weather(self, location=None):
        self.clear_widgets()

        if self.current_weather is None:
            # #location = ("New York",  "US")
            # location = CurrentWeather().location
            self.current_weather = CurrentWeather()

        if location is not None:
            # self.current_weather = Factory.CurrentWeather()
            self.current_weather.location = location
            self.current_weather.update_weather()
            # self.current_weather.
            self.add_widget(self.current_weather)

    def show_add_location_form(self):
        self.clear_widgets()
        add_location = Factory.WeatherRoot()
        self.add_widget(add_location)
        # self.add_widget(AddLocationForm())


class LocationButton(ListItemButton):
    location = ListProperty()


class AddLocationForm(BoxLayout):
    global OPEN_WEATHER_ID

    search_input = ObjectProperty()
    search_results = ObjectProperty()
    current_location = ObjectProperty()
    search_button = ObjectProperty()

    def search_location(self):
        # OpenWeatherMap (http://openweathermap.org/) API implementation
        search_template = "http://api.openweathermap.org/data/2.5/find?q={}&type=like&APPID={}"

        # WeatherUnderground (http://www.wunderground.com) API implementation
        # search_template = "http://api.wunderground.com/api/xxxxxxxxxxxxxxxxx/conditions/q/{}.json"

        search_url = search_template.format(self.search_input.text, OPEN_WEATHER_ID)
        request = UrlRequest(search_url, self.found_location)

    def found_location(self, request, data):

        # WeatherUnderground (http://www.wunderground.com) API implementation
        # data = json.loads(data.decode()) if not isinstance(data, dict) else data
        # cities = [ "{}-{}, ({})".format(d["city"], d["state"], d["country"]) for d in data["response"]["results"]]
        # self.search_results.item_strings = cities

        # OpenWeatherMap (http://openweathermap.org/) API implementation
        data = json.loads(data.decode()) if not isinstance(data, dict) else data
        # cities = ["{} ({})". format(d['name'], d['sys']['country']) for d in data['list']]
        cities = [(d['name'], d['sys']['country']) for d in data['list']]
        self.search_results.item_strings = cities

        # Python 3.x syntax
        #   self.search_results.adapter.data.clear()

        #   Python 2.7.x syntax
        del self.search_results.adapter.data[:]
        self.search_results.adapter.data.extend(cities)
        self.search_results._trigger_reset_populate()

    def args_converter(self, index, data_item):
        city, country = data_item
        return{'location': (city, country)}


class CurrentWeather(BoxLayout):
    global OPEN_WEATHER_ID

    location = ListProperty(["New York", "US"])
    conditions = StringProperty()
    temp = NumericProperty()
    temp_min = NumericProperty()
    temp_max = NumericProperty()
    conditions_image = StringProperty()

    def update_weather(self):
        weather_template = "http://api.openweathermap.org/data/2.5/" \
                           "weather?q={},{}&units=metric&appid="+OPEN_WEATHER_ID
        weather_url = weather_template.format(*self.location)
        request = UrlRequest(weather_url, self.weather_retrieved)

    def weather_retrieved(self, request, data):
        data = json.loads(data.decode()) if not isinstance(data, dict) else data
        self.conditions = data['weather'][0]['description']
        self.temp = data['main']['temp']
        self.temp_min = data['main']['temp_min']
        self.temp_max = data['main']['temp_max']
        self.conditions_image = "http://openweathermap.org/img/w/{}.png"\
            .format(data['weather'][0]['icon'])

class WeatherApp(App):
    pass


if __name__ == '__main__':
    WeatherApp().run()
