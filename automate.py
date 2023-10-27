import time
import validators
import requests


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
