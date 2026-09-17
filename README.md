# SS_PRX_IC
## Inštalácia:

1.

uv venv --python 3.13 .venv

2. Policy

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

3. Aktivácia

.\\.venv\Scripts\Activate.ps1

4. Kivy

uv pip install --python .\\.venv\Scripts\python.exe "kivy==2.3.1"


5. Overenie:

.\\.venv\Scripts\python.exe -c "import sys, kivy; print(sys.version); print(kivy.__version__)"

6. Ak Kivy nepreslo

Remove-Item -Recurse -Force .venv

a potom kroky 1. az 5.

ZDROJ:
https://www.perplexity.ai/computer/a/7920c975-2290-4183-8c24-b04c421ab789
