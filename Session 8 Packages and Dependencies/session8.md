# Session 8 - Packages and Dependencies

## Virtual Environments
A virtual environment gives each Python project its own isolated copy of Python and third-party packages, 
preventing projects from interfering with one another or with your operating system.

* **Prevents version conflicts:** One project might rely on an older version of a library (for example, `pandas 1.5`), while a newer project requires `pandas 2.2`. Without virtual environments, all projects share a single global folder of packages, so upgrading a library for one project can break another.
* **Keeps your global Python installation clean:** Installing packages for every tutorial, test, or assignment into your main Python installation quickly clutters it. On macOS and Linux, modifying global packages can also interfere with built-in operating system tools that depend on Python.
* **Makes projects easy to share and reproduce:** Because a virtual environment contains only the packages installed for that specific project, you can export a clean list of dependencies (`pip freeze > requirements.txt`). Anyone else running your code—such as a teammate or lecturer—can install those exact versions with a single command.
* **Works without administrator permissions:** Packages installed inside a local `.venv` folder live inside your own project directory, so you can install and remove libraries freely even on locked-down lab or university computers.

### Making a virtual environment

Run this once inside your project folder:

* **Windows:**
```bash
python -m venv .venv

```


* **macOS / Linux:**
```bash
python3 -m venv .venv

```



This creates a hidden `.venv` folder containing an isolated copy of Python and pip.

---

### Activate the Virtual Environment

Run the activation script that matches your operating system and terminal:
In PyCharm you can access the terminal by going to `View > Tool Windows > Terminal` or pressing `Alt + F12`. It is also a short-cd cut icon on the left.

Got to the directory where your project is located. You can use the `cd` command to change directories. 
For example, if your project is in `Session 8 Packages and Dependencies`, you would run:
```bash
cd Session 8 Packages and Dependencies
```
Now we can activate the virtual environment. The command depends on your operating system and terminal:


* **Windows (Command Prompt):**
```bash
.venv\Scripts\activate

```

* **Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1

```


*(If PowerShell blocks the script with an execution policy error, run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` once and try again.)*
* **macOS / Linux:**
```bash
source .venv/bin/activate

```

---


* **Confirm it is active:** Your terminal prompt will now start with `(.venv)`. Any packages you install with `pip install <package>` will only be installed inside this environment.
* **Exit when finished:** Run `deactivate` to return to your system's global Python environment.

## Packages

PyPI (the Python Package Index, pronounced "pie-pea-eye") is the official online repository of third-party software packages and libraries for Python, 
hosted at [pypi.org](https://pypi.org).

While Python comes with a built-in standard library (modules like sys, math, and csv that work out of the box), PyPI hosts hundreds of thousands 
of community-created packages that extend what Python can do—for example:

- requests for fetching data from websites and APIs
- pandas for data analysis and working with spreadsheets
- pygame for building 2D games
- flask or django for web development

Click on the pypi link and search to see some libraries.

## An Example
`requests_example.py` is a simple program that uses the [requests](https://pypi.org/project/requests/) package to fetch data from a website.
If you try and run it now, it will fail because the `requests` package is not installed in your virtual environment.
```bash
 python .\requests_example.py
```
Try it you will get
`Traceback (most recent call last):
  File "C:\Users\Dunc\PycharmProjects\Python2026\Session 8 Packages and Dependencies\requests_example.py", line 1, in <module>
    import requests
ModuleNotFoundError: No module named 'requests'`

We need to install the `requests` package in our virtual environment before we can run the program.

### How you use PyPI
Rather than downloading files manually from the website, you use a package manager from the command line (or PyCharm's Python Packages tool window) 
to download and install packages automatically from PyPI:
```bash
pip install requests
```
This will install the `requests` package into our environment.

Now when you run the program, it should work correctly:
```bash
python .\requests_example.py
```

It's not very exciting but thw website returns a code! If you look at requests_example.py in PyCharm you will see that it is giving a syntax error on the library because PyCharm itself isn't inside our environment.
But we are running that program when we execute it from our environment on the command line. So change the web address to something silly, change the .uk to uk2), now when you run it you get a failure instead of the code(20).

You should **not** copy or zip the `.venv` folder itself, as it contains hardcoded paths and files tied to your specific operating system and Python installation. Instead, you export a plain-text list of your installed packages into a **`requirements.txt`** file and distribute that alongside your code so others can recreate the exact environment on their own machine.

### Export Your Environment
Ok requests_example is a bit boring so let's swap to forecast.py. You can see that this program is a bit more interesting,
it is using the requests library to get the weather for Leeds from a public API. You can run it and see what it does.
With your virtual environment activated in the terminal, run:

```bash
pip freeze > requirements.txt

```
Have a look to see what it has generated.
```bash
type requirements.txt
```
You'll see something like:
```bash
certifi==2026.11.20
charset-normalizer==3.5.3
idna==3.20
requests==2.34.2
urllib3==2.8.0
```
This creates a `requirements.txt` file listing every package installed in your environment along with its exact version number (for example, `requests==2.32.3`).

### Distribute Your Project Files

Package up (or push to GitHub) only your project files:

* Your Python scripts (e.g. `forecast.py`)
* Any required data files 
* `requirements.txt`

*(Leave out the `.venv` folder. If you are using Git and GitHub, add `.venv/` to your `.gitignore` file so it is never committed to the repository.)*

### Recreate the Environment Elsewhere

Whoever receives your files can recreate the environment in either of two ways:

* **In PyCharm:** Open the project folder containing `requirements.txt`. PyCharm will automatically detect the file and display a banner prompting to create a virtual environment and install the listed packages with one click.
* **From the command line:** Create and activate a fresh virtual environment, then install from the requirements file:
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```
```bash
# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

```



*(Note: If you are managing your project with **`uv`** rather than `pip`, distribute **`pyproject.toml`** and **`uv.lock`** instead—recipients can then recreate the entire environment by running `uv sync`.)*

### Deactivate the Virtual Environment
When you're done working in the virtual environment, you can deactivate it by running:
```bash
deactivate
```

### Installing Packages in PyCharm
You can also install packages from within PyCharm. Go to `File > Settings  > Python > Interpreter` and click the `+` 
icon to search for and install
packages from PyPI. This is equivalent to running `pip install <package>` in the terminal, but it provides a graphical 
interface and automatically installs the package into your project's virtual environment.

On the examples in this directory you will see the syntax error where it is trying to import the requests library disappear.

There isn't a one click way to write out PyCharm's installed packages to a requirements.txt file, 
but you can use the terminal in PyCharm to run the `pip freeze > requirements.txt` command.
In the very bottom right you can see what PyCharm is using (mine says .venv [3.12.9] and if I click on it, it gives me the full path, which is the root of y repo directory.
In the terminal make sure you are in the root of your project.

```bash
```

## A better Example
This repo contain `forecast.py` which is a more interesting example of using the requests library to get the weather for Leeds from a public API. You can run it and see what it does.

## Resetting everything
if you are playing around with this and want to go through it all again, you can remove your library with
```bash
python.exe -m pip uninstall -y requests
python -c "import requests"
```

In PyCharm go back to settings and remove the libraries you installed. Then delete the .venv folder and start again.