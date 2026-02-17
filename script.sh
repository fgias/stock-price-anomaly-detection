conda activate stgan
cd stgan-algo/STGAN
python main.py --dataset crypto --lambda_G 1 --trend_time 7 > log.txt 2>&1
