import platform
import subprocess
import time

website = input("Please enter your website domain: ")


def ping(host):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", host]
    return subprocess.call(command) == 0


if __name__ == "__main__":
    while True:
        print(ping(website))
        time.sleep(600)
