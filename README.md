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

## API Documentation

### Endpoint: `/generate-reply`

**Method:** `POST`

**Request Body:**
```json
{
  "emailText": "The email you want to reply to",
  "tone": "professional"
}
```

**Response:**
```json
{
  "reply": "Generated email reply text"
}
```

**Available Tones:**
- `professional`
- `friendly`
- `formal`
- `casual`
- `urgent`

## Configuration

### Environment Variables (`.env`)

```
GEMINI_API_KEY=your_api_key_here          # Required: Your Google Gemini API key
GEMINI_MODEL=gemini-2.5-flash             # Optional: Model to use (default: gemini-2.5-flash)
```

### Backend Server Settings

To run on a different port:
```bash
uvicorn main:app --reload --port 8080
```

## Testing Your Setup

Run the test script to verify your API key:
```bash
python test_api.py
```

Expected output:
```
✓ API key found
✓ Client initialized
✓ API call successful
✓ Your Gemini API key is working perfectly!
```

## Security Notes

- 🔒 Keep your `.env` file private - never commit it to GitHub
- 🔒 Never share your Gemini API key publicly
- 🔒 Add `.env` to `.gitignore` before pushing to GitHub

## Requirements

See `Backendpy/requirements.txt`:
- fastapi
- uvicorn
- python-dotenv
- google-genai
- pydantic

## Troubleshooting

### Extension doesn't appear in toolbar
- Reload the extension in `chrome://extensions/`
- Ensure Developer mode is enabled
- Check browser console for errors

### API connection failed
- Verify FastAPI server is running (`http://localhost:8000`)
- Check if port 8000 is available
- Ensure CORS middleware is enabled in `main.py`

### Invalid API key error
- Double-check your Gemini API key in `.env`
- Ensure there are no extra spaces or quotes
- Regenerate the key from Google AI Studio if needed

### Model not found error
- Ensure your Gemini API key has access to the selected model
- Run `list_models.py` to see available models:
  ```bash
  python list_models.py
  ```

## Future Enhancements

- [ ] Subject line generation
- [ ] Email length control (Short/Medium/Long)
- [ ] Draft history and saving
- [ ] Email sentiment analysis
- [ ] Multiple language support
- [ ] Custom prompt templates
- [ ] Dark mode for extension UI
- [ ] Settings panel for customization

## Contributing

Contributions are welcome! Feel free to fork, modify, and submit pull requests.

## License

This project is open source and available under the MIT License.

## Disclaimer

This tool is designed to help draft emails. Always review AI-generated content before sending. The authors are not responsible for any miscommunication or errors in generated emails.

## Support

For issues, questions, or suggestions:
1. Check the troubleshooting section above
2. Review the Google Gemini API documentation
3. Open an issue on GitHub

---

**Made with ❤️ using Google Gemini AI**
