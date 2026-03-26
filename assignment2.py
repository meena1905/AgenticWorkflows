match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1).strip()
    
    # Fallback: manually strip common Markdown artifacts if regex fails
    return text.replace("```python", "").replace("```", "").strip()

def ask_groq(client, task, code, filename):
    """Executes specific agentic reasoning tasks using the Llama-3.3-70B model."""
    current_date = "2026-03-26"
    
    prompts = {
        "explain": f"""System: You are a Senior Software Architect. Date: {current_date}.
Task: Explain the architecture of the file '{filename}'. 
Provide: High-level overview, key functions/classes logic, and data flow analysis.""",

        "debug": f"""System: You are a Lead Security & QA Engineer.
Task: Audit '{filename}' for:
1. Logic bugs and calculation errors.
2. Security risks (OWASP Top 10 focus).
3. PEP 8 coding style violations.
Provide: Description of problems and the corrected code snippets for each.""",

        "document": f"""System: You are a Technical Documentation Expert.
Task: Add professional Google-style docstrings to all functions and classes in '{filename}'.
Constraint: Return ONLY the complete updated Python code. Do not include introductory chat.""",

        "test": f"""System: You are a Senior QA Automation Engineer.
Task: Write a comprehensive 'pytest' suite for '{filename}'.
Requirements:
1. Test happy paths, boundary conditions, and invalid inputs.
2. Use the EXACT exception types raised in the original code.
Return ONLY the runnable pytest code."""
    }

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a specialized AI Developer Agent. Your output is technical, accurate, and ready for production use."},
                {"role": "user", "content": f"{prompts[task]}\n\n### SOURCE CODE:\n{code}"}
            ],
            temperature=0.1,
            max_tokens=3500
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"⚠️ Agent Reasoning Error: {str(e)}"

def print_result(title, content):
    """Prints a formatted summary of the agent's work to the console."""
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)
    print(content)
    print()

def save_file(path, content, is_code=True):
    """Saves output to disk, cleaning code blocks if necessary."""
    data = clean_code_block(content) if is_code else content
    with open(path, "w", encoding="utf-8") as f:
        f.write(data)
    print(f"  💾 [File Saved] {path}")

def save_report(filename, results):
    """Generates a consolidated Markdown audit report."""
    report_path = os.path.splitext(filename)[0] + "_audit_report.md"
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(f"# AI Developer Audit Report: `{filename}`\n\n")
        f.write(f"- **Generated on:** {now}\n")
        f.write(f"- **Agent Version:** v2.0 (Llama-3.3-70B)\n\n")
        f.write("---\n\n")

        for title, content in results:
            f.write(f"## {title}\n\n")
            f.write(content)
            f.write("\n\n---\n\n")

    print(f"  📝 [Full Report Generated] {report_path}")
    return report_path

def run_pytest(test_file):
    """Automated execution of the generated pytest file."""
    print(f"\n🚀 Running Automated Test Suite: {test_file}")
    print("-" * 60)
    try:
        subprocess.run(["pytest", "--version"], capture_output=True, check=True)
        result = subprocess.run(["pytest", test_file, "-v"], capture_output=False)
        if result.returncode == 0:
            print("\n✅ ANALYSIS: All AI-generated tests PASSED.")
        else:
            print("\n⚠️ ANALYSIS: Test failures detected.")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("\nℹ️ Notice: 'pytest' not found. Skipping auto-run.")

def main():
    parser = argparse.ArgumentParser(description="Assignment 2 — AI Dev Workflow Assistant")
    parser.add_argument("--file", required=True, help="Python file path to analyze")
    parser.add_argument("--mode", required=True, choices=["explain", "debug", "document", "test", "all"])
    args = parser.parse_args()

    client = get_client()
    source_code = read_file(args.file)
    base_name = os.path.splitext(args.file)[0]

    tasks = ["explain", "debug", "document", "test"] if args.mode == "all" else [args.mode]
    titles = {"explain": "Code Architecture", "debug": "Security Audit", "document": "Documentation", "test": "Unit Tests"}

    results_for_report = []
    generated_test_path = None

    print(f"🔍 Agent initiated for: {args.file}")

    for task in tasks:
        print(f"\n🤖 Processing Task: {task.upper()}...")
        raw_response = ask_groq(client, task, source_code, args.file)
        print_result(titles.get(task, task), raw_response)
        results_for_report.append((titles.get(task, task), raw_response))

        if task == "test":
            generated_test_path = f"{base_name}_tests.py"
            save_file(generated_test_path, raw_response)
        if task == "document":
            save_file(f"{base_name}_documented.py", raw_response)

    save_report(args.file, results_for_report)
    if generated_test_path and os.path.exists(generated_test_path):
        run_pytest(generated_test_path)

if __name__ == "__main__":
    main()