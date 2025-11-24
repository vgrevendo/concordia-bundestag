# Developer Notes

## Setting Up Virtual Environment

### Creating the venv/ Folder

Create a virtual environment in the project directory:

```bash
python3 -m venv venv
```

Or on some systems:

```bash
python -m venv venv
```

### Activating the Virtual Environment

**On macOS/Linux:**
```bash
source venv/bin/activate
```

**On Windows (Command Prompt):**
```bash
venv\Scripts\activate.bat
```

**On Windows (PowerShell):**
```bash
venv\Scripts\Activate.ps1
```

Once activated, your terminal prompt should be prefixed with `(venv)`.

### Installing Packages with pip

After activating the virtual environment, install the project dependencies:

```bash
pip install -e .
```

Or to install with development dependencies:

```bash
pip install -e ".[dev]"
```

To install from requirements.txt (if available):

```bash
pip install -r requirements.txt
```

To deactivate the virtual environment when you're done:

```bash
deactivate
```

## PyTorch/vLLM Compatibility on Intel Macs

PyTorch dropped Intel macOS (x86_64) support after version 2.2.0 in January 2024. If you're on an Intel Mac:

- Latest available PyTorch version: **2.2.2**
- vLLM requires PyTorch 2.9.0+ and **will not install** on Intel Macs
- To update requirements without vLLM:
  ```bash
  pip-compile --generate-hashes --reuse-hashes --strip-extras --allow-unsafe --upgrade --extra dev setup.py examples/requirements.in
  ```

## Local Colab Runtime

To run a local Jupyter runtime that can connect to Google Colab:

```bash
jupyter notebook \
    --NotebookApp.allow_origin='https://colab.research.google.com' \
    --port=8888 \
    --NotebookApp.port_retries=0 \
    --NotebookApp.allow_credentials=True
```
