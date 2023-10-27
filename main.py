import time
import validators
import requests

website = input("Please enter your website domain: ")


def ping(host):
    if validators.url(host) == True:
        r = requests.get(host)
        return r.status_code
    else:
        exit(
            f"Invalid URL '{host}': No scheme supplied. Perhaps you meant http://{host}?"
        )


if __name__ == "__main__":
    while True:
        print(ping(website))
        time.sleep(600)
