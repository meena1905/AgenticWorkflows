"""
AI Dev Workflow Assistant
=========================================
An AI agent that assists in development workflows:
  - Code understanding
  - Debugging
  - Documentation generation
  - Test generation + auto-run

Usage:
  python assignment2.py --file <your_file.py> --mode explain
  python assignment2.py --file <your_file.py> --mode debug
  python assignment2.py --file <your_file.py> --mode document
  python assignment2.py --file <your_file.py> --mode test
  python assignment2.py --file <your_file.py> --mode all

Setup:
  pip install -r requirements.txt
  Create a .env file with: GROQ_API_KEY=your-key-here
"""

import os
import sys
import argparse
import subprocess
from datetime import datetime
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

def get_client():
    key = os.getenv("GROQ_API_KEY")
    if not key:
        print("ERROR: GROQ_API_KEY not set.")
        print("Add it to a .env file: GROQ_API_KEY=your-key-here")
        sys.exit(1)
    return Groq(api_key=key)

def read_file(path):
    if not os.path.exists(path):
        print(f"ERROR: File '{path}' not found.")
        sys.exit(1)
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def ask_groq(client, task, code, filename):
    prompts = {
        "explain": f"""You are an expert software engineer.
Explain the following code from '{filename}' clearly.
Cover: what it does, key functions/classes, inputs, outputs, and any important notes.
``````````python
{code}
`````````""",

        "debug": f"""You are an expert Python debugger.
Analyse the following code from '{filename}'.
Identify all bugs, logic errors, edge cases, and bad practices.
For each issue: describe the problem, where it occurs, and provide a corrected code snippet.
````````python
{code}
```````""",

        "document": f"""You are a technical documentation writer.
Add clear Google-style docstrings to every function and class in '{filename}' that is missing one.
Return the COMPLETE updated file with all original code preserved.
``````python
{code}
`````""",

"test": f"""You are a Python testing expert.
Write comprehensive pytest unit tests for all functions and classes in '{filename}'.
Cover happy paths, edge cases, and error/exception cases.
IMPORTANT: Use the exact exception types raised in the actual code. For example, if calculate() raises ValueError for invalid operations, test for ValueError not KeyError.
Return only the test file content, ready to run with pytest.
````python
{code}
```""",

    }

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompts[task]}],
        max_tokens=2048,
    )
    return response.choices[0].message.content

def print_result(title, content):
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)
    print(content)
    print()

def save_file(path, content):
    clean = content.replace("```python", "").replace("```", "").strip()
    with open(path, "w", encoding="utf-8") as f:
        f.write(clean)
    print(f"  [Saved] {path}")

def save_report(filename, results):
    """Save all results into a single clean report.md file."""
    report_path = os.path.splitext(filename)[0] + "_report.md"
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(f"# AI Dev Workflow Report\n\n")
        f.write(f"**File analysed:** `{filename}`  \n")
        f.write(f"**Generated on:** {now}  \n")
        f.write(f"**Model:** llama-3.3-70b-versatile (Groq)\n\n")
        f.write("---\n\n")

        for title, content in results:
            f.write(f"## {title}\n\n")
            f.write(content)
            f.write("\n\n---\n\n")

    print(f"  [Saved] {report_path}")
    return report_path

def run_pytest(test_file):
    """Auto-run pytest on the generated test file."""
    print(f"\n  Running pytest on {test_file}...\n")
    print("=" * 60)
    result = subprocess.run(
        ["pytest", test_file, "-v"],
        capture_output=False
    )
    if result.returncode == 0:
        print("\n  [pytest] All tests passed!")
    else:
        print("\n  [pytest] Some tests failed — check output above.")

def main():
    parser = argparse.ArgumentParser(
        description="Assignment 2 — AI Dev Workflow Assistant"
    )
    parser.add_argument("--file", required=True, help="Python file to analyse")
    parser.add_argument(
        "--mode",
        required=True,
        choices=["explain", "debug", "document", "test", "all"],
        help="Task to perform"
    )
    args = parser.parse_args()

    client = get_client()
    code = read_file(args.file)
    base = os.path.splitext(args.file)[0]

    tasks = (
        ["explain", "debug", "document", "test"]
        if args.mode == "all"
        else [args.mode]
    )

    titles = {
        "explain":  "Code Understanding",
        "debug":    "Debugging Report",
        "document": "Documentation Generated",
        "test":     "Unit Tests Generated",
    }

    results = []
    test_file = None

    for task in tasks:
        print(f"\nRunning '{task}' on {args.file}...")
        result = ask_groq(client, task, code, args.file)
        print_result(titles[task], result)
        results.append((titles[task], result))

        if task == "test":
            test_file = f"{base}_tests.py"
            save_file(test_file, result)

        if task == "document":
            save_file(f"{base}_documented.py", result)

    print("\nGenerating report...")
    save_report(args.file, results)

    
    if test_file and os.path.exists(test_file):
        run_pytest(test_file)

if __name__ == "__main__":
    main()
