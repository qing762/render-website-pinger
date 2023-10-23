> **Warning**
> Please be advised that usage of this tool is entirely at your own risk. I assumes no responsibility for any adverse consequences that may arise from its use, and users are encouraged to exercise caution and exercise their own judgment in utilizing this tool.

# Render-Website-Pinger

Ping a website hosted on [Render](https://render.com) every 10 minutes to avoid website spinning down. (for free plan)

# Why?

([Source](https://render.com/docs/free#free-web-services)) Render spins down a free web service that goes 15 minutes without receiving inbound traffic. Render spins the service back up whenever it next receives a request to process.

Spinning up a service takes a few seconds, which causes a noticeable delay for incoming requests until the service is back up and running. For example, a browser page load will hang momentarily. 


## Installation / Usage

Clone the project

```bash
  git clone https://github.com/qing762/Render-Website-Pinger
```

Go to the project directory

```bash
  cd Render-Website-Pinger
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python main.py
```


# Automation

To automate it, instead of running `main.py`, run `automate.py`



## Contributing

Contributions are always welcome!

To contribute, fork this repository and improve it. After that, press the contribute button.



## Feedback / Issues

If you have any feedback or issues running the code, please reach out to me at [Discord/chaeyo_0](https://discord.com/users/635765555277725696)