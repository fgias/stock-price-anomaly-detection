#!/bin/bash

#SBATCH --job-name=ximantis
#SBATCH --nodes=1
#SBATCH --time=28800
#SBATCH --output=%x-%j.out
#SBATCH --error=%x-%j.err
#SBATCH --gpus=a100_3g.40gb:1
#SBATCH --cpus-per-task=8

eval "$(conda shell.bash hook)"
conda activate stgan
cd stgan-algo/STGAN
python main.py --dataset ximantis_smooth_3_truncated --lambda_G 1 --trend_time 113 #(252-58)/288 * 7 * 24
