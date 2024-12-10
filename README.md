# gradio_with_ollama
gradio chat service

# Useage
```shell
python ollama_chat_gradio.py
```

# Authenticate
- Insert user id and passwd
```python
def authenticate(username, password):
    if username == "user" and password == "passwd":
        return True
        
    else:
        return False

```