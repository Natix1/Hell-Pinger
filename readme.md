# Hell-Pinger
*Create messages to ping alot of people*

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Tested on Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white) ![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?style=for-the-badge&logo=discord&logoColor=white)

## How to use

If you haven't, install [Python](https://www.python.org/downloads/). Make sure to check the **add to path** box.

*Optional: create an envinorment*

Open a [command prompt](https://www.makeuseof.com/tag/a-beginners-guide-to-the-windows-command-line/), if needed navigate to the download folder and type `pip install -r requirements.txt`. This will install the dependencies.

*Optional: edit config.ini to adjust settings*

Now, in the command prompt type `python program.py`.

# Errors

1. `requests` error, `discord.py` or similar: Double check the token to make sure its correct. 
2. `os` error, `discord.py`, `requests` or similar: If a `.env` file wasn't created, create it manually in the same directory the rest of files are placed. then put this in the folder: `ACCOUNT_TOKEN=YOUR_TOKEN_HERE` and replace the `YOUR_TOKEN_HERE` with your actual discord token.
3. `discord.py` error, `requests` error: **__By saying token I mean the account token. I didn't test it on a bot token but im 90% sure it won't work.__**
4. 
