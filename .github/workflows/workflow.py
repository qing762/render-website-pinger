import validators
import requests


def ping(host):
    if validators.url(host) == True:
        r = requests.get(host)
        return r.status_code
    else:
        exit(
            f"Invalid URL '{host}': No scheme supplied. Perhaps you meant http://{host}?"
        )


if __name__ == "__main__":
    print(ping("https://qing-website.onrender.com/"))
    exit()
