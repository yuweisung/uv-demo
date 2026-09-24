# Steps
## 1. Install uv

    ```
    brew install uv
    uv --version
    ```

## 2. Init a project

    ```
    cd ~/git
    uv init uv-demo
    cd uv-demo
    ```

## 3. Show/set python version

    ```
    cat .python-version
    3.13

    uv python list
    cpython-3.15.0rc2-macos-aarch64-none                 <download available>
    cpython-3.15.0rc2+freethreaded-macos-aarch64-none    <download available>
    cpython-3.14.7-macos-aarch64-none                    <download available>
    cpython-3.14.7+freethreaded-macos-aarch64-none       <download available>
    cpython-3.14.6-macos-aarch64-none                    /opt/homebrew/bin/python3.14 -> ../Cellar/python@3.14/3.14.6/bin/python3.14
    ...

    uv python pin 3.14
    Updated `.python-version` from `3.13` -> `3.14`
    ```

## 4. Venv

    ```
    uv venv
    uv add pandas
    Resolved 6 packages in 521ms
      Built uv-demo @ file:///Users/ysung/git/uv-demo                                                                                                                                                                                                                                                                 
    Prepared 5 packages in 884ms
    Uninstalled 1 package in 0.79ms
    Installed 5 packages in 19ms
    + numpy==2.5.3
    + pandas==3.0.6
    + python-dateutil==2.9.0.post0
    + six==1.17.0
    ~ uv-demo==0.1.0 (from file:///Users/ysung/git/uv-demo)
    
    # Check uv.lock and pyproject.toml
    ```

## 4. Run!

    ```
    uv run uv-demo
    Hello from uv-demo!

    ```

## . Set github repo

    ```
    git remote add origin git@github.com:yuweisung/uv-demo.gituv-demo.git
    git push
    ```
