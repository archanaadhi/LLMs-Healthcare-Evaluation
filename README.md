# Advancing Medical LLMs: A Multi-Metric Evaluation Framework

This repository presents a complete evaluation framework for benchmarking medical large language models (LLMs) across factual and human-aligned dimensions. The project evaluates real-world patient queries using a unified, end-to-end pipeline developed in a single script.

## 🔍 Overview

We introduce a retrieval-grounded, multi-metric evaluation method for assessing LLMs in healthcare applications. The framework scores model responses on six key dimensions:

- **Correctness**
- **Hallucination Resistance**
- **Completeness**
- **Faithfulness**
- **Groundedness**
- **Empathy**

The evaluation is applied to responses from three commercial models:
- ChatGPT (GPT-3.5-turbo)
- Claude (Anthropic)
- DeepSeek

  ## 🎯 Objectives

- Evaluate commercial LLMs on real-world medical queries using a reproducible pipeline.
- Benchmark models across six critical axes: correctness, hallucination, completeness, faithfulness, groundedness, and empathy.
- Enable retrieval-augmented, document-grounded evaluation using real biomedical literature.
- Provide insights into model behavior trade-offs in factual vs. empathetic response quality.

## 📦 Prerequisites

Before running the pipeline, make sure you have:

- Python 3.8+
- API keys for:
  - OpenAI (GPT-3.5-turbo or GPT-4 for gold doc synthesis)
  - Anthropic Claude
  - DeepSeek
- Basic familiarity with:
  - Jupyter Notebooks or Python scripting
  - LangChain and OpenAI API
  - PubMed/EuropePMC for biomedical document retrieval


## ⚙️ How It Works

All logic is contained in a single Python file / Jupyter notebook, which performs:

- Prompt-based LLM querying using LangChain
- PubMed/EuropePMC biomedical document retrieval
- Embedding and FAISS-based relevance scoring
- Pseudo-gold document synthesis via GPT-4
- Prompt-based evaluation across six metrics
- Visualization of results (bar plots, radar charts, trade-off plots)



---

## Team Members
* Archana Adhi
* Havanitha Macha
* Shravan Busireddy
