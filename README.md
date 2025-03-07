# KOS6313
Statistical Methods in Python for KOS6313

## Install
1. Install Python (`python.org`)
   - Mac computers do have python installed. Do not try to install a new version of python.
   - Anaconda environment will not be used.
1. Install `Visual Studio Code`
   - Install `Python Extension` in `vscode`
   - Hello World
1. Virtual Environment
    ```
    python -m venv .venv
    .venv/Scripts/activate
    python -m pip install --upgrade pip
    ```
1. Python-Stan Interface (this takes time)
    ```
    pip install cmdstanpy
    python -m cmdstanpy.install_cmdstan
    ```
1. Install `pandas`, `matplotlib`, `seaborn`
    ```
    pip install pandas matplotlib seaborn
    ```
1. create a Jupyter notebook in vscode (`myNotebook.ipynb`)
   - choose proper kernel: `.venv/python`
   - `hello world` will install necessary things
