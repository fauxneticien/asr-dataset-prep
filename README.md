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

## NVIDIA Speech Data Explorer

Included in the repo is a copy of the [NVIDIA NeMo Speech Data Explorer](https://github.com/NVIDIA/NeMo/tree/stable/tools/speech_data_explorer)

### Setup

```
pip install -r requirements-sde.txt
```

### Usage

Given a manifest JSON file such as (where `text` is the human/reference transcription and `pred_text` is the machine transcription):

```json
{"audio_filepath": "data/processed/20230818_mixtec/clips/SMD-0049-Medicinas6_00h02m45s110.wav", "duration": 1.2, "text": "ujum", "pred_text": "ujum ujum"}
{"audio_filepath": "data/processed/20230818_mixtec/clips/SMD-0054-Maestro_00h35m17s082.wav", "duration": 1.1, "text": "su si ko an", "pred_text": "txn ixin ko'o o va"}
```

```bash
python nvidia-sde.py tmp/mixtec-manifest-demo.json 
```

You can then browse to the Data Explorer running on the URL reported by the script (e.g. `http://0.0.0.0:8050/`):

<img width="1000" alt="Screenshot 2023-08-18 at 4 50 42 PM" src="https://user-images.githubusercontent.com/9938298/261731833-716dc988-1cf6-4c33-af89-6553dadf3be4.png">