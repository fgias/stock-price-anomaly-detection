cd stgan/STGAN
mamba run -n stgan \
    python main.py \
    --dataset crypto_volume \
    --lambda_G 10 \
    --trend_time 7 \
    --epoch 20 \
    2>&1 | tee crypto_volume/result/training.log