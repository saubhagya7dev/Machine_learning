# Python Virtual Environments

A **virtual environment** in Python is an isolated environment that allows a project to have its own Python packages and dependencies without interfering with other projects or the system-wide Python installation.

This guide covers virtual environments from **beginner to practical/professional usage**.

---

# 1. What is a Virtual Environment?

Suppose you have two Python projects:

```text
Project A → pandas 2.x
Project B → pandas 3.x
```

If you install pandas globally, you can run into version conflicts.

A virtual environment solves this:

```text
Computer
│
├── Global Python
│
├── Project A
│   └── venv
│       └── pandas 2.x
│
└── Project B
    └── venv
        └── pandas 3.x
```

Each project gets its own isolated packages.

---

# 2. Why Should You Use Virtual Environments?

Virtual environments are useful because they provide:

* Dependency isolation
* Version control
* Reproducible projects
* Cleaner development environments
* Easier deployment
* Fewer package conflicts
* Better project organization

For example:

```text
Project A
Python 3.11
TensorFlow 2.x
Pandas 2.x

Project B
Python 3.12
PyTorch
Pandas 3.x
```

Both projects can coexist without interfering with each other.

---

# 3. Check Python Installation

Open your terminal.

On Windows:

```powershell
python --version
```

Example:

```text
Python 3.12.4
```

You can also check:

```powershell
py --version
```

To find where Python is working/Active

```powershell
where.exe python
```

To find where pip is currently working/Active

```powershell
where.exe pip
```
---

# 4. Create a Project Folder

For example:

```powershell
mkdir my_project
cd my_project
```

Your folder currently looks like:

```text
my_project/
```

---

# 5. Create a Virtual Environment

Run:

```powershell
python -m venv venv
```

Here:

```text
python
```

runs Python.

```text
-m
```

means "run a Python module."

```text
venv
```

is Python's built-in virtual-environment module.

```text
venv
```

at the end is the name of the environment.

So:

```powershell
python -m venv venv
```

means:

> Use Python's `venv` module to create a virtual environment named `venv`.

---

# 6. You Can Name the Environment Anything

For example:

```powershell
python -m venv env
```

or:

```powershell
python -m venv .venv
```

or:

```powershell
python -m venv my_environment
```

A common professional convention is:

```text
.venv
```

So I recommend:

```powershell
python -m venv .venv
```

---

# 7. What Gets Created?

After running:

```powershell
python -m venv .venv
```

your project looks approximately like:

```text
my_project/
│
└── .venv/
    ├── Include/
    ├── Lib/
    ├── Scripts/
    └── pyvenv.cfg
```

The exact structure can vary slightly by Python version and operating system.

---

# 8. Activate the Virtual Environment

## Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

After activation, you'll see something similar to:

```text
(.venv) PS D:\Code\my_project>
```

The:

```text
(.venv)
```

means your virtual environment is active.

---

# 9. Windows Command Prompt

If you're using CMD instead of PowerShell:

```cmd
.venv\Scripts\activate
```

---

# 10. macOS/Linux

Use:

```bash
source .venv/bin/activate
```

---

# 11. How Do You Know It Is Activated?

Run:

```powershell
python --version
```

Then:

```powershell
where python
```

The Python path should point inside your `.venv`.

For example:

```text
D:\Code\my_project\.venv\Scripts\python.exe
```

---

# 12. Upgrade pip

Once your environment is activated, it is good practice to upgrade pip:

```powershell
python -m pip install --upgrade pip
```

Check the version:

```powershell
pip --version
```

You can also use:

```powershell
python -m pip --version
```

Using:

```powershell
python -m pip
```

is often safer because it explicitly uses the pip associated with the currently selected Python interpreter.

---

# 13. Install Packages

For example:

```powershell
pip install numpy
```

Install pandas:

```powershell
pip install pandas
```

Install multiple packages:

```powershell
pip install numpy pandas matplotlib scikit-learn
```

For an AI/ML project, you might eventually install packages such as:

```powershell
pip install numpy pandas matplotlib scikit-learn
```

and later:

```powershell
pip install torch
```

---

# 14. Check Installed Packages

Run:

```powershell
pip list
```

Example:

