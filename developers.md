# Developer Notes

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
