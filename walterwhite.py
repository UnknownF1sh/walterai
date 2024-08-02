import ollama

olmc = ollama.Client(host='http://sheepdog-profound-herring.ngrok-free.app')

def gen_response(message):
    
    response = olmc.chat(
    model="UnknownFish/waltergpt",
    messages=[
    {
    'role': 'user',
    'content': message,
    },]
    )
    return response