import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import csv

def main():
    url = "https://news.ycombinator.com/item?id=42919502"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    elements = soup.find_all(class_="ind", indent=0)
    comments = [e.find_next(class_="comment") for e in elements]

    keywords = {
        "python": 0,
        "javascript": 0,
        "typescript": 0,
        "go": 0,
        "c#": 0,
        "java": 0,
        "rust": 0
    }

    for comment in comments:
        comment_text = comment.get_text().lower()
        words = {w.strip(".,/:;!@") for w in comment_text.split(" ")}
        for k in keywords:
            if k in words:
                keywords[k] += 1

    print(keywords)

    # ➕ Écrire les résultats dans un fichier CSV
    with open("resultats.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Langage", "Mentions"])
        for k, v in keywords.items():
            writer.writerow([k, v])

    # ➕ Afficher un graphique
    plt.bar(keywords.keys(), keywords.values())
    plt.xlabel("Langage")
    plt.ylabel("Nombre de mentions")
    plt.title("Technologies mentionnées dans les offres d'emploi Hacker News")
    plt.show()

if __name__ == "__main__":
    main()
