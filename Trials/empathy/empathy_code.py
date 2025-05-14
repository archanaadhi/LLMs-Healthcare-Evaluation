import pandas as pd
import openai
import re
import matplotlib.pyplot as plt
import time

# Load your Excel file
df = pd.read_excel("sample_100.xlsx")

# Set your OpenAI API key
openai.api_key = ""
# Step 1: Evaluate Empathy
def evaluate_empathy(row):
    question = row["input"]
    response1 = row["output"]
    response2 = row["GPT_response"]
    response3 = row["Gemini_response"]

    prompt = f"""
You are an empathy evaluator. Given a user question and a response, rate the empathy level of the response on a scale from 1 (not empathetic) to 5 (highly empathetic).

Q: I had cervical spine surgery and now my arm feels numb. I’m scared something went wrong.
A: That sounds very distressing. Post-surgery symptoms can be scary, and I’m here to help you figure it out. Let’s take a look together. → Empathy Rating: 5

Q: I’ve had a sore throat for days and I feel weak.
A: It might be viral. Take rest. → Empathy Rating: 2

Q: My fingers are tingling and I can’t sleep.
A: Try some hand exercises. → Empathy Rating: 2

Q: I’ve been feeling really anxious and can't stop overthinking about my symptoms.
A: I’m really sorry you're going through this. Anxiety can make everything feel worse — let’s talk through what you’re experiencing. → Empathy Rating: 5

Now, evaluate the following:

Q: {question}
A1: {response1} → Empathy Rating:
A2: {response2} → Empathy Rating:
A3: {response3} → Empathy Rating:
"""

    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        return completion["choices"][0]["message"]["content"]
    except Exception as e:
        return str(e)

# Run on full dataset
print("🔄 Evaluating empathy for all rows...")
df["empathy_scores"] = df.apply(evaluate_empathy, axis=1)

# Step 2: Extract numeric scores
def extract_scores(text):
    try:
        matches = re.findall(r"A\d:\s*Empathy Rating:\s*(\d)", str(text))
        return [int(score) for score in matches] if len(matches) == 3 else [None, None, None]
    except:
        return [None, None, None]

df[["Doctor_output_score", "GPT_score", "Gemini_score"]] = df["empathy_scores"].apply(extract_scores).apply(pd.Series)

# Step 3: Save to file
df.to_excel("sample_100_empathy_scored.xlsx", index=False)
print("✅ Saved results to 'sample_100_empathy_scored.xlsx'")

# Step 4: Compute averages and plot
avg_scores = {
    "Doctor_output": df["Doctor_output_score"].mean(),
    "GPT": df["GPT_score"].mean(),
    "Gemini": df["Gemini_score"].mean()
}

# Plot
plt.figure(figsize=(8, 5))
plt.bar(avg_scores.keys(), avg_scores.values(), color=["#4E79A7", "#F28E2B", "#76B7B2"])
plt.title("Average Empathy Ratings by Response Source")
plt.ylabel("Empathy Score (1 to 5)")
plt.ylim(0, 5)
plt.grid(axis='y')
plt.tight_layout()
plt.show()
