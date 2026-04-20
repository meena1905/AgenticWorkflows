# AI Dev Workflow Assistant

> AI-powered CLI tool to explain, debug, document, and test any Python file — using the free Groq API.

---

## Modes

| Mode | What It Does |
|------|-------------|
| `explain` | Plain-English breakdown of the code |
| `debug` | Finds bugs, logic errors, bad practices |
| `document` | Injects Google-style docstrings |
| `test` | Generates pytest unit tests |
| `all` | Runs all modes + saves a report |

---

## Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Get a free Groq API key

Sign up at [console.groq.com](https://console.groq.com) — it's free.

### 3. Create your `.env` file

```env
GROQ_API_KEY=your-groq-key-here
```

> ⚠️ Never commit your `.env` file. Add it to `.gitignore`.

---

## Usage

```bash
python agenticworkflow.py --file sample_code.py --mode explain
python agenticworkflow.py --file sample_code.py --mode debug
python agenticworkflow.py --file sample_code.py --mode document
python agenticworkflow.py --file sample_code.py --mode test
python agenticworkflow.py --file sample_code.py --mode all
```

You can pass any Python file:

```bash
python agenticworkflow.py --file your_script.py --mode debug
```

---

## Project Structure

```
Assignment-2/
├── agenticworkflow.py    # Main agent script
├── sample_code.py        # Sample Python file to analyze
├── requirements.txt      # Python dependencies
├── README.md             # This file
└── .env                  # Your Groq API key (not committed)
```

---

## Output Files

| File | Description |
|------|-------------|
| `sample_code_documented.py` | Code with Google-style docstrings added |
| `sample_code_tests.py` | Auto-generated pytest test file |
| `sample_code_report.md` | Full markdown report of all results |

---

## Running the Generated Tests

```bash
pytest sample_code_tests.py -v
```

`--mode all` also runs tests automatically and includes results in the report.

---

## Tech Stack

- **Python 3.x**
- **[Groq API](https://console.groq.com)** — `llama-3.3-70b-versatile` (free tier)
- **python-dotenv** — loads `.env` credentials
- **pytest** — runs auto-generated tests

---

## Requirements

```
groq
python-dotenv
pytest
```

---

## Notes

- Code is sent to the Groq API — avoid using with sensitive or proprietary files.
- Cleaner input code produces better results.
- `document` mode only adds docstrings — your logic is never changed.

---

## License

MIT — free to use, modify, and distribute.
