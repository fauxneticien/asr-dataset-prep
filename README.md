# Prepare data for ASR experiments

## Setup

```bash
# Create new conda environment
conda create -y --prefix ./env python=3.10 --no-default-packages
# Activate environment
conda activate ./env
# Install requirements
pip install -r requirements.txt
```

## Usage

Start a JupyterLab server:

```bash
# Activate environment if necessary
# conda activate ./env

jupyter lab
```

In your browser open the Jupyter Lab web interface and open an ipynb file (e.g. `prep-from-eafs_mixtec.ipynb`).