```text
Package       Version
------------- -------
numpy         2.x
pandas        3.x
pip           xx.x
```

Another useful command:

```powershell
pip freeze
```

---

# 15. Difference Between `pip list` and `pip freeze`

## `pip list`

Shows installed packages in a readable table:

```powershell
pip list
```

Example:

```text
numpy       2.x
pandas      3.x
matplotlib  3.x
```

## `pip freeze`

Produces package requirements in a format suitable for saving:

```powershell
pip freeze > requirements.txt
```
this created a file named requirements.txt that ahve all the dependencies that is currently installed

Example:

```text
numpy==2.x
pandas==3.x
matplotlib==3.x
```

---

# 16. The Most Important File: `requirements.txt`

A Python project commonly stores its dependencies in:

```text
requirements.txt
```

Create it using:

```powershell
pip freeze > requirements.txt
```

Your project now looks like:

```text
my_project/
│
├── .venv/
│
└── requirements.txt
```

The file might contain:

```text
numpy==2.x
pandas==3.x
matplotlib==3.x
scikit-learn==1.x
```

---

# 17. Why Is `requirements.txt` Important?

Imagine you send your project to another developer.

They clone your GitHub repository.

They don't know which packages you used.

Instead of telling them:

```text
Install numpy
Install pandas
Install matplotlib
Install scikit-learn
...
```

they can simply run:

```powershell
pip install -r requirements.txt
```

Python installs all listed dependencies.

---

# 18. Complete Setup for Someone Cloning Your Project

Suppose someone clones:

```text
my_project
```

They can do:

```powershell
cd my_project
```

Create the environment:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Now they have an environment similar to yours.

---

# 19. `.venv` Should NOT Usually Be Uploaded to GitHub

You should generally **not commit the virtual environment** to Git.

Why?

Because `.venv` can contain:

* Thousands of files
* Installed packages
* Platform-specific binaries
* Large files
* Machine-specific paths

Instead, upload:

```text
requirements.txt
```

and let other developers recreate the environment.

---

# 20. Add `.venv` to `.gitignore`

Create:

```text
.gitignore
```

Add:

```gitignore
.venv/
```

You can also use:

```gitignore
venv/
env/
```

if those are the names you use.

A typical Python `.gitignore` might contain:

```gitignore
# Virtual environment
.venv/
venv/
env/

# Python cache
__pycache__/
*.py[cod]

# Jupyter
.ipynb_checkpoints/

# Environment variables
.env
```

---

# 21. VS Code and Virtual Environments

VS Code can automatically detect virtual environments.

Open your project:

```powershell
code .
```

Then select your Python interpreter.

Press:

```text
Ctrl + Shift + P
```

Search:

```text
Python: Select Interpreter
```

Choose:

```text
.venv\Scripts\python.exe
```

Now VS Code uses the Python interpreter inside your virtual environment.

---

# 22. Verify the VS Code Interpreter

Create:

```text
test.py
```

and run:

```python
import sys

print(sys.executable)
```

It should print something similar to:

```text
D:\Code\my_project\.venv\Scripts\python.exe
```

That confirms you're using the virtual environment.

---

# 23. Installing Packages from VS Code Terminal

Once the `.venv` interpreter is selected, you can use:

```powershell
pip install pandas
```

VS Code's terminal may automatically activate the environment.

You might see:

```text
(.venv) PS D:\Code\my_project>
```

---

# 24. Virtual Environment + Jupyter Notebook

Virtual environments are especially useful for Data Science and ML projects.

Install Jupyter:

```powershell
pip install jupyter
```

Install the IPython kernel:

```powershell
pip install ipykernel
```

Register your environment:

```powershell
python -m ipykernel install --user --name=myproject --display-name "Python (myproject)"
```

Then open Jupyter:

```powershell
jupyter notebook
```

or:

```powershell
jupyter lab
```

Select:

```text
Python (myproject)
```

as your notebook kernel.

---

# 25. Why This Matters for Machine Learning

For example, one ML project might require:

```text
numpy
pandas
scikit-learn
matplotlib
seaborn
xgboost
```

Another project might require:

```text
torch
torchvision
transformers
accelerate
```

Trying to install everything globally can create dependency conflicts.

