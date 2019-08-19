"""
skip.py

Example usage of skip and skip_if attributes.

Usage:
    $ pipenv install
    $ pipenv run skip.py
"""

from typing import List, Dict
from dataclasses import dataclass, field
from serde import serialize
from serde.json import to_json


@serialize
@dataclass
class Resource:
    name: str
    hash: str
    metadata: Dict[str, str] = field(default_factory=dict, metadata={'serde_skip': True})


def main():
    resources = [
        Resource("Stack Overflow", "b6469c3f31653d281bbbfa6f94d60fea130abe38"),
        Resource("GitHub", "5cb7a0c47e53854cd00e1a968de5abce1c124601", metadata={"headquarters": "San Francisco"}),
    ]
    print(to_json(resources))


if __name__ == '__main__':
    main()