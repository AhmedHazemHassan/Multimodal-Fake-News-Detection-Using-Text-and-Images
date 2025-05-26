# # Patch for Python 3.11+ compatibility with old libraries using inspect.formatargspec
# import inspect

# if not hasattr(inspect, 'formatargspec'):
#     from inspect import Signature, _empty

#     def formatargspec(*args, **kwargs):
#         return str(Signature(parameters=[]))

#     inspect.formatargspec = formatargspec

# import csv
# import json
# import logging
# import time

# from util.util import Config, News

# from news_content_collection import NewsContentCollector
# from retweet_collection import RetweetCollector
# from tweet_collection import TweetCollector
# from user_profile_collection import UserProfileCollector, UserTimelineTweetsCollector, UserFollowingCollector, \
#     UserFollowersCollector


# class DataCollectorFactory:

#     def __init__(self, config):
#         self.config = config

#     def get_collector_object(self, feature_type):

#         if feature_type == "news_articles":
#             print("Got news articles")
#             return NewsContentCollector(self.config)
#         elif feature_type == "tweets":
#             print("Got tweets")
#             return TweetCollector(self.config)
#         elif feature_type == "retweets":
#             print("Got retweets")
#             return RetweetCollector(self.config)
#         elif feature_type == "user_profile":
#             print("Got user profile")
#             return UserProfileCollector(self.config)
#         elif feature_type == "user_timeline_tweets":
#             print("Got user timeline tweets")
#             return UserTimelineTweetsCollector(self.config)
#         elif feature_type == "user_following":
#             print("Got user following")
#             return UserFollowingCollector(self.config)
#         elif feature_type == "user_followers":
#             print("Got user followers")
#             return UserFollowersCollector(self.config)


# def init_config():
#     json_object = json.load(open("config.json"))

#     config = Config(json_object["dataset_dir"], json_object["dump_location"], json_object["tweet_keys_file"],
#                     int(json_object["num_process"]))

#     data_choices = json_object["data_collection_choice"]
#     data_features_to_collect = json_object["data_features_to_collect"]

#     return config, data_choices, data_features_to_collect

# def init_logging(config):
#     format = '%(asctime)s %(process)d %(module)s %(levelname)s %(message)s'
#     # format = '%(message)s'
#     logging.basicConfig(
#         filename='data_collection_{}.log'.format(str(int(time.time()))),
#         level=logging.INFO,
#         format=format)
#     logging.getLogger('requests').setLevel(logging.CRITICAL)


# def download_dataset():
#     config, data_choices, data_features_to_collect = init_config()
#     init_logging(config)
#     data_collector_factory = DataCollectorFactory(config)

#     for feature_type in data_features_to_collect:
#         data_collector = data_collector_factory.get_collector_object(feature_type)
#         data_collector.collect_data(data_choices)


# if __name__ == "__main__":
#     download_dataset()


# # Patch for Python 3.11+ compatibility with old libraries using inspect.formatargspec
# import inspect
# import os
# import newspaper
# import re

# if not hasattr(inspect, 'formatargspec'):
#     from inspect import Signature, _empty

#     def formatargspec(*args, **kwargs):
#         return str(Signature(parameters=[]))

#     inspect.formatargspec = formatargspec

# # Patch: Fix newspaper3k resource directory error on Windows
# home = os.path.expanduser("~")
# resource_dir = os.path.join(home, "newspaper_resources")
# os.makedirs(resource_dir, exist_ok=True)
# # newspaper.config.set('RESOURCE_DIRECTORY', resource_dir)
# from newspaper.configuration import Configuration
# config = Configuration()
# # config.set('RESOURCE_DIRECTORY', resource_dir)
# config.RESOURCE_DIRECTORY = resource_dir

# import csv
# import json
# import logging
# import time

# from util.util import Config, News

# from news_content_collection import NewsContentCollector
# from retweet_collection import RetweetCollector
# from tweet_collection import TweetCollector
# from user_profile_collection import UserProfileCollector, UserTimelineTweetsCollector, UserFollowingCollector, \
#     UserFollowersCollector

# # ----------------------
# # Parse failed articles from log
# # ----------------------
# def extract_failed_articles_from_log(log_path):
#     failed_urls = []
#     failed_ids = set()

#     with open(log_path, 'r', encoding='utf-8') as log:
#         for line in log:
#             if "ERROR Exception in getting data from url" in line:
#                 match = re.search(r"from url (\S+)", line)
#                 if match:
#                     url = match.group(1)
#                     failed_urls.append(url)

#                     if "gossipcop-" in url:
#                         id_match = re.search(r"gossipcop-(\d+)", url)
#                         if id_match:
#                             failed_ids.add(f"gossipcop-{id_match.group(1)}")
#                     elif "politifact-" in url:
#                         id_match = re.search(r"politifact-(\d+)", url)
#                         if id_match:
#                             failed_ids.add(f"politifact-{id_match.group(1)}")

#     return failed_urls, failed_ids


# class DataCollectorFactory:

#     def __init__(self, config):
#         self.config = config

#     def get_collector_object(self, feature_type):

#         if feature_type == "news_articles":
#             print("Got news articles")
#             return NewsContentCollector(self.config)
#         elif feature_type == "tweets":
#             print("Got tweets")
#             return TweetCollector(self.config)
#         elif feature_type == "retweets":
#             print("Got retweets")
#             return RetweetCollector(self.config)
#         elif feature_type == "user_profile":
#             print("Got user profile")
#             return UserProfileCollector(self.config)
#         elif feature_type == "user_timeline_tweets":
#             print("Got user timeline tweets")
#             return UserTimelineTweetsCollector(self.config)
#         elif feature_type == "user_following":
#             print("Got user following")
#             return UserFollowingCollector(self.config)
#         elif feature_type == "user_followers":
#             print("Got user followers")
#             return UserFollowersCollector(self.config)


