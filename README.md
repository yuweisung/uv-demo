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

## 5. Set github repo

    ```
    git remote add origin git@github.com:yuweisung/uv-demo.gituv-demo.git
    git push
    ```

## 6. Export uv.lock to sbom

    ```
    uv export --format cyclonedx1.5 --output-file sbom.json
    ```

## 7. Add pytest to dev grouop

    ```
    uv add --dev pytest
    Resolved 12 packages in 324ms
      Built uv-demo @ file:///Users/ysung/git/uv-demo                                                                                                                                                                                                                                                                 
    Prepared 6 packages in 205ms
    Uninstalled 1 package in 0.77ms
    Installed 6 packages in 6ms
    + iniconfig==2.3.0
    + packaging==26.3
    + pluggy==1.6.0
    + pygments==2.21.0
    + pytest==9.1.1
    ~ uv-demo==0.1.0 (from file:///Users/ysung/git/uv-demo)
    ```

## 8. Install tools
    
    ```
    uv tool install httpie
    Resolved 16 packages in 462ms
    Prepared 15 packages in 318ms
    Installed 16 packages in 17ms
    + certifi==2026.7.22
    + charset-normalizer==3.5.1
    + defusedxml==0.7.1
    + httpie==3.2.4
    + idna==3.20
    + markdown-it-py==4.2.0
    + mdurl==0.1.2
    + multidict==6.9.1
    + pip==26.2.1
    + pygments==2.21.0
    + pysocks==1.7.1
    + requests==2.34.2
    + requests-toolbelt==1.0.0
    + rich==15.0.0
    + setuptools==84.0.0
    + urllib3==2.8.0
    Installed 3 executables: http, httpie, https

    uv tool list
    httpie v3.2.4
    - http
    - httpie
    - https

    uv tool run httpie
    usage: httpie [-h] [--debug] [--traceback] [--version] {cli,plugins} ...
    httpie: error: Please specify one of these: 'cli', 'plugins'

    This command is only for managing HTTPie plugins.
    To send a request, please use the http/https commands:

    $ http POST pie.dev/post hello=world

    $ https POST pie.dev/post hello=world

    uv

    ```

