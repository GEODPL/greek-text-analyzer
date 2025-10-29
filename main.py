import pandas as pd
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import sys

# Προσπάθεια ανάγνωσης αρχείου κειμένου
try:
    with open("sample_text.txt", encoding="utf8") as f:
        text = f.read()
except FileNotFoundError:
    print("❌ Το αρχείο sample_text.txt δεν βρέθηκε. Δημιούργησέ το και ξανατρέξε το πρόγραμμα.")
    sys.exit(1)

# Καθαρισμός κειμένου
words = [w.strip(".,!;:()[]«»\"").lower() for w in text.split()]
counts = Counter(words)

# Εμφάνιση των 10 πιο συχνών λέξεων
print("🔹 Οι 10 πιο συχνές λέξεις είναι:")
for word, freq in counts.most_common(10):
    print(f"{word}: {freq}")

# Δημιουργία word cloud
wc = WordCloud(width=800, height=400, background_color="white")
wc.generate_from_frequencies(counts)
wc.to_file("wordcloud.png")

# Δημιουργία ραβδογράμματος
top_words = counts.most_common(10)
words, freqs = zip(*top_words)
plt.figure(figsize=(8, 5))
plt.bar(words, freqs)
plt.title("Top 10 λέξεις")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top_words.png")

print("\n✅ Δημιουργήθηκαν τα αρχεία 'wordcloud.png' και 'top_words.png'.")
