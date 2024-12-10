import gradio as gr
import torch
import time
import json
import requests

# NOTE: ollama must be running for this to work, start the ollama app or run `ollama serve`
model = "llama3.3"  # TODO: update this for whatever model you wish to use


def prime_thread(message, history):
    if len(history) == 0:
        history.append({
        "role": "system",
        "content": "You are a friendly chatbot. and you short answers.",
    })
    history.append({"role": "user",
                    "content": message})
    
    history.append({"role": "assistant",
                     "content": ''})
    r = requests.post(
            "http://0.0.0.0:11434/api/chat",
            json={"model": model, "messages": history, "stream": True}, stream=True)
    r.raise_for_status()
    output = ""
    # for the visualization
    for line in r.iter_lines():
        time.sleep(0.01)
        body = json.loads(line)
        if "error" in body:
            raise Exception(body["error"])
        if body.get("done") is False:
            message = body.get("message", "")
            content = message.get("content", "")
            output += content
            # the response streams one token at a time, print that as we receive it
            print(content, end="", flush=True)
            yield output

        if body.get("done", False):
            history[-1]["content"] = output
            yield output
        
CSS = """
.contain { display: flex; flex-direction: column; }
.gradio-container { height: 100vh !important; }
#component-0 { height: 100%; }
#chatbot { flex-grow: 1; overflow: auto;}
"""

with gr.Blocks(css=CSS) as demo:
    chatbot = gr.ChatInterface(prime_thread, type="messages")

def authenticate(username, password):
    if username == "user" and password == "passwd":
        return True
        
    else:
        return False

if __name__ == "__main__":
    demo.launch(auth=authenticate, server_name="0.0.0.0", server_port=7860)#, share=True)
