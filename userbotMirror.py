import asyncio
from pyrogram import Client, filters

api_id = "YOUR_API_ID"
api_hash = "YOUR_API_HASH"
bot_token = "YOUR_TOKEN"

## I use two client instances in this script
## "app" is my account, since this one has access to the messages
app = Client("my_account", api_id, api_hash)

## "bot" is the bot i use to send the messages, since it won't get banned
## or rate-limited
bot = Client(
    "my_bot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token,
)

## Your targets from where you want to get the messages from
## You can get the IDs from web telegram, just add a 100 before it
TARGET = [-1001222227215, -1003333333893, -1004444444713]


## Where you want to send the messages
DESTINATION = -1001000000396


@app.on_message(filters.chat(TARGET))
async def echo(client, message):
    ## Here i use index to send to a chat with different topics
    ## If you aren't using topics, removed the index variable and "reply_to_message_id" in bot.send_message
    index = TARGET.index(message.chat.id) + 2
    await bot.send_message(
        DESTINATION,
        text=message.text,
        entities=message.entities,
        disable_web_page_preview=True,
        reply_to_message_id=index,
    )


if __name__ == "__main__":
    import asyncio

    # Run both clients concurrently
    app.start()
    bot.start()
    print("Both clients have been started!")

    # Here we keep the script running
    asyncio.get_event_loop().run_forever()
