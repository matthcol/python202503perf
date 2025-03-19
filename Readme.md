# Python advanced

## Links
- This repository: https://github.com/matthcol/python202503perf
- Python website: https://www.python.org/
- Distribution Anaconda: https://www.anaconda.com/
- Distribution Miniforge: https://github.com/conda-forge/miniforge
- IDE Visual Studio Code: https://code.visualstudio.com/
- IDE PyCharm: https://www.jetbrains.com/pycharm/

## Pytest (CLI)
Install avec conda, mamba or pip:
``` 
pip install pytest
```

Run pytest:
```
pytest
pytest tests/
pytest -v
pytest -v -k fibo3
```

## Conda environments
With distributions: anaconda, miniconda, miniforge

### Start a new environment
```
conda create -n envformation313 python=3.13
conda activate envformation313
conda install numpy pandas jupyterlab pytest
```

### VS Code
Installer les extensions Python et Pylance et éventuellement MyPy.
- Lancer VS Code dans son répertoire de projet et environnement adéquat: `code .`
- Choisir son interprète python: `Ctrl+Maj+P`
- Quick Fix (import, ...): `Ctrl+;` or `Ctrl+Maj+;`

 