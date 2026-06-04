import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_rel

# =========================================================
# LOAD DATA
# =========================================================
df = pd.read_csv("survey_data.csv")

# =========================================================
# CALCULATE SUS SCORE
# =========================================================
sus_items = [
    "SUS_Q1","SUS_Q2","SUS_Q3","SUS_Q4","SUS_Q5",
    "SUS_Q6","SUS_Q7","SUS_Q8","SUS_Q9","SUS_Q10"
]

def calculate_sus(row):
    score = 0

    for i, item in enumerate(sus_items, start=1):
        value = row[item]

        # Odd items
        if i % 2 == 1:
            score += (value - 1)

        # Even items (reverse-scored)
        else:
            score += (5 - value)

    return score * 2.5

df["SUS_Score"] = df.apply(calculate_sus, axis=1)

# =========================================================
# CALCULATE UEQ-S SCORES
# Convert 1-7 scale to -3 to +3
# =========================================================
ueq_pragmatic = ["UEQ_P1", "UEQ_P2", "UEQ_P3", "UEQ_P4"]
ueq_hedonic = ["UEQ_H1", "UEQ_H2", "UEQ_H3", "UEQ_H4"]

for col in ueq_pragmatic + ueq_hedonic:
    df[col + "_scaled"] = df[col] - 4

df["UEQ_Pragmatic"] = df[
    [c + "_scaled" for c in ueq_pragmatic]
].mean(axis=1)

df["UEQ_Hedonic"] = df[
    [c + "_scaled" for c in ueq_hedonic]
].mean(axis=1)




# =========================================================
# SPLIT CONDITIONS
# =========================================================
museum = df[df["CONDITION"] == "HAT BOI"]
baseline = df[df["CONDITION"] == "GA&C"]

# =========================================================
# PRINT STATISTICS
# =========================================================
museum_sus = museum["SUS_Score"]
baseline_sus = baseline["SUS_Score"]


t_sus, p_sus = ttest_rel(
    museum_sus.reset_index(drop=True),
    baseline_sus.reset_index(drop=True)
)

print("==========================================")
print(" SURVEY ANALYSIS RESULTS")
print("==========================================\n")

print("--- SYSTEM USABILITY SCALE (SUS) ---")
print(f"Museum:   Mean = {museum_sus.mean():.1f}, SD = {museum_sus.std(ddof=1):.1f}")
print(f"Baseline: Mean = {baseline_sus.mean():.1f}, SD = {baseline_sus.std(ddof=1):.1f}")
print(f"Paired T-Test: t = {t_sus:.2f}, p-value = {p_sus:.4e}\n")

# =========================================================
# UEQ-S DESCRIPTIVE STATISTICS + PAIRED T-TESTS
# =========================================================

museum_prag = museum["UEQ_Pragmatic"]
baseline_prag = baseline["UEQ_Pragmatic"]

museum_hed = museum["UEQ_Hedonic"]
baseline_hed = baseline["UEQ_Hedonic"]

# Paired t-tests
t_prag, p_prag = ttest_rel(
    museum_prag.reset_index(drop=True),
    baseline_prag.reset_index(drop=True)
)

t_hed, p_hed = ttest_rel(
    museum_hed.reset_index(drop=True),
    baseline_hed.reset_index(drop=True)
)

# Print UEQ-S results
print("--- USER EXPERIENCE QUESTIONNAIRE (UEQ-S) ---\n")

print("[Pragmatic Quality]")
print(
    f"Museum:   Mean = {museum_prag.mean():.2f}, "
    f"SD = {museum_prag.std(ddof=1):.2f}"
)

print(
    f"Baseline: Mean = {baseline_prag.mean():.2f}, "
    f"SD = {baseline_prag.std(ddof=1):.2f}"
)

print(
    f"Paired T-Test: t = {t_prag:.2f}, "
    f"p-value = {p_prag:.4e}\n"
)

print("[Hedonic Quality]")
print(
    f"Museum:   Mean = {museum_hed.mean():.2f}, "
    f"SD = {museum_hed.std(ddof=1):.2f}"
)

print(
    f"Baseline: Mean = {baseline_hed.mean():.2f}, "
    f"SD = {baseline_hed.std(ddof=1):.2f}"
)

print(
    f"Paired T-Test: t = {t_hed:.2f}, "
    f"p-value = {p_hed:.4e}\n"
)



# =========================================================
# VISUALIZATION STYLE
# =========================================================
sns.set_theme(style="whitegrid")

# =========================================================
# SUS VIOLIN PLOT
# =========================================================
plt.figure(figsize=(8, 6))

sns.violinplot(
    data=df,
    x="CONDITION",
    y="SUS_Score",
    inner="box"
)

plt.title("System Usability Scale (SUS) Across Conditions")
plt.xlabel("Condition")
plt.ylabel("SUS Score")

plt.tight_layout()
plt.show()

# =========================================================
# UEQ DATAFRAME FOR VISUALIZATION
# =========================================================
ueq_long = pd.concat([
    pd.DataFrame({
        "Condition": museum["CONDITION"],
        "Score": museum["UEQ_Pragmatic"],
        "Dimension": "Pragmatic"
    }),
    pd.DataFrame({
        "Condition": baseline["CONDITION"],
        "Score": baseline["UEQ_Pragmatic"],
        "Dimension": "Pragmatic"
    }),
    pd.DataFrame({
        "Condition": museum["CONDITION"],
        "Score": museum["UEQ_Hedonic"],
        "Dimension": "Hedonic"
    }),
    pd.DataFrame({
        "Condition": baseline["CONDITION"],
        "Score": baseline["UEQ_Hedonic"],
        "Dimension": "Hedonic"
    })
])

# =========================================================
# UEQ-S VIOLIN PLOT
# =========================================================
plt.figure(figsize=(10, 6))

sns.violinplot(
    data=ueq_long,
    x="Dimension",
    y="Score",
    hue="Condition",
    split=True,
    inner="box"
)

plt.title("UEQ-S Scores Across Conditions")
plt.xlabel("UEQ-S Dimension")
plt.ylabel("UEQ-S Score (-3 to +3)")

plt.axhline(0, linestyle="--")

plt.tight_layout()
plt.show()
