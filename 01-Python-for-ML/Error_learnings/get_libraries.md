# Generate `requirements.txt` from an Existing Python Project

A quick guide to automatically detect Python dependencies from an existing project when `requirements.txt` is missing.

---

## 1. Open the Project

Open PowerShell/Terminal and navigate to the project's root directory:

```powershell
cd "D:\Path\To\Your\Project"
```

---

## 2. Create a Virtual Environment

Recommended when working with a downloaded project:

```powershell
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\activate
```

You should see:

```text
(.venv) PS D:\Path\To\Your\Project>
```

---

## 3. Install `pipreqs`

`pipreqs` scans the project's Python files and detects the external libraries being imported.

```powershell
pip install pipreqs
```

---

## 4. Generate `requirements.txt`

### Recommended command for Windows

```powershell
pipreqs . --force --encoding=utf-8 --ignore .venv
```

### What the options mean

| Option             | Purpose                                  |
| ------------------ | ---------------------------------------- |
| `.`                | Scan the current project directory       |
| `--force`          | Create/overwrite `requirements.txt`      |
| `--encoding=utf-8` | Prevent Windows encoding errors          |
| `--ignore .venv`   | Prevent scanning the virtual environment |

The generated file will appear at:

```text
Project/
├── .venv/
├── requirements.txt
├── ...
└── ...
```

---

## 5. Install the Dependencies

Once `requirements.txt` has been generated:

```powershell
pip install -r requirements.txt
```

This installs the detected dependencies in one go.

---

## 6. Test the Project

Run the project normally.

For example:

```powershell
python main.py
```

or use whatever command the project requires.

If you encounter:

```text
ModuleNotFoundError: No module named 'xyz'
```

install the missing package:

```powershell
pip install xyz
```

Then add/update it in `requirements.txt`.

---

# Common Problem: UnicodeDecodeError

On Windows, `pipreqs` may fail with an error similar to:

```text
UnicodeDecodeError: 'charmap' codec can't decode byte ...
```

This happens when `pipreqs` tries to read a project file using Windows' default encoding.

### Fix

Use UTF-8 explicitly:

```powershell
pipreqs . --force --encoding=utf-8 --ignore .venv
```

This is the preferred command on Windows.

---

# Common Problem: `SyntaxWarning`

You may see warnings such as:

```text
SyntaxWarning: "\S" is an invalid escape sequence
SyntaxWarning: "\[" is an invalid escape sequence
```

These warnings may come from `pipreqs` itself.

If `requirements.txt` is generated successfully, these warnings can generally be ignored.

---

# If `pipreqs` Still Fails

You can identify Python files that cannot be read as UTF-8.

Run this in PowerShell:

```powershell
Get-ChildItem -Recurse -Filter *.py | ForEach-Object {
    try {
        [System.IO.File]::ReadAllText(
            $_.FullName,
            [System.Text.Encoding]::UTF8
        ) | Out-Null
    }
    catch {
        Write-Host "PROBLEM FILE: $($_.FullName)"
    }
}
```

This will show the problematic Python file.

Example:

```text
PROBLEM FILE: D:\Project\config.py
```

---

# Recommended Workflow

For a downloaded Python project:

```text
Download Project
       │
       ▼
Open Project Directory
       │
       ▼
Create .venv
       │
       ▼
Activate .venv
       │
       ▼
Install pipreqs
       │
       ▼
Run pipreqs
       │
       ▼
requirements.txt
       │
       ▼
pip install -r requirements.txt
       │
       ▼
Run & Test Project
```

### Commands at a glance

```powershell
cd "D:\Path\To\Project"

python -m venv .venv

.venv\Scripts\activate

pip install pipreqs

pipreqs . --force --encoding=utf-8 --ignore .venv

pip install -r requirements.txt
```

---

## `pipreqs` vs `pip freeze`

Do **not** confuse `pipreqs` with `pip freeze`.

### `pipreqs`

Scans the project source code and generates dependencies based on imports:

```powershell
pipreqs . --force --encoding=utf-8 --ignore .venv
```

Best when you downloaded a project that doesn't contain `requirements.txt`.

### `pip freeze`

Lists packages currently installed in the active environment:

```powershell
pip freeze > requirements.txt
```

This can include many unrelated packages installed in your environment.

### Recommendation

For a downloaded project with no dependency file:

**Use `pipreqs` first.**

For a project where you intentionally want to capture the exact environment:

**Use `pip freeze`.**

---

## Final Note

`pipreqs` is not perfect. Some dependencies may be loaded dynamically or may not be detected from imports.

Therefore:

1. Generate `requirements.txt`
2. Install it
3. Run the project
4. Fix any `ModuleNotFoundError`
5. Update `requirements.txt`
6. Commit `requirements.txt` to Git

This gives you a reproducible dependency setup for future machines and environments.
