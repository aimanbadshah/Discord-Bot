# 🤖 Discord Bot using Ollama AI

A **Discord bot** that can:

✅ Respond with a greeting (`/hello` command)  
✅ Answer user queries using **Ollama AI** (`/ask <message>` command)  
✅ Summarize the last 10 messages in a channel (`/summarize` command)  

---

## 🚀 Features
- Uses **discord.py** for bot interaction
- Integrates **Ollama AI** for intelligent responses
- Secure token storage with **environment variables**
- Summarizes recent messages in bullet points

---

## 📌 Installation

1️⃣ **Clone the repository**  
```bash
git clone https://github.com/aimanbadshah/Discord-Bot.git
cd Discord-Bot
```

2️⃣ **Create a virtual environment** (optional but recommended)  
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

3️⃣ **Install dependencies**  
```bash
pip install -r requirements.txt
```

4️⃣ **Set up environment variables**  
Create a `.env` file in the root folder and add:  
```ini
DISCORD_BOT_TOKEN=your_token_here
```

---

## 🔧 Usage

🟢 **Run the bot**  
```bash
python bot.py
```

💬 **Available Commands**  
| Command         | Description                        |
|----------------|--------------------------------|
| `/hello`       | Bot responds with a greeting |
| `/ask <text>`  | Bot replies using Ollama AI |
| `/summarize`   | Summarizes the last 10 messages in the channel |

---

## 🛠 Technologies Used
- **Python** 🐍  
- **Discord API (`discord.py`)** 🎤  
- **Ollama AI** 🤖  

---

## 📝 License  
This project is licensed under the **MIT License**.

👨‍💻 **Developed by [Aiman Badshah](https://github.com/aimanbadshah)**  
🌟 Star the repo if you like it! ⭐  
