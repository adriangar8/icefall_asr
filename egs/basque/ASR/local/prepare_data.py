import argparse
import pandas as pd
import os

def prepare_data(input_file, output_dir):
    df = pd.read_csv(input_file, sep='\t')
    os.makedirs(output_dir, exist_ok=True)
    for index, row in df.iterrows():
        audio_path = row['audio']
        text = row['text']
        with open(os.path.join(output_dir, f"{index}.txt"), 'w') as f:
            f.write(text)
        # Copy or symlink the audio files to the output directory
        os.symlink(audio_path, os.path.join(output_dir, f"{index}.wav"))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Prepare Basque ASR data")
    parser.add_argument('--input', type=str, required=True, help="Input CSV/TSV file")
    parser.add_argument('--output', type=str, required=True, help="Output directory")
    args = parser.parse_args()
    prepare_data(args.input, args.output)
