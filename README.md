# biomedical-continual-pretraining-bert
BERT-based model continually pre-trained using the Masked Language Modeling (MLM) objective on 2 million samples from English PubMed.

## Model description

This BERT-based model has been continuously trained using the Masked Language Modeling (MLM) objective on 2 million samples from the English column of the [vi_pubmed](https://huggingface.co/datasets/VietAI/vi_pubmed)

## Intended uses & limitations

This model is developed as part of an undergraduate thesis to compare the performance of general language models with domain-specific biomedical language models for Clinical NER applications. It is an experimental model, and its performance may not be optimal. Therefore, I recommend using [biobert-v1.1](https://huggingface.co/dmis-lab/biobert-v1.1) or [PubMedBERT](https://huggingface.co/microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext) for better results.

## Training and evaluation data

The model is trained on 2 million English text samples from [vi_pubmed](https://huggingface.co/datasets/VietAI/vi_pubmed), using a 90:10 split ratio for training and evaluation.

## Training procedure
The training procedure follows the [tutorial](https://huggingface.co/docs/transformers/tasks/masked_language_modeling) provided by Hugging Face, with the batch size adjusted to 64. Training was conducted on an NVIDIA RTX 4070 GPU.
### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'inner_optimizer': {'class_name': 'AdamWeightDecay', 'config': {'name': 'AdamWeightDecay', 'learning_rate': 2e-05, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-07, 'amsgrad': False, 'weight_decay_rate': 0.01}}, 'dynamic': True, 'initial_scale': 32768.0, 'dynamic_growth_steps': 2000}
- training_precision: mixed_float16
