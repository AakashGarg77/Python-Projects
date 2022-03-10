# State Wise
import json, requests
from plyer import notification
import time

def getnotify(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "C:\\Users\\Aakash Garg\\PycharmProjects\\Python Projects\\favicon.ico",
        timeout = 0
    )


def getcovid19details(url):
    r = requests.get(url).text
    parsed = json.loads(r)
    for i in parsed["statewise"][1:6]:
        state = i["state"]
        statecode = i["statecode"]
        active = i["active"]
        confirmed = i["confirmed"]
        recovered = i["recovered"]
        deaths = i["deaths"]
        print(f"State: {state} | StateCode: {statecode} | Active: {active} | Confirmed: {confirmed} | Recovered: {recovered} | Deaths: {deaths}")
        title = "Covid-19 Notification System"
        message = f"\nState: {state} \nStateCode: {statecode} \nActive: {active} \nConfirmed: {confirmed} \nRecovered: {recovered} \nDeaths: {deaths}"
        getnotify(title, message)
        time.sleep(8)


if __name__ == '__main__':
    print("Welcome To The Covid-19 Notification System".center(100, '-'))
    url = "https://data.covid19india.org/data.json"
    getcovid19details(url)