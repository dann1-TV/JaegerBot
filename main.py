#!/usr/bin/env python

import bot
import sys

if __name__ == '__main__':
    bot_token = sys.argv[1]
    bot.run_discord_bot(bot_token)
