<div align="center">
<img width="899" height="712" alt="image" src="https://github.com/user-attachments/assets/aba09d81-d63d-4501-8057-9855c88730c0" />

<div align="center">

  # 🎭 EmojiWhisperer (powered by demoji)

  ### **Stop staring at icons. Start reading the data.**
  
  <p>
    <img src="https://img.shields.io/badge/Python-3.7%2B-blue?style=for-the-badge&logo=python" />
    <img src="https://img.shields.io/badge/Library-demoji-ff69b4?style=for-the-badge" />
    <img src="https://img.shields.io/badge/Data-Clean-success?style=for-the-badge" />
  </p>

  <p>
    <a href="#-the-mission">The Mission</a> •
    <a href="#-how-it-works">How It Works</a> •
    <a href="#-usage">Usage</a>
  </p>

</div>

---

## 🚀 The Mission

Data science is hard enough without "🚀", "💎", and "🙌" messing up your tokenizers. **EmojiWhisperer** uses the `demoji` library to give you total control over how your Python scripts handle emojis. 

* **Scrubbing:** Delete them all to leave pure, clean text. 🧼
* **Translating:** Swap icons for their official Unicode descriptions. 📖
* **Discovery:** Find out exactly which emojis are hiding in your massive datasets. 🔍

---

## 🧠 How It Works

The `demoji` module doesn't just guess; it's a scholar of the Unicode Consortium.

1.  **The Registry:** It downloads a local mapping of every official emoji and its English description.
2.  **The Scan:** It utilizes optimized Regular Expressions (Regex) to find emoji patterns in your strings.
3.  **The Swap:** It replaces the high-byte characters with their text labels (e.g., "🐍" becomes ":python:").



---

## 🛠️ Installation

Get the library that speaks "Millennial" fluently:

```bash
pip install demoji
```

## ▶️ Usage
1. Initialize (The Handshake)
Before you start, you need to sync with the latest emoji codes:

import demoji
demoji.download_codes()

2. Replace Emojis with Text 🗣️
Turn those icons into actual words for your NLP models.

text = "Python is 🔥 and 🐍!"
clean_text = demoji.replace_with_desc(text, sep=" ")
# Result: "Python is fire and snake!"

3. Remove Emojis Entirely 🧹
For when you just want the emojis to go away forever.

text = "Wait, don't delete me! 😱😭"
boring_text = demoji.replace(text, "")
# Result: "Wait, don't delete me! "

4. Find All Emojis 🕵️‍♂️
Get a dictionary of every emoji used in a string.

demoji.findall("I love 🍕 and 🍺")
# Result: {'🍕': 'pizza', '🍺': 'beer mug'}

## 🤝 Contributing
Want to add more fun wrappers?

Fork this repo.

Add your flair.

Open a Pull Request! 🥳


<div align="center"> <sub>Because sometimes, a picture is NOT worth a thousand words. 🚫🖼️</sub> </div>
