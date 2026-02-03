# AI Email Reply Generator

A Chrome extension powered by Google Gemini AI that generates professional email replies with customizable tones. This tool helps you compose emails faster by leveraging advanced AI capabilities.

## Features

✨ **AI-Powered Reply Generation**
- Generate professional email responses instantly
- Powered by Google Gemini 2.5 Flash model

🎭 **Multiple Tone Options**
- Professional
- Friendly
- Formal
- Casual
- Urgent

⚡ **Quick Integration**
- Works directly in Gmail and other web-based email clients
- One-click reply generation and insertion

🔐 **Secure**
- API key stored locally in `.env` file
- No data sent to external servers except Google Gemini

## Tech Stack

**Backend:**
- Python 3.x
- FastAPI
- Google Gemini API (google-genai)
- python-dotenv for environment management

**Frontend:**
- Chrome Extension API
- HTML5, CSS3, JavaScript
- CORS-enabled for extension communication

## Project Structure

```
AI Email Generator/
├── Backendpy/
│   ├── main.py              # FastAPI server
│   ├── requirements.txt      # Python dependencies
│   ├── .env                  # Environment variables (API key)
│   └── __pycache__/
└── chromeextension/
    ├── manifest.json         # Extension configuration
    ├── popup.html            # Extension UI
    ├── popup.js              # Extension logic
    ├── content.js            # Content script
    └── style.css             # Extension styling
```

## Installation

### Prerequisites
- Python 3.8 or higher
- Google Chrome browser
- Google Gemini API key (get one at [Google AI Studio](https://aistudio.google.com))

### Backend Setup

1. **Clone or download the project:**
   ```bash
   cd "AI Email Generator/Backendpy"
   ```

2. **Create a `.env` file with your API key:**
   ```
   GEMINI_API_KEY=your_api_key_here
   GEMINI_MODEL=gemini-2.5-flash
   ```

3. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the FastAPI server:**
   ```bash
   uvicorn main:app --reload
   ```
   The server will run on `http://localhost:8000`

### Chrome Extension Setup

1. **Open Chrome Extensions Page:**
   - Go to `chrome://extensions/` in Chrome
   - Enable **Developer mode** (top right)

2. **Load the Extension:**
   - Click **"Load unpacked"**
   - Navigate to the `chromeextension` folder
   - Select and open the folder

3. **Verify Installation:**
   - The extension should appear in your Chrome toolbar
   - Ensure the backend server is running before using

## How to Use

1. **Open an email** in Gmail or any web-based email client
2. **Click the extension icon** in your Chrome toolbar
3. **Select a tone** for your reply (Professional, Friendly, Formal, etc.)
4. **Click "Generate Reply"** button
5. **Review the generated reply** in the text area
6. **Click "Insert Reply"** to add it to your email draft
7. **Send** the email as usual



## Future Enhancements

- [ ] Subject line generation
- [ ] Email length control (Short/Medium/Long)
- [ ] Draft history and saving
- [ ] Email sentiment analysis
- [ ] Multiple language support
- [ ] Custom prompt templates
- [ ] Dark mode for extension UI
- [ ] Settings panel for customization



## Disclaimer

This tool is designed to help draft emails. Always review AI-generated content before sending. The authors are not responsible for any miscommunication or errors in generated emails.


