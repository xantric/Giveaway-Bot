from bot import GiveawayBot

VERSION = '0.0.1'

def main():
    bot=GiveawayBot()
    @bot.check
    def check_commands(ctx):
        return ctx.guild is not None
    bot.run(VERSION)


if __name__ == "__main__":
    main()