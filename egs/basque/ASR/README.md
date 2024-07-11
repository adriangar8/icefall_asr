---
license: cc-by-4.0
task_categories:
- automatic-speech-recognition
language:
- eu
tags:
- asr
- stt
- dataset
pretty_name: Composite dataset for basque
size_categories:
- 100K<n<1M
configs:
- config_name: default
  data_files:
  - split: train
    path: "metadata/train.tsv"
  - split: test_cv
    path: "metadata/test_cv.tsv"
  - split: test_parl
    path: "metadata/test_parl.tsv"
  - split: test_oslr
    path: "metadata/test_oslr.tsv"
  - split: dev
    path: "metadata/dev.tsv"
---

# Composite dataset for Basque made from public available data
This dataset is composed of the following public available data:

**Train split**
- mozilla-foundation/common_voice_16_1/eu: "validated" split removing "test" split's sentences. (validated split contains official train + dev + test splits and more unique data)
- gttsehu/basque_parliament_1/eu: "train_clean" split removing some of the sentences that are repeated in "test" and "dev/validation" splits (not the same recording but same text).
- openslr: a train split made from the SLR76 (Basque recordings) subset, this split has been cleaned from acronyms, numbers and sentences that are repeated in the following test split.
| Source               | Hours        | Sentences  |
|----------------------|--------------|------------|
| common_voice_16_1    | 173.78 h     | 117517     |
| basque_parliament_1  | 368.02 h     | 184837     |
| openslr              | 6.45 h       | 3306       |
| **Total**            | **548.25 h** | **305660** |

**Test split**
It is recommended to evaluate on separated test splits.
- mozilla-foundation/common_voice_16_1/eu: official "test" split.
- gttsehu/basque_parliament_1/eu: official "test" split.
- openslr: a test split made from the SLR76 (Basque recordings) subset, this split has been cleaned from acronyms, numbers and repeated sentences so all of them are only once in the split.
| Source               | Hours        | Sentences  |
|----------------------|--------------|------------|
| common_voice_16_1    | 21.5 h       | 12742      |
| basque_parliament_1  | 2.85 h       | 1521       |
| openslr              | 2 h          | 1034       |
| **Total**            | **26.35 h**  | **15297**  |

**Dev split**
- gttsehu/basque_parliament_1/eu: official "dev/validation" split.
| Source               | Hours        | Sentences  |
|----------------------|--------------|------------|
| basque_parliament_1  | 2.62 h       | 1397       |
| **Total**            | **2.62 h**   | **1397**   |