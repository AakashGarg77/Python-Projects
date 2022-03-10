from plyer import notification
import time


def notify_user(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon="C:\\Users\\Aakash Garg\\PycharmProjects\\Python Projects\\Health Reminder Notification System\\health.ico",
        timeout=1
    )


if __name__ == '__main__':
    water = 10
    eyes = 20
    physical = 30

    water_time = time.time()
    eyes_time = time.time()
    physical_time = time.time()
    title = "Health Reminder Notification System"
    while True:
        if time.time() - water_time > water:
            notify_user(title, "It's right time to drink water...")
            water_time = time.time()
        elif time.time() - eyes_time > eyes:
            notify_user(title, "It's right time to rest your eyes...")
            eyes_time = time.time()
        elif time.time() - physical_time > physical:
            notify_user(title, "It's right time to do some physical...")
            physical_time = time.time()