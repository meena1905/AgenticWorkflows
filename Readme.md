# AI Dev Workflow Assistant

An AI-powered agent that assists developers with everyday coding tasks using the Groq API (free).

## Features

- **Code Understanding** — explains what any Python file does
- **Debugging** — finds bugs, logic errors, and bad practices
- **Documentation** — auto-generates Google-style docstrings
- **Test Generation** — writes pytest unit tests automatically
- **Auto Test Runner** — runs generated tests with pytest instantly
- **Report Generation** — saves all output as a clean markdown report

## Setup

1. Install dependencies:
   pip install -r requirements.txt

2. Create a `.env` file:
   GROQ_API_KEY=your-groq-key-here

   Get a free key at: https://console.groq.com

## Usage

  python agenticworkflow.py --file sample_code.py --mode explain
  python agenticworkflow.py --file sample_code.py --mode debug
  python agenticworkflow.py --file sample_code.py --mode document
  python agenticworkflow.py --file sample_code.py --mode test
  python agenticworkflow.py --file sample_code.py --mode all

## Output Files

| File | Description |
|------|-------------|
| `sample_code_documented.py` | Code with docstrings added |
| `sample_code_tests.py` | Generated pytest test file |
| `sample_code_report.md` | Full report of all results |

## Tech Stack

- Python 3.x
- Groq API (llama-3.3-70b-versatile)
- pytest


```

---

Your final folder:
````
Assignment-2/
├── agenticworkflow.py       
├── sample_code.py
├── requirements.txt
├── README.md            
└── .env
`````

Run it:
`````bash
python agenticworkflow.py --file sample_code.py --mode all
`````
