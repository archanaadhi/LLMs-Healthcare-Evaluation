## 🧠 Empathy Evaluation: What Worked & What Didn’t

### ✅ Techniques That Worked

**1. Few-Shot Prompting with GPT-3.5 (OpenAI API)**  
- **What we did:** Prompted GPT-3.5 with labeled examples to rate empathy (1–10).  
- **Why it worked:** Clean, consistent prompts led to reliable scores.  
- **Best for:** Small to medium-scale evaluations with well-tuned prompts.  
- ⚠️ **Limitation:** Ran into API quota limits during extended runs.

---

### ⚠️ Techniques That Didn't Work Well

**1. `nateraw/bert-base-uncased-emotion`**  
- Labeled serious responses with irrelevant emotions like "joy".  
- ❌ Not trained on medical data — poor domain relevance.

**2. `mrm8488/t5-base-finetuned-emotion`**  
- Outputs were noisy and difficult to parse.  
- ❌ No clear confidence or numeric empathy scoring.

**3. `distilbert-base-uncased-emotion` (Transformer-based)**  
- Misclassified serious/neutral responses as "joy".  
- ❌ Could not capture supportive or empathetic tone.  
- ✔️ Works better for social media or general emotional tone.

---
