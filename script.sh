cd stgan-algo/STGAN
mamba run -n stgan python main.py --dataset crypto --lambda_G 1 --trend_time 7 > training.log 2>&1
