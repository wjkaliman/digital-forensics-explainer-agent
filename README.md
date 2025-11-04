## 🕵️‍♂️ Digital Forensics Explainer Agent

A modular, Streamlit-based tool that parses digital forensic artifacts and explains them using Azure OpenAI. Built to help DFIR professionals, students, and educators understand complex forensic data with clarity and speed.

---

### 🚀 Features

- **Modular Tabs** for parsing:
  - `$MFT` (Master File Table)
  - `USBSTOR` (USB device history)
  - `AmCache` (application execution traces)
  - Event Logs (coming soon!)
- **One-click Parsing** of raw artifact text into structured JSON
- **Azure Agent Integration** for natural language explanations of parsed data
- **Streamlit UI** with real-time feedback, loading spinners, and copy-ready prompts
- **Sample Inputs** for quick testing and demos

---

### 🧰 Tech Stack

| Component        | Description                             |
|------------------|-----------------------------------------|
| Python           | Core scripting and parsing logic        |
| Streamlit        | Interactive web UI                      |
| Azure OpenAI     | Agent-based explanations via API        |
| GitHub           | Version control and collaboration       |

---

### 🛠️ Setup Instructions

1. **Clone the repo**

```bash
git clone https://github.com/wjkaliman/digital-forensics-explainer-agent.git
cd digital-forensics-explainer-agent
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Add your Azure credentials**

Create a `.streamlit/secrets.toml` file (excluded from Git) with:

```toml
AZURE_OPENAI_API_KEY = "your-azure-api-key"
AZURE_OPENAI_ENDPOINT = "https://your-endpoint.openai.azure.com/"
AZURE_OPENAI_DEPLOYMENT = "your-deployment-name"
```

4. **Run the app**

```bash
streamlit run app.py
```

---

### 📂 Project Structure

```
├── app.py                     # Main Streamlit app
├── parsers/                  # Modular artifact parsers
│   ├── parse_mft.py
│   ├── parse_usb.py
│   └── parse_amcache.py
├── .streamlit/
│   └── secrets.toml          # (local only, not committed)
├── requirements.txt
└── README.md
```

---

### 🎯 Use Cases

- 🧑‍🏫 **Educators**: Demonstrate forensic artifact interpretation in real time
- 🧑‍💻 **Analysts**: Quickly parse and explain artifacts during investigations
- 🧪 **Learners**: Understand how forensic data maps to real-world activity

---

### 🤝 Contributing

Pull requests are welcome! If you’d like to add new artifact types, improve parsing logic, or enhance the UI, feel free to fork and submit a PR.

---


### 📢 Acknowledgments

Built with ❤️ by [@wjkaliman](https://github.com/wjkaliman) to make digital forensics more accessible, explainable, and collaborative.

---

Would you like me to help you add a screenshot, write a `requirements.txt`, or generate a `LICENSE` file next?
