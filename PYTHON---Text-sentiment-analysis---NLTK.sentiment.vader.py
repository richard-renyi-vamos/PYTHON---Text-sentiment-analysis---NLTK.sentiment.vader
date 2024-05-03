import tkinter as tk
from tkinter import ttk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def analyze_sentiment():
    text = text_entry.get("1.0", tk.END)
    analyzer = SentimentIntensityAnalyzer()
    sentiment_scores = analyzer.polarity_scores(text)
    display_results(sentiment_scores)

def display_results(scores):
    for key, value in scores.items():
        result_label = tk.Label(result_frame, text=f"{key.capitalize()}: {value}", font=("Helvetica", 12))
        result_label.pack()

# Create main window
root = tk.Tk()
root.title("Text Sentiment Analyzer")

# Create text entry
text_entry = tk.Text(root, height=10, width=50, wrap=tk.WORD)
text_entry.pack(pady=10)

# Create analyze button
analyze_button = ttk.Button(root, text="Analyze", command=analyze_sentiment)
analyze_button.pack()

# Create frame for results
result_frame = tk.Frame(root)
result_frame.pack(pady=10)

# Run the GUI loop
root.mainloop()
