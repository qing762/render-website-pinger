import platform
import subprocess
import time
import validators
import requests

website = input("Please enter your website domain: ")


def ping(host):
    if validators.url(host) == True:
        r = requests.get(host)
        print(r.status_code)
        host = host.replace("https://", "").rstrip("/")
        param = "-n" if platform.system().lower() == "windows" else "-c"
        command = ["ping", param, "1", host]
        return subprocess.call(command) == 0
    else:
        exit(f"Invalid URL '{host}': No scheme supplied. Perhaps you meant http://{host}?")


if __name__ == "__main__":
    while True:
        print(ping(website))
        time.sleep(600)
