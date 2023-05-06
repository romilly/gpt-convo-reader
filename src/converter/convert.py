#!/usr/bin/env python
# coding: utf-8

import zipfile
import json
import datetime
from typing import List, Dict

from converter.message import Message


class Conversation:
    def __init__(self, title: str, update_time: float, messages: List[Message]):
        self.title = title
        self.update_time = update_time
        self.messages = messages

    def updated(self) -> str:
        # convert epoch to ISO timestamp
        return datetime.datetime.fromtimestamp(self.update_time).isoformat()


def conversation(item: dict) -> Conversation:
    title = item['title']
    update_time = item['update_time']
    mapping = item['mapping']
    raw_messages = [d['message'] for d in mapping.values() if d['message'] is not None]
    messages = [Message.from_json_dict(raw) for raw in raw_messages if 'author' in raw]
    convo = Conversation(title, update_time, messages)
    return convo


def convert(zip_file_name) -> Dict[str, Conversation]:
    file_to_extract = "conversations.json"
    with zipfile.ZipFile(zip_file_name, 'r') as zip_file:
        with zip_file.open(file_to_extract) as file:
            data = json.load(file)
    result = {}
    for item in data:
        convo= conversation(item)
        result[convo.title] = convo
    return result
