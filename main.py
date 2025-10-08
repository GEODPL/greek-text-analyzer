from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import re
import pandas as pd

# --- 1. Φόρτωση ελληνικού κειμένου ---
with open("sample_text.txt", encoding="utf8") as f:
    text = f.read().lower()

# --- 2. Καθαρισμός ---
text = re.sub(r"[^α-ωάέήίόύώϊϋΐΰ\s]", " ", text)
words = [w for w in text.split() if len(w) > 1]

# --- 3. Συχνότητα λέξεων ---
counter = Counter(words)
most_common = counter.most_common(10)

# --- 4. Εμφάνιση ---
print("📊 10 πιο συχνές λέξεις:")
for w, c in most_common:
    print(f"{w}: {c}")

# --- 5. Λεξικό συναισθήματος ---
lexicon = pd.read_csv("sentiment_lexicon.csv")
pos = set(lexicon[lexicon["sentiment"] == "positive"]["word"])
neg = set(lexicon[lexicon["sentiment"] == "negative"]["word"])

pos_count = sum(w in pos for w in words)
neg_count = sum(w in neg for w in words)
total = len(words)

print(f"\n😊 Θετικό συναίσθημα: {pos_count / total * 100:.2f}%")
print(f"☹️  Αρνητικό συναίσθημα: {neg_count / total * 100:.2f}%")

# --- 6. Bar chart ---
plt.bar([w for w, _ in most_common], [c for _, c in most_common])
plt.title("Top 10 λέξεις στο κείμενο")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top_words.png")
plt.show()

# --- 7. Word Cloud ---
wc = WordCloud(width=800, height=400, background_color="white", collocations=False).generate(" ".join(words))
wc.to_file("wordcloud.png")
print("\n📸 Αποθηκεύτηκαν τα αρχεία top_words.png & wordcloud.png")
