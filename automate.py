import time
import requests
import validators
from flask import Flask
from threading import Thread

app = Flask("/")


@app.route("/")
def home():
    return "Hello World!"


def run():
    app.run(host="0.0.0.0", port=8080)  # 127.0.0.1 or ::


def keep_alive():
    t = Thread(target=run)
    t.start()


def ping(host):
    if validators.url(host) is True:
        r = requests.get(host)
        return r.status_code
    else:
        exit(
            f"Invalid URL '{host}': No scheme supplied. Perhaps you meant http://{host}?"
        )


if __name__ == "__main__":
    while True:
        print(ping("https://qing-website.onrender.com/"))
        time.sleep(600)
        keep_alive()
