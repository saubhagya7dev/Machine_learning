## Jupyter Notebook & Virtual Environment Troubleshooting

### Problem Encountered

I created a virtual environment inside my `Machine_Learning` project and installed Jupyter Notebook. When I opened a `.ipynb` file in VS Code and tried to run a cell, I encountered:

```python
ModuleNotFoundError: No module named 'pandas'
```

Even after running:

```bash
pip install pandas numpy
```

the error persisted.

## Root Cause

The issue was caused by using the wrong virtual environment.

Although my terminal showed:

```bash
(.venv) PS D:\Code\Machine_Learning>
```

the packages were actually being installed into another environment:

```text
D:\Code\python-for-ai\.venv\Lib\site-packages
```

As a result:

* Jupyter Notebook was using one Python environment.
* `pip` was installing packages into a different Python environment.
* The notebook kernel could not find the installed packages.

## How I Diagnosed It

I checked which Python executable was being used:

```bash
where.exe python
where.exe pip
```

This revealed that the active environment was not the one inside my `Machine_Learning` project.

## Solution

1. Deactivated the incorrect virtual environment:

```bash
deactivate
```

2. Activated the correct project environment:

```bash
.\venv\Scripts\Activate.ps1
```

3. Verified the correct Python executable:

```bash
where.exe python
```

Expected output:

```text
D:\Code\Machine_Learning\venv\Scripts\python.exe
```

4. Installed required packages into the correct environment:

```bash
python -m pip install pandas numpy notebook ipykernel
```

5. Registered the environment as a Jupyter kernel:

```bash
python -m ipykernel install --user --name machine_learning --display-name "Python (Machine_Learning)"
```

6. Selected the correct kernel in VS Code.

## Key Lesson

Whenever working with multiple virtual environments:

```bash
where.exe python
where.exe pip
```

should be checked before installing packages.

Never assume the environment shown in the terminal prompt is the one actually being used.

## Outcome

Successfully configured Jupyter Notebook with the correct virtual environment and was able to run notebook cells using `pandas`, `numpy`, and other installed packages without errors.
