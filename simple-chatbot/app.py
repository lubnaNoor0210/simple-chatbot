import chainlit as cl

# on_message is a built in decorator that takes new message from the user.
@cl.on_message 
async def main(message: cl.Message):

    response = f"You said: {message.content}"
    await cl.Message(content=response).send()


    
    
