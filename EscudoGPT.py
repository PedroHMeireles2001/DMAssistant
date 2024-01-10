import dotenv
import time
from openai import OpenAI
from playsound import playsound

dotenv.load_dotenv()
client = OpenAI()


def getResponse(thread,content):
    client.beta.threads.messages.create(
        thread,
        role="user",
        content=content
    )

    run = client.beta.threads.runs.create(
        thread_id=thread,
        assistant_id="asst_0u3GRnVJRPNSZMPkBb7cnAqR"
    )
    while run.status != "completed":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread,
            run_id=run.id
        )
        time.sleep(1)

    thread_messages = client.beta.threads.messages.list(thread)
    return thread_messages.data[0].content[0].text.value


def start():
    thread = client.beta.threads.create()
    msg = ""
    print(thread)
    while msg != "exit":
        msg = input("> ")
        gptmsg= getResponse(thread.id,msg)
        print(gptmsg)
        response = client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=gptmsg
        )
        response.stream_to_file("audio.mp3")
        playsound('audio.mp3')
    client.beta.threads.delete(thread.id)

if __name__ == "__main__":
    start()