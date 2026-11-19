"""Execute every lab reference and assignment with the workspace virtual environment."""
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parent
python = root / ".venv" / "Scripts" / "python.exe"
if not python.exists():
    raise SystemExit(f"Workspace venv not found: {python}")

lab_dirs = sorted(path for path in root.glob("Lab_*") if path.is_dir())
summary = []
for lab_dir in lab_dirs:
    files = sorted(lab_dir.glob("reference.py")) + sorted(lab_dir.glob("assignment1.py")) + sorted(lab_dir.glob("assignment2.py"))
    source_dir = lab_dir / "source_code"
    if source_dir.exists():
        files.extend(sorted(source_dir.glob("*.py")))
    lines = []
    for file in files:
        process = subprocess.run(
            [str(python), str(file)],
            cwd=str(root),
            capture_output=True,
            text=True,
        )
        status = "PASS" if process.returncode == 0 else "FAIL"
        lines.append(f"COMMAND: {python.name} {file.relative_to(root)}")
        lines.append(f"EXIT_CODE: {process.returncode}")
        lines.append(f"STATUS: {status}")
        if process.stdout:
            lines.append("STDOUT:")
            lines.append(process.stdout.rstrip())
        if process.stderr:
            lines.append("STDERR:")
            lines.append(process.stderr.rstrip())
        lines.append("")
        summary.append((lab_dir.name, file.name, status))
    (lab_dir / "TEST_OUTPUT.txt").write_text("\n".join(lines), encoding="utf-8")

failed = [item for item in summary if item[2] != "PASS"]
progress = ["# Agentic AI Lab Progress", "", f"Test runner: `{python.relative_to(root)}`", ""]
for lab_dir in lab_dirs:
    items = [item for item in summary if item[0] == lab_dir.name]
    if items:
        progress.append(f"## {lab_dir.name}")
        for _, name, status in items:
            progress.append(f"- [{'x' if status == 'PASS' else ' '}] {name}: {status}")
        progress.append("")

progress.append("## Overall")
progress.append(f"- Total executed: {len(summary)}")
progress.append(f"- Passed: {len(summary) - len(failed)}")
progress.append(f"- Failed: {len(failed)}")
(root / "PROGRESS.md").write_text("\n".join(progress), encoding="utf-8")

print(f"Executed {len(summary)} Python files: {len(summary) - len(failed)} passed, {len(failed)} failed")
for item in failed:
    print("FAIL", *item)
sys.exit(1 if failed else 0)
