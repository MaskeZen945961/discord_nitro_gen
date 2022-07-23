import random
import string
from discord_webhook import DiscordWebhook
import time

def wait(seconds):
    time.sleep(seconds)


def main():
    webhock = input ("Webhook: ") 

    while True:
        code = "".join(random.choices(
        string.ascii_uppercase + string.digits + string.ascii_lowercase,
        k = 16
        ))
        print(f"https://discord.gift/{code}\n")
        webhook = DiscordWebhook(webhock, content=f"https://discord.gift/{code}")
        response = webhook.execute()
        wait(1) #wait 1 seconde before sending the next message delete this if you want to send the message instantly (bug)


main()
