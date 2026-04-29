# 👋 goodbye-but-make-it-tech

> 💼 Quit my job. Built a chatbot.

On my last day at my first job, instead of sending a boring farewell email, I built a **personalised farewell chatbot** for my teammates. Each colleague could enter the last 4 digits of their phone number and receive a custom goodbye message written just for them. Because some goodbyes deserve to be special. 🥹

---

## 💡 The Story

It was my last day at my first company — a place I genuinely loved. I wanted to say goodbye in a way that was memorable, personal, and a little unexpected. So instead of a generic farewell email, I spent my last few days building this chatbot and writing a personal message for every single teammate.

The result? The most memorable resignation ever. 😄

---

## 🚀 Features

- **Personalised messages** — Each person gets a unique message written just for them
- **Phone number based lookup** — Enter last 4 digits of your phone number to get your message
- **Dialogflow NLP** — Natural conversation flow powered by Google Dialogflow
- **Private messages** — Personal messages stored locally in a CSV, never pushed to GitHub 🔒

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Flask |
| NLP | Google Dialogflow |
| Deployment | Google App Engine |
| Data | CSV file (local only) |

---

## 📁 Project Structure

```
Demo2/
│
├── templates/
│   └── base.html        # Main page with Dialogflow chat widget
│
├── main.py              # Flask app & Dialogflow webhook
├── messages.csv         # Personal messages (local only, never pushed)
├── app.yaml             # Google App Engine config
├── requirements.txt     # Python dependencies
├── .env.example         # Environment variable template
├── .gitignore
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/VamikaShrivastava/goodbye-but-make-it-tech.git
cd goodbye-but-make-it-tech
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up environment variables

Create a `.env` file based on `.env.example`:
```
DIALOGFLOW_AGENT_ID=your_dialogflow_agent_id
```

### 4. Create your `messages.csv`

Create a `messages.csv` file in the root directory:
```
phone,message
1234,Thank you for everything. It was a pleasure working with you!
5678,You were the best part of this journey. Stay in touch!
```

### 5. Run the app locally
```bash
python main.py
```

---

## 🔒 Privacy

Personal messages are stored in a local `messages.csv` file which is listed in `.gitignore` and **never pushed to GitHub**. This keeps all private messages safe and off the internet.

---

## ☁️ Deployment

Configured for **Google App Engine**. To deploy:
```bash
gcloud app deploy
```

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

> *"The most memorable resignation email was not an email at all."* 😄