Instead:

```text
ML Project
└── .venv
    ├── numpy
    ├── pandas
    ├── sklearn
    └── xgboost

Deep Learning Project
└── .venv
    ├── torch
    ├── torchvision
    └── transformers
```

Each project remains isolated.

---

# 26. Environment Variables

Virtual environments are also commonly used alongside `.env` files.

Install:

```powershell
pip install python-dotenv
```

Example `.env`:

```text
API_KEY=your_api_key
DATABASE_URL=your_database_url
```

Python:

```python
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")

print(api_key)
```

Important:

**Never upload secrets to GitHub.**

Add:

```gitignore
.env
```

to `.gitignore`.

---

# 27. Deactivating the Environment

When you're finished working:

```powershell
deactivate
```

Your terminal changes from:

```text
(.venv) PS D:\Code\my_project>
```

to:

```text
PS D:\Code\my_project>
```

The environment is now inactive.

---

# 28. Reactivating the Environment Later

You don't need to create it again.

If `.venv` already exists:

```powershell
.venv\Scripts\Activate.ps1
```

That's all.

Then continue working.

---

# 29. Important: Don't Recreate It Every Time

Wrong workflow:

```text
Create venv
Work
Delete venv
Create venv
Work
Delete venv
```

Normal workflow:

```text
Create venv
      ↓
Activate
      ↓
Work
      ↓
Deactivate
      ↓
Next day
      ↓
Activate existing venv
      ↓
Continue working
```

---

# 30. Delete a Virtual Environment

If you want to completely remove it, first deactivate:

```powershell
deactivate
```

Then delete the `.venv` folder.

PowerShell:

```powershell
Remove-Item -Recurse -Force .venv
```

Or simply delete `.venv` using File Explorer.

Your source code and `requirements.txt` remain untouched.

---

# 31. Recreate a Deleted Environment

If you accidentally delete `.venv`, don't panic.

As long as you have:

```text
requirements.txt
```

you can recreate it:

```powershell
python -m venv .venv
```

Activate:

```powershell
.venv\Scripts\Activate.ps1
```

Install everything:

```powershell
pip install -r requirements.txt
```

---

# 32. PowerShell Execution Policy Error

Sometimes Windows PowerShell gives an error such as:

```text
cannot be loaded because running scripts is disabled
```

This can happen when activating:

```powershell
.venv\Scripts\Activate.ps1
```

One option is to use Command Prompt instead:

```cmd
.venv\Scripts\activate
```

Another option is to change the PowerShell execution policy for your user account:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then try:

```powershell
.venv\Scripts\Activate.ps1
```

Only change execution-policy settings when you understand the security implications.

---

# 33. Check Whether You Are Inside a Virtual Environment

Run:

```powershell
python -c "import sys; print(sys.prefix != sys.base_prefix)"
```

If it prints:

```text
True
```

you're inside a virtual environment.

If it prints:

```text
False
```

you're using the base/system Python environment.

---

# 34. Find the Current Python Interpreter

Run:

```powershell
python -c "import sys; print(sys.executable)"
```

Example:

```text
D:\Code\my_project\.venv\Scripts\python.exe
```

This is one of the most useful debugging commands.

---

# 35. Check Where a Package Is Installed

For example:

```powershell
pip show pandas
```

You'll see information including:

```text
Name: pandas
Version: ...
Location: D:\Code\my_project\.venv\Lib\site-packages
```

This helps confirm that the package is installed inside the correct environment.

---

# 36. Install a Specific Package Version

You don't have to install the latest version.

For example:

```powershell
pip install pandas==2.2.3
```

You can also specify a minimum version:

```powershell
pip install "pandas>=2.2"
```

Or a version range:

```powershell
pip install "pandas>=2.2,<3"
```

---

# 37. Upgrade a Package

```powershell
pip install --upgrade pandas
```

or:

```powershell
python -m pip install --upgrade pandas
```

---

# 38. Uninstall a Package

```powershell
pip uninstall pandas
```

Pip will ask for confirmation.

---

# 39. Install Development Dependencies

Some projects need packages only during development.

For example:

```text
pytest
black
ruff
jupyter
```

You can organize them separately if your project requires it.

