# gradio_with_ollama
gradio chat service

# Useage
```shell
python gradio_chat.py
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