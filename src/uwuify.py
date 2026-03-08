import re
import random
import sys

def probability(p: float) -> bool:
    return random.random() < p

def emoticon(text: str) -> str:
    emoticons = (
        ":3",
        ">w<",
        ">~<",
        "(˶˃ ᵕ ˂˶) .ᐟ.ᐟ",
        "(◜௰◝)",
        ">3<",
        ">//<",
        "(ꈍᴗꈍ)",
        "^•ﻌ•^",
        "(`･ω･´)",
        "(☼◡☼)",
        "°ω°",
        "UwU",
        "OwO",
        "rawr xd",
        "^-^",
        "😳",
        "🥺",
        "👉👈",
        "🥺 👉👈",
        "<3",
        "nyaa~",
        "mya",
        "nyah!",
        "nya!",
        " (✿oωo)",
    )

    repl = lambda txt: f"{txt.group(1)} {random.choice(emoticons)} "\
            if probability(1/3) else txt.group(0)
    text = re.sub(r"([!?,.~])\s", repl, text)
    text += random.choice(emoticons) if probability(1/3) else ""
    return text

def tilde(text: str) -> str:
    repl = lambda txt: "~ " if probability(0.5) else txt.group(0)
    text = re.sub(r"[.]", repl, text)
    text = re.sub(r"[!]", f"{'~'*random.randint(1,3)} ", text)
    return text

def stutter(text: str) -> str:
    def repl(match) : return f"{match.group(1)}-{match.group(1)}"\
        if probability(1/12) else match.group(0)
    return re.sub(r"\b(\w)", repl, text)

def nyaify(text: str) -> str:
    raise NotImplementedError

def replace(text: str) -> str:
    pointers: dict[str, str|tuple] = {
        "small" : "smol",
        "you" : "u",
        "hello" : ("hai", "haiii","hiii", "hello"),
        "love" : "luv",
        "what" : ("what", "nani??"),
        "meow" : "nyaa~",
        "stupid" : "baka",
    }  

    for word, new_word in pointers.items():
        if isinstance(new_word, str):
            text = re.sub(rf"{word}", rf"{new_word}", text)
        elif isinstance(new_word, tuple| list):
            text = re.sub(rf"{word}", rf"{random.choice(new_word)}", text)

    text = re.sub(r"[lr]", "w", text)
    return text

def uwuify(text: str) -> str:
    text += " "
    text = text.lower()
    text = replace(text)
    text = stutter(text)
    text = tilde(text)
    text = emoticon(text)
    return text
        
args = sys.argv[1:]
if len(args) == 0:
    print("Usage: uwuify <text to uwuify>")
    sys.exit(1)
uwuified = uwuify(" ".join(args))
print(uwuified)