For a simple project, however, one `requirements.txt` is often enough.

---

# 40. Virtual Environment Is Not a Python Version Manager

This distinction is important.

A virtual environment isolates packages and Python installations for a project, but it isn't primarily a tool for managing multiple Python versions across your machine.

For example:

```text
Python 3.11
Python 3.12
Python 3.13
```

Managing multiple Python versions is a separate problem.

Tools such as:

```text
pyenv
uv
conda
```

can help with Python-version/environment management.

---

# 41. Using a Specific Python Version

If you have multiple Python versions installed on Windows, you can use the Python launcher:

```powershell
py -3.12 -m venv .venv
```

This specifically asks Python 3.12 to create the environment.

For example:

```powershell
py -3.11 -m venv .venv
```

creates the environment using Python 3.11.

---

# 42. Recommended Professional Project Structure

A typical Python project might look like:

```text
my_project/
│
├── .venv/
│
├── src/
│   └── main.py
│
├── tests/
│   └── test_main.py
│
├── .gitignore
├── requirements.txt
├── README.md
└── main.py
```

For larger projects, the exact structure will depend on the framework and architecture.

---

# 43. Typical Daily Workflow

When starting work on an existing project:

```powershell
cd my_project
```

Activate:

```powershell
.venv\Scripts\Activate.ps1
```

Check Python:

```powershell
python --version
```

Check packages:

```powershell
pip list
```

Then work on your project.

When finished:

```powershell
deactivate
```

---

# 44. Typical New Project Workflow

For a completely new project:

```powershell
mkdir my_project
cd my_project

python -m venv .venv

.venv\Scripts\Activate.ps1

python -m pip install --upgrade pip

pip install numpy pandas matplotlib

pip freeze > requirements.txt
```

Then create your code.

---

# 45. Typical GitHub Workflow

A professional workflow can look like:

```text
Create project
      ↓
Create .venv
      ↓
Activate .venv
      ↓
Install dependencies
      ↓
Write code
      ↓
Test
      ↓
pip freeze > requirements.txt
      ↓
Create .gitignore
      ↓
Ignore .venv/
      ↓
git add .
      ↓
git commit
      ↓
git push
```

When another developer clones it:

```text
git clone
    ↓
Create .venv
    ↓
Activate .venv
    ↓
pip install -r requirements.txt
    ↓
Run project
```

---

# 46. Common Mistakes

## Mistake 1 — Installing packages globally

For example:

```powershell
pip install pandas
```

without checking whether your environment is active.

You might accidentally install it globally.

Check:

```powershell
python -c "import sys; print(sys.executable)"
```

---

## Mistake 2 — Committing `.venv`

Don't normally do:

```text
git add .venv/
```

Instead add:

```gitignore
.venv/
```

---

## Mistake 3 — Forgetting to activate the environment

You may think:

```text
I installed pandas yesterday.
```

but today:

```powershell
python my_program.py
```

could be using a different Python interpreter.

Activate first:

```powershell
.venv\Scripts\Activate.ps1
```

---

## Mistake 4 — Using the wrong VS Code interpreter

Your terminal might use:

```text
.venv
```

while VS Code/Jupyter uses another Python interpreter.

Check:

```text
Python: Select Interpreter
```

and choose:

```text
.venv
```

---

## Mistake 5 — Forgetting `requirements.txt`

If you don't record your dependencies, reproducing the project later becomes harder.

Use:

```powershell
pip freeze > requirements.txt
```

---

# 47. What Happens Internally?

When you create:

```powershell
python -m venv .venv
```

Python creates an isolated environment containing the necessary Python environment structure.

Packages are installed into the environment's site-packages directory.

Conceptually:

```text
Global Python
│
└── Global packages

Project
│
└── .venv
    │
    ├── Python environment
    ├── pip
    └── site-packages
        ├── numpy
        ├── pandas
        └── matplotlib
```

When the environment is activated, commands such as:

```text
python
pip
```

resolve to the environment's executables.

---

# 48. Activation Does Not "Turn Python On"

This is a common misunderstanding.

Python itself is already installed.

Activation mainly changes your shell's environment so that commands such as:

```text
python
pip
```

point to the virtual environment.

