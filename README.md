![1](https://user-images.githubusercontent.com/52669201/212093165-1daf18e4-5713-4a83-a1ce-a6b53db551c3.png)
Telegram bot that generates responses using chat gpt. Easy to expand. All code is written according to the concept of OOP


# Instalation

#### Change important information in config
1. edit ```src/config.py```

#### Install requirements
2. ```pip install -r requirements.txt```

### Final (star program)
3. ```python3 src/main.py```

Well done!


# Structer
```
📦src
 ┣ 📂handlers
 ┃ ┣ 📜__init__.py
 ┃ ┗ 📜user.py
 ┣ 📂service
 ┃ ┣ 📜ChatGPT.py
 ┃ ┣ 📜__init__.py
 ┃ ┗ 📜animation.py
 ┣ 📜config.py
 ┗ 📜main.py
 ```
 
 
### Iformation


```
📦src - stock way

📂handlers - message handling methods
┗📜user.py - main message handling method

📂service - communication methods: bd, generators.
┗📜ChatGPT.py - crutch for convenient work with api chatgpt (create an object)
┗📜animation.py - animations in the bot. Very convenient to use, designed to offload the load

📜config.py - config or strings all static variables are stored here
📜main.py - main method (used to run)
```
