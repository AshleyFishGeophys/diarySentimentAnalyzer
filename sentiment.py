from nltk.sentiment import SentimentIntensityAnalyzer
import glob

def analyze_diary_journals():
    analyzer = SentimentIntensityAnalyzer()
    filepaths = sorted(glob.glob("diary/*.txt"))
    positivity = []
    negativity = []
    dates = [name.strip("diary\\").strip(".txt") for name in filepaths]
    for file in filepaths:
        with open(file, "r") as f:
            contents = f.read()
        scores = analyzer.polarity_scores(contents)
        positivity.append(scores["pos"])
        negativity.append(scores["neg"])

    return dates, positivity, negativity


if __name__ == "__main__":
    results = analyze_diary_journals()
    print(results)
