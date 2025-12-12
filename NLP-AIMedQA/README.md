# AIMedQA – Medical Question Answering with Transformers

This project focuses on the development and evaluation of a Medical Question Answering (Q&A)
system using transformer-based language models. The task is framed as a sequence-to-sequence
generation problem, where a patient-style question is mapped to a medically accurate response.

## Objectives
- Compare fine-tuning and prompt-based strategies for medical Q&A
- Evaluate the impact of domain-specific pretraining
- Analyze model behavior across different architectures

## Models
Two complementary approaches were explored:

### Fine-tuned Encoder–Decoder Models
- **T5-small** (general-domain)
- **SciFive** (biomedical-domain, pretrained on PubMed)
Both models were fine-tuned on a medical Q&A dataset and evaluated for generalization and
domain adaptation.

### Prompt-based Instruction-Following Models
- **Flan-T5**
- **Phi-3-mini**
These models were evaluated in zero-shot, one-shot, and few-shot settings without fine-tuning,
to assess their reasoning and instruction-following capabilities.

## Dataset
- 1,000 medical question–answer pairs
- Optional chain-of-thought explanations
- Split into train / validation / test

## Evaluation
Model outputs were evaluated using:
- ROUGE
- BLEU
- BERTScore

## Key Findings
- SciFive consistently outperformed T5-small in fine-tuning settings
- Phi-3-mini achieved strong performance in prompt-based scenarios
- Domain-specific pretraining and instruction tuning play a crucial role in medical NLP tasks

## Context
Academic project – Text Mining and Natural Language Processing  
University of Pavia - Milano Statale - Milano Bicocca (2024–2025)

