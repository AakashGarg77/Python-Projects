import requests, json
def getweather(url):
    r = requests.get(url).text
    parsed = json.loads(r)

    # LOCATION
    name = parsed["location"]["name"]
    state = parsed["location"]["region"]
    country = parsed["location"]["country"]
    print(f"Name: {name} | State: {state} | Country: {country}")

    # CURRENT CONDITIONS
    temp = parsed["current"]["temp_c"]
    wind = parsed["current"]["wind_kph"]
    humidity = parsed["current"]["humidity"]
    updated = parsed["current"]["last_updated"]
    print(f"Temperature: {temp} Degree Celsius | Wind_Speed: {wind}kph | Humidity: {humidity} | Updated_On: {updated}")


if __name__ == '__main__':
    while True:
        print("Welcome To The Realtime Weather App".center(100, '-'))
        user = input(f"Enter your city here:\n").lower()
        try:
            url = "https://api.weatherapi.com/v1/current.json?key=ef520b63c2de40c78f0181127222802&q=" + user + "&aqi=yes"
            getweather(url)
        except Exception as e:
            print(e)

        inp = input("Type c to continue and q to quit:\n")
        if inp=="c":
            continue
        else:
            quit()