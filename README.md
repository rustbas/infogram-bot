# Infogram Bot

> [!WARNING]
> Your username will be saved in the bot logs.

Simple bot for fast identifying chat metadata, for further using it in
different services (e.g. Zabbix, Jenkins, Github Actions, etc).

## How to start a bot

First of all, you need to get token from [botFather](https://t.me/BotFather). 
You can register for it next commands:
- `help` — print help message;
- `getinfo` — get info about current chat.

After that you need to start a bot.

### Pull docker image from DockerHub

```console
foo@bar:~$ docker run --rm -d -e TELEGRAM_TOKEN=[YOUR TELEGRAM BOT TOKEN] wtukatyr/infogram-bot
```

### Build docker locally

In root directory:

```console
foo@bar:~/infogram-bot$ docker build -t infogram-bot .
foo@bar:~/infogram-bot$ docker run --rm -d -e TELEGRAM_TOKEN=[YOUR TELEGRAM TOKEN] infogram-bot
```

### Run python script

If you can't (or don't want to) run a docker container.

```console
foo@bar:~/infogram-bot$ python3 -m venv venv
foo@bar:~/infogram-bot$ source venv/bin/activate
foo@bar:~/infogram-bot$ pip install -r requirements.txt
foo@bar:~/infogram-bot$ export TELEGRAM_TOKEN=[YOUR TELEGRAM BOT TOKEN]
foo@bar:~/infogram-bot$ python3 main.py
```

## Usage

1. Add your bot to the right chat.
2. Run `/getinfo` command. It will return information, that you can use in
   different notification services.
