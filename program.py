import requests
from dotenv import load_dotenv
from os import getenv as os_getenv
import json
import time
import configparser
import os
import pyperclip
from pystyle import Colorate, Colors

# TODO: Split the code in functions so it's easier to read.


def main():
    if not os.path.exists('.env'):
        with open('.env', 'w') as f:
            f.write("ACCOUNT_TOKEN=YOUR_TOKEN_HERE")
        print(Colorate.Diagonal(Colors.black_to_red, "Put your token in .env!", 1))
        time.sleep(9999)
        exit()
    cfg = configparser.ConfigParser()
    cfg.read('config.ini')
    # Initalization values. Don't modify unless you know what you're doing - edit config.ini instead
    load_dotenv('.env')
    TOKEN = os_getenv('ACCOUNT_TOKEN')
    if TOKEN == "YOUR_TOKEN_HERE":
        print(Colorate.Diagonal(Colors.black_to_red, "Put your token in .env!", 1))
        time.sleep(9999)
        exit()
    scanned = set()
    ids = set()
    current_lenght = 0
    cooldown = cfg.getfloat('scraper', 'cooldown')
    ping_message = ""
    limit = 50

    # Beginning of actual code here

    channelid = int(input(Colorate.DiagonalBackwards(Colors.cyan_to_blue, "Enter channel id: ", 1)))
    headers = {
        'accept': '*/*',
        'authorization': TOKEN,
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'x-debug-options': 'bugReporterEnabled',
        'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE1MTYzOCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0='}

    r = requests.get(
        f'https://discord.com/api/v9/channels/{channelid}/messages?limit=100', headers=headers)
    data = json.loads(r.text)
    print("\n")
    for info in data:
        try:
            if current_lenght > 2000:
                break
            else:
                userid = info['author']['id']
                username = info['author']['username']
                discrim = info['author']['discriminator']
                messageid = int(info['id'])
                # The 3 stands for <@>, because example id is <@5125125125>
                current_lenght = len(userid) + 3
                if userid not in scanned:
                    print(Colorate.Vertical(Colors.blue_to_cyan, f"Found username: {username}{discrim}, with id of {userid}. Adding to list..."))
                    scanned.add(userid)
                    ids.add(str(userid))
                else:
                    continue
        except Exception as e:
            print(Colorate.Vertical(Colors.blue_to_cyan, f"Exception occured: {e}", 1))
            break

    for i in range(limit):
        try:
            r = requests.get(
                f'https://discord.com/api/v9/channels/{channelid}/messages?limit=100&before={messageid}', headers=headers)
            data = json.loads(r.text)
            print("\n\n\n\n\n\n\n\n")
        except KeyboardInterrupt:
            break
        for info in data:
            try:
                if current_lenght > 2000:
                    break
                userid = info['author']['id']
                username = info['author']['username']
                discrim = info['author']['discriminator']
                messageid = int(info['id'])
                # The 3 stands for <@>, because example id is <@5125125125>
                current_lenght += len(userid) + 3
                if userid not in scanned:
                    print(Colorate.Vertical(Colors.blue_to_cyan, f"Found username: {username}{discrim}, with id of {id}. Adding to list..."))
                    scanned.add(userid)
                    ids.add(str(userid))
                else:
                    continue
            except (KeyboardInterrupt, Exception) as e:
                print(Colorate.Vertical(Colors.blue_to_cyan, f"Exception occured: {str(e)}", 1))
                if e == KeyboardInterrupt:
                    break
                break
            time.sleep(0.01)

    for user_identification in ids:
        ping_message += "<@" + user_identification + ">"

    print(ping_message)
    choice = input(Colorate.Diagonal(Colors.green_to_cyan, "Do you want to copy the message to your clipboard? (y/n): ", 1))
    if choice.lower() == "y" or choice.lower() == "yes":
        pyperclip.copy(ping_message)
        print(Colorate.Diagonal(Colors.green_to_cyan, "Copied to clipboard", 1))
        time.sleep(9999)
        exit()

    else:
        print(Colorate.Diagonal(Colors.green_to_cyan, "Ok, bye. Make em' suffer!", 1))
        time.sleep(9999)
        exit()


if __name__ == '__main__':
    main()
