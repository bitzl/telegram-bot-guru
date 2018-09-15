from dataclasses import dataclass
from itertools import chain

import yaml
from typing import List


@dataclass
class Fact:
    info: str
    tags: List[str]
    types: List[str]


def load_facts(facts_path):
    with open(facts_path, 'r') as facts_source:
        return [Fact(item['info'], item['tags'], item['types']) for item in yaml.load(facts_source)]


class Facts:
    def __init__(self, facts):
        self.facts = facts

    @staticmethod
    def from_file(facts_path):
        return Facts(load_facts(facts_path))

    def with_tags(self, tags):
        return Facts(fact for fact in self.facts if all(tag in fact.tags for tag in tags))

    def with_types(self, types):
        return Facts(fact for fact in self.facts if all(t in fact.types for t in types))

    def get_types(self):
        return set(chain.from_iterable(fact.types for fact in self.facts))

    def get_tags(self):
        return set(chain.from_iterable(fact.tags for fact in self.facts))
