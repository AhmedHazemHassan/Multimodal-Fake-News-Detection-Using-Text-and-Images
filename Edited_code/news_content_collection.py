import json
import logging
import time
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
from tqdm import tqdm
from newspaper import Article

from util.util import DataCollector
from util.util import Config, create_dir
from util import Constants

MAX_THREADS = 16  # Adjust based on your CPU


def crawl_link_article(url):
    try:
        if not url.startswith('http'):
            url = 'http://' + url

        article = Article(url)
        article.download()
        time.sleep(1)
        article.parse()

        if not article.is_parsed:
            return None

        return {
            'url': url,
            'text': article.text,
            'images': list(article.images),
            'top_img': article.top_image,
            'keywords': article.keywords,
            'authors': article.authors,
            'canonical_link': article.canonical_link,
            'title': article.title,
            'meta_data': article.meta_data,
            'movies': article.movies,
            'publish_date': article.publish_date.timestamp() if article.publish_date else None,
            'source': article.source_url,
            'summary': article.summary
        }
    except Exception as e:
        logging.warning(f"[✗] Failed downloading article from URL: {url} | {str(e)}")
        return None


def crawl_news_article(url):
    article = crawl_link_article(url)
    if article is None:
        try:
            archive_url = get_archive_url(url)
            if archive_url:
                return crawl_link_article(archive_url)
        except:
            return None
    return article


def get_archive_url(url):
    try:
        arch_url = f"http://web.archive.org/cdx/search/cdx?url={url}&output=json"
        r = requests.get(arch_url)
        records = json.loads(r.text)[1:]  # Skip header row
        if records:
            return f"https://web.archive.org/web/{records[0][1]}/{records[0][2]}"
    except:
        return None


def process_news_item(news, save_dir, only_ids):
    try:
        if only_ids and news.news_id not in only_ids:
            return None

        article_dir = os.path.join(save_dir, news.news_id)
        article_path = os.path.join(article_dir, "news content.json")

        if os.path.exists(article_path):
            return None

        create_dir(article_dir)
        article = crawl_news_article(news.news_url)

        if article:
            with open(article_path, "w", encoding="utf-8") as f:
                json.dump(article, f, ensure_ascii=False, indent=2)
            logging.info(f"[✓] Finished {news.news_id}")
            return news.news_id
    except Exception as e:
        logging.warning(f"[✗] Failed {news.news_id} | {str(e)}")
    return None


def collect_news_articles(news_list, news_source, label, config: Config, only_ids=None):
    save_dir = os.path.join(config.dump_location, news_source, label)
    create_dir(save_dir)

    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        futures = [
            executor.submit(process_news_item, news, save_dir, only_ids)
            for news in news_list
        ]

        for _ in tqdm(as_completed(futures), total=len(futures), desc=f"Processing {news_source}/{label}"):
            pass


class NewsContentCollector(DataCollector):
    def __init__(self, config):
        super(NewsContentCollector, self).__init__(config)

    def collect_data(self, choices, only_ids=None):
        for choice in choices:
            news_list = self.load_news_file(choice)
            collect_news_articles(news_list, choice["news_source"], choice["label"], self.config, only_ids=only_ids)
