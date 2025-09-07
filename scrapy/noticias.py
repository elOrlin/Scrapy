import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime


class NewsScreaper:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })

    def scrape_hacker_news(self):
        "Acraper de noticias de Hacker News"
        try:
            response = self.session.get('https://news.ycombinator.com/')
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')

            stories = []
            story_links = soup.find_all('span', class_='titleline')

            for link in story_links[:30]:
                title_elem = link.find('a')
                if title_elem:
                    stories.append({
                        'title': title_elem.text.strip(),
                        'url': title_elem.get('href', ''),
                        'scraped_at': datetime.now().isoformat()
                    })

            return stories

        except Exception as e:
            print(f"Error scraping Hacker News: {e}")
            return []

    def save_to_json(self, data, filename='hacker_news.json'):
        """Guarda los datos en un archivo JSON"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def scrape_and_save(self):
        """Metodo principal para raspar y guardar las noticias"""
        print("Iniciardo scraping de Hacker News...")
        stories = self.scrape_hacker_news()

        if stories:
            self.save_to_json(stories, 'hacker_news.json')
            print(f"Guardado {len(stories)} historias en hacker_news.json \n")

            # Mostrar las primeras 3 historias
            for i, story in enumerate(stories[:30], start=1):
                print(f"{i}. {story['title']}")
                print(f"{story['url']}\n")

        else:
            print("No se encontraron historias.")


# Uso del scraper
if __name__ == "__main__":
    scraper = NewsScreaper()
    scraper.scrape_and_save()