# def init_config():
#     json_object = json.load(open("config.json"))

#     config = Config(json_object["dataset_dir"], json_object["dump_location"], json_object["tweet_keys_file"],
#                     int(json_object["num_process"]))

#     data_choices = json_object["data_collection_choice"]
#     data_features_to_collect = json_object["data_features_to_collect"]

#     return config, data_choices, data_features_to_collect


# def init_logging(config):
#     format = '%(asctime)s %(process)d %(module)s %(levelname)s %(message)s'
#     logging.basicConfig(
#         filename='data_collection_{}.log'.format(str(int(time.time()))),
#         level=logging.INFO,
#         format=format)
#     logging.getLogger('requests').setLevel(logging.CRITICAL)


# def download_dataset():
#     config, data_choices, data_features_to_collect = init_config()
#     init_logging(config)
#     data_collector_factory = DataCollectorFactory(config)

#     # Load failed article IDs from the last log file (replace with your actual log filename)
#     failed_urls, failed_ids = extract_failed_articles_from_log("data_collection_1745238033.log")
#     print(f"[!] Retrying {len(failed_ids)} failed articles only")

#     for feature_type in data_features_to_collect:
#         data_collector = data_collector_factory.get_collector_object(feature_type)
#         # Pass failed_ids to restrict retries
#         data_collector.collect_data(data_choices, only_ids=failed_ids)


# if __name__ == "__main__":
#     download_dataset()

# Patch for Python 3.11+ compatibility with old libraries using inspect.formatargspec
import inspect
import os
import re
import json
import logging
import time
from newspaper.configuration import Configuration

from util.util import Config, News
from news_content_collection import NewsContentCollector
from retweet_collection import RetweetCollector
from tweet_collection import TweetCollector
from user_profile_collection import UserProfileCollector, UserTimelineTweetsCollector, UserFollowingCollector, \
    UserFollowersCollector

if not hasattr(inspect, 'formatargspec'):
    from inspect import Signature, _empty
    def formatargspec(*args, **kwargs):
        return str(Signature(parameters=[]))
    inspect.formatargspec = formatargspec

# Patch: Fix newspaper3k resource directory error on Windows
home = os.path.expanduser("~")
resource_dir = os.path.join(home, "newspaper_resources")
os.makedirs(resource_dir, exist_ok=True)
config_patch = Configuration()
config_patch.RESOURCE_DIRECTORY = resource_dir

# ----------------------
# Parse failed articles from log
# ----------------------
def extract_failed_articles_from_log(log_path):
    failed_urls = []
    failed_ids = set()

    with open(log_path, 'r', encoding='utf-8') as log:
        for line in log:
            if "ERROR Exception in getting data from url" in line or "[✗] Failed" in line:
                match = re.search(r"from url (\S+)|Failed (\S+)", line)
                if match:
                    url = match.group(1) or ""
                    news_id = match.group(2) or ""
                    if news_id:
                        failed_ids.add(news_id)
                    elif "gossipcop-" in url:
                        id_match = re.search(r"gossipcop-(\d+)", url)
                        if id_match:
                            failed_ids.add(f"gossipcop-{id_match.group(1)}")
                    elif "politifact-" in url:
                        id_match = re.search(r"politifact-(\d+)", url)
                        if id_match:
                            failed_ids.add(f"politifact-{id_match.group(1)}")
    return failed_urls, failed_ids


class DataCollectorFactory:
    def __init__(self, config):
        self.config = config

    def get_collector_object(self, feature_type):
        if feature_type == "news_articles":
            print("Got news articles")
            return NewsContentCollector(self.config)
        elif feature_type == "tweets":
            print("Got tweets")
            return TweetCollector(self.config)
        elif feature_type == "retweets":
            print("Got retweets")
            return RetweetCollector(self.config)
        elif feature_type == "user_profile":
            print("Got user profile")
            return UserProfileCollector(self.config)
        elif feature_type == "user_timeline_tweets":
            print("Got user timeline tweets")
            return UserTimelineTweetsCollector(self.config)
        elif feature_type == "user_following":
            print("Got user following")
            return UserFollowingCollector(self.config)
        elif feature_type == "user_followers":
            print("Got user followers")
            return UserFollowersCollector(self.config)


def init_config():
    json_object = json.load(open("config.json"))

    config = Config(json_object["dataset_dir"], json_object["dump_location"], json_object["tweet_keys_file"],
                    int(json_object["num_process"]))

    data_choices = json_object["data_collection_choice"]
    data_features_to_collect = json_object["data_features_to_collect"]

    return config, data_choices, data_features_to_collect


def init_logging(config):
    format = '%(asctime)s %(process)d %(module)s %(levelname)s %(message)s'
    logging.basicConfig(
        filename='data_collection_{}.log'.format(str(int(time.time()))),
        level=logging.INFO,
        format=format)
    logging.getLogger('requests').setLevel(logging.CRITICAL)


def download_dataset():
    config, data_choices, data_features_to_collect = init_config()
    init_logging(config)
    data_collector_factory = DataCollectorFactory(config)

    # Optional: log retry setup (comment out if not retrying)
    failed_urls, failed_ids = extract_failed_articles_from_log("data_collection_1745496726.log")
    print(f"[!] Retrying {len(failed_ids)} failed articles only")

    for feature_type in data_features_to_collect:
        data_collector = data_collector_factory.get_collector_object(feature_type)
        data_collector.collect_data(data_choices, only_ids=failed_ids)


if __name__ == "__main__":
    download_dataset()
