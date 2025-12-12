# AIMedQA – Medical Question Answering with Transformers

This project investigates Medical Question Answering (Q&A) using transformer-based language
models. The goal is to generate medically accurate, clear, and context-aware responses to
patient-style questions, reflecting the tone and precision of a medical assistant.

The task is framed as a sequence-to-sequence text generation problem, combining data
preprocessing, model adaptation (fine-tuning and prompt engineering), and systematic evaluation.

## Context
Academic project for the *Text Mining and Natural Language Processing* course  
Bachelor’s Degree in Artificial Intelligence – University of Pavia (2024–2025)

## Models
We explored two complementary approaches:

### Fine-tuned Encoder–Decoder Models
- **T5-small** – general-purpose model
- **SciFive** – biomedical model pretrained on PubMed data

### Prompt-based Instruction-Following Models
- **Flan-T5**
- **Phi-3-mini** (3.8B parameters)

Instruction-tuned models were evaluated in zero-shot, one-shot, and few-shot settings, without
fine-tuning.

## Dataset
- 1,000 simulated medical question–answer pairs
- Multiple clinical domains
- Optional chain-of-thought reasoning
- Train / validation / test split

## Methodology
1. **Preprocessing**
   - Text normalization and whitespace cleaning
   - Stopwords and clinical numbers retained to preserve medical meaning
2. **Exploratory Analysis**
   - Term frequency analysis
   - Word clouds
   - Topic modeling with BERTopic
3. **Modeling**
   - Fine-tuning of T5-small and SciFive
   - Prompt engineering for Flan-T5 and Phi-3-mini
4. **Evaluation**
   - ROUGE
   - BLEU
   - BERTScore

## Results
- **SciFive** outperformed T5-small in fine-tuning scenarios, highlighting the benefit of
  domain-specific pretraining
- **Phi-3-mini** achieved strong performance in prompt-based settings, generating fluent and
  context-aware answers
- Few-shot prompting consistently improved relevance compared to zero-shot approaches

## Challenges
The main limitations were related to computational resources, which constrained the size of
models that could be fully fine-tuned.

## Conclusion
This project provided hands-on experience with medical NLP, highlighting the trade-offs between
fine-tuning and prompt-based approaches. Beyond model performance, the work emphasized
the importance of domain adaptation, evaluation strategies, and interpretability in real-world
medical applications.
