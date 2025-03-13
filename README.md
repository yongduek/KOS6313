# KOS6313
Statistical Methods in Python for KOS6313

## Installation
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
4. Install `pandas`, `matplotlib`, `seaborn`
    ```
    pip install pandas matplotlib seaborn
    ```
1. create a Jupyter notebook in vscode (`myNotebook.ipynb`)
   - choose proper kernel: `.venv/python`
   - `hello world` will install necessary things


## CmdStanPy Installation

1. PIP install
   ``` 
   pip install cmdstanpy
   ```
   Then open python shell and run the following. It may take 10 minutes.
   ```
    import cmdstanpy
    cmdstanpy.install_cmdstan()
    cmdstanpy.install_cmdstan(compiler=True)  # only valid on Windows
   ```
## If you want to install C++ toolchain for your own    
1. You need a C++ compiler or toolchain. Choose one:
    - Mac users install `xcode`
    - MSYS2 for Windows 10/11: 
        - Go to the website https://www.msys2.org/, follow the **Installation** instructions there.
        - Then install open `MSYS2 UCRT64 terminal`
        - run: `pacman -S mingw-w64-ucrt-x86_64-toolchain`
        - Add UCRT64 to the PATH in Windows 10/11
            - To use the UCRT64 g++ in PowerShell, add the UCRT64 bin directory to your system’s PATH:
            - Find the bin directory:
                The typical location is:
                ``` C:\msys64\ucrt64\bin```

            - Add the path to the PATH environment variable:
                1. Search for “Environment Variables” in the Start menu.
                2. Click “Edit the system environment variables.”
                3. In the System Properties window, click the “Environment Variables” button.
                4. Under “System Variables,” find Path, select it, and click “Edit.”
                5. Click “New,” and paste `C:\msys64\ucrt64\bin` (or your specific path).
                6. Click OK to save.

            - Restart PowerShell to apply the changes.

        - Verify the Configuration
            In PowerShell, check if g++ is accessible by running:
            
            ``` g++ --version```
            
            You should see the version information of the UCRT64 g++ compiler.
    - WSL in Windows 10/11
        - Install Ubuntu 22.04: 
        - run `wsl --install -d Ubuntu-22.04` in PowerShell(Admin)
  
2. Python-Stan Interface (this takes time)
    ```
    pip install cmdstanpy
    python -m cmdstanpy.install_cmdstan
    ```
