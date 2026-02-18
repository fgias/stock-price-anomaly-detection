# Stock Price Anomaly Detection

Anomaly detection for stock prices.

## Plan

- Use [STGAN](https://ieeexplore.ieee.org/document/9669110), [repository](https://github.com/dleyan/STGAN), my [fork](https://github.com/fgias/STGAN).

## Folder structure

```
STGAN/
    - <dataset>/
        - data/
            - data.npy
            - ...
        - checkpoint/
        - result/
```

## Instructions

- Install mamba/miniforge3:

```
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
bash Miniforge3-$(uname)-$(uname -m).sh
```

- Install dependencies:

```
mamba env create -f env.yaml
```

- Run training:



## Workflow

1. **Prepare data and generate dataset**

    Use `crypto*data.ipynb` to download data from yahoo finance, and then preprocess them in the required format. Also, calculate any accompanying features.

1. **Specify the parameters of the generated dataset**

    Inside `stgan/STGAN/main.py` specify the parameters of the dataset:
    - `opt['dataset'] == 'crypto'`
    - `opt['timestamp'] = 1 # 1h`
    - ...

1. **Run training on the generated dataset**
    
    Specify configuration in `script.sh` and run training:

    ```
    bash script.sh
    ```

1. **Monitor training**

    Run notebook `stgan/training/training-plot.ipynb`, specifying the correct `training.log`.

1. **Check results**

    Run an evaluation as done in notebook `stgan/results_crypto.ipynb`, again using the correct output data.