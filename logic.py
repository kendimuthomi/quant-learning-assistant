import json


def load_topics(file_path="data/topics.json"):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def get_topic_data(topic, file_path="data/topics.json"):
    if not topic or not topic.strip():
        return None

    topics = load_topics(file_path)
    return topics.get(topic.strip().lower())