from app.discord_bot.discord_api import client, discord_token

#God statement that ensures code is only run if this file run directly and is not called as an imported module.
if __name__ == '__main__':
    client.run(discord_token)