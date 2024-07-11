#!/bin/bash

set -e

stage=0
stop_stage=100

dl_dir=$PWD/download

. ./path.sh || exit 1
. ./cmd.sh || exit 1

if [ $stage -le 0 ] && [ $stop_stage -ge 0 ]; then
  echo "Stage 0: Data Preparation"
  # Assuming your .csv/.tsv files are already in the metadata directory
  mkdir -p data/{train,dev,test}
  for split in train dev test; do
    python local/prepare_data.py --input metadata/${split}.csv --output data/${split}
  done
fi

echo "Data preparation completed."
