class Weather():
    def __init__(self, d, m, y, minTemp, maxTemp,s ):

        self.date = {'day': d , 'month': m, 'year': y}
        self.minTemp = minTemp
        self.maxTemp = maxTemp
        self.sky = s
        self.avgTemp = (self.minTemp + self.maxTemp) / 2

    def __str__(self):
        return f'WHEATHER:{self.date["day"] }-{self.date[ "month" ]}-{self.date[ "year" ]} TempMin:{self.minTemp }C TempMax:{self.maxTemp }C TempAvg:{self.avgTemp }C Sky:{self.sky}.'

    def __gt__(self, value):
        return self.maxTemp > value.maxTemp

    def __eq__(self, value):
        return self.avgTemp == value.avgTemp and self.sky == value.sky

today_weather = Weather('17', '8', '2020', 18, 30, 'clear')
tomorow_weather = Weather('18', '8', '2020', 19, 31, 'clear')
print(today_weather)
print(tomorow_weather)

if today_weather > tomorow_weather:
    print("today is hotter than it will be tomorow")
else:
    print("toomorow is hotter than it today")

if today_weather == tomorow_weather:
    print("the weather tomorow will be like todays")
