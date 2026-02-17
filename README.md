# traffic-anomaly-detection

Link prediction and anomaly detection for traffic networks.

## Plan

- Use [STGAN](https://ieeexplore.ieee.org/document/9669110), [repository](https://github.com/dleyan/STGAN), my [fork](https://github.com/fgias/STGAN).

## Instructions

- Install mamba/miniforge3.

```
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
bash Miniforge3-$(uname)-$(uname -m).sh
```

- Install dependencies.

```
mamba env create -f env.yaml
```

- Activate environment.

```
conda activate env
```

## Traffic data

- Dropbox links: confidential.

- Notebook: `traffic_data.ipynb`.

### Data

- The X coordinate is the time, e.g. `0458` is 4:58am, and `2038` is 8:38pm.

- The Y coordinate is the density.

### Datasets

- `dataset1`: Data for every Monday, for 18 days.

- `dataset2`: Data for consecutive days, including weekends, for 6 months, February through July.

- `dataset3`: Data for consecutive days, including weekends, for 6 months, April through November.

## Weather data

- Dropbox links: confidential.

- Notebook: `weather_data.ipynb`.

## Ground Truth Data

- Social events

- Traffic accidents

- Road closures
