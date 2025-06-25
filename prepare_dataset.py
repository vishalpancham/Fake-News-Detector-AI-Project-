import pandas as pd

# Load both CSV files
fake_df = pd.read_csv("Fake.csv")
true_df = pd.read_csv("True.csv")

# Add labels
fake_df["label"] = 0  # Fake news
true_df["label"] = 1  # Real news

# Combine both
df = pd.concat([fake_df, true_df], ignore_index=True)

# Shuffle
df = df.sample(frac=1).reset_index(drop=True)

# Save to new file
df.to_csv("train.csv", index=False)

print("✅ Combined dataset saved as train.csv")