That's why you can also directly execute the environment's Python without activating it.

For example:

```powershell
.venv\Scripts\python.exe main.py
```

Activation is mainly a convenience.

---

# 49. Can You Have Multiple Virtual Environments?

Yes.

For example:

```text
Projects/
│
├── fraud_detection/
│   └── .venv/
│
├── chatbot/
│   └── .venv/
│
├── computer_vision/
│   └── .venv/
│
└── data_analysis/
    └── .venv/
```

Each project can have completely different dependencies.

---

# 50. Virtual Environment vs Global Python

## Global Python

```text
One Python installation
       ↓
Many packages
       ↓
Many projects
       ↓
Potential conflicts
```

## Virtual Environments

```text
Python
│
├── Project A
│   └── .venv
│       └── dependencies
│
├── Project B
│   └── .venv
│       └── dependencies
│
└── Project C
    └── .venv
        └── dependencies
```

For serious development, the second approach is generally preferable.

---

# 51. Essential Commands Cheat Sheet

## Create

```powershell
python -m venv .venv
```

## Activate — Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

## Activate — Windows CMD

```cmd
.venv\Scripts\activate
```

## Activate — macOS/Linux

```bash
source .venv/bin/activate
```

## Check Python

```powershell
python --version
```

## Find Python

```powershell
where python
```

## Find exact interpreter

```powershell
python -c "import sys; print(sys.executable)"
```

## Upgrade pip

```powershell
python -m pip install --upgrade pip
```

## Install package

```powershell
pip install package_name
```

## Install multiple packages

```powershell
pip install numpy pandas matplotlib
```

## Install from requirements

```powershell
pip install -r requirements.txt
```

## List packages

```powershell
pip list
```

## Freeze packages

```powershell
pip freeze
```

## Create requirements file

```powershell
pip freeze > requirements.txt
```

## Upgrade package

```powershell
pip install --upgrade package_name
```

## Uninstall package

```powershell
pip uninstall package_name
```

## Deactivate

```powershell
deactivate
```

## Delete environment

```powershell
Remove-Item -Recurse -Force .venv
```

---

# 52. The Most Important Workflow to Remember

If you're working on a Python project, remember this:

```text
1. Create project
       ↓
2. Create virtual environment
       ↓
3. Activate it
       ↓
4. Install packages
       ↓
5. Write code
       ↓
6. Save dependencies
       ↓
7. Add .venv to .gitignore
       ↓
8. Push source code + requirements.txt
       ↓
9. Another machine creates its own .venv
       ↓
10. pip install -r requirements.txt
```

The three commands you should remember first are:

```powershell
python -m venv .venv
```

```powershell
.venv\Scripts\Activate.ps1
```

```powershell
pip install -r requirements.txt
```

And when you're done:

```powershell
deactivate
```

---

# 53. Recommended Setup for Your AI/ML Projects

For an AI/ML project, I recommend using this structure:

```text
project/
│
├── .venv/
│
├── data/
│
├── notebooks/
│
├── src/
│
├── models/
│
├── tests/
│
├── .gitignore
├── requirements.txt
├── README.md
└── main.py
```

Start with:

```powershell
python -m venv .venv
```

Activate:

```powershell
.venv\Scripts\Activate.ps1
```

Then:

```powershell
python -m pip install --upgrade pip
```

Install your initial packages:

```powershell
pip install numpy pandas matplotlib scikit-learn jupyter
```

Save them:

```powershell
pip freeze > requirements.txt
```

Add this to `.gitignore`:

```gitignore
.venv/
__pycache__/
.ipynb_checkpoints/
.env
```

Now your project is ready for development and GitHub.

---

# 54. Final Mental Model

Think of a virtual environment as a **separate toolbox for each Python project**.

Without virtual environments:

```text
One toolbox
    ↓
Everything mixed together
    ↓
Version conflicts
    ↓
Problems
```

With virtual environments:

```text
Project A
└── Its own toolbox

Project B
└── Its own toolbox

Project C
└── Its own toolbox
```

Your computer's Python installation remains separate, while every project gets the dependencies it needs.

**Best practice:**

> One project → one virtual environment → one dependency definition (`requirements.txt`) → don't commit `.venv` to Git.
