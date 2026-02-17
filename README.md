# Stock Price Anomaly Detection

Anomaly detection for stock prices.

## Plan

- Use [STGAN](https://ieeexplore.ieee.org/document/9669110), [repository](https://github.com/dleyan/STGAN), my [fork](https://github.com/fgias/STGAN).

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

```
bash script.sh
```
