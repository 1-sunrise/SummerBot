import interactions
from interactions import (
    Client,
    Intents,
    slash_command,
    SlashContext,
    OptionType,
    slash_option,
    check,
    is_owner,
    integration_types,
)

BOT_TOKEN = open("token.txt", "r").read().strip()

bot = Client(intents=Intents.ALL, basic_logging=True)


# Print bot status
@interactions.listen()
async def on_startup():
    print("SummerBot is ready")


# Slash commands
@slash_command(name="say", description="Makes the bot say what you want it to say:")
@integration_types(user=True)
@check(is_owner())
@slash_option(
    name="text",
    description="Adds text",
    required=False,
    opt_type=OptionType.STRING,
)
async def channel_function(ctx: SlashContext, text: str = None):
    if not text:
        print("ERROR: Please select an option")
        await ctx.send("ERROR: Please select an option", ephemeral=True)
    elif text:
        print("Sent: " + text)
        await ctx.send(text)


# Start bot
if __name__ == "__main__":
    bot.start(BOT_TOKEN)
