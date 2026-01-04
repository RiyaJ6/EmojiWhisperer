import demoji

emoji_text = """The demoji module is a Python library that helps you remove emojis from a string of text efficiently. 🚫😊🔤 It allows you to clean up text by replacing emojis with nothing or a placeholder, making it easier to process and analyze text data. 🧹📊💻 When you import the demoji module, you can use the demoji.replace() function to remove emojis from any given text. 🆓📉🔧

To use the module, you first need to download the emoji database, which demoji will reference to find all emojis. 🌍🗂️💾 After that, you can call the replace() method, which will go through the text and remove any emoji characters it detects. 🔍🚫💬 This makes it super useful when you're processing data that contains emojis, like social media posts or chat messages. 📱📝🎯"""

demoji.findall(emoji_text)
