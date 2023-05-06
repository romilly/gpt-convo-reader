from io import StringIO
from typing import List, Dict, Any


class Message:
    def __init__(self, role: str, contents: List[str]):
        self.role = role
        self.contents = contents

    def __str__(self) -> str:
        return f"{self.role}: {self.text()}"

    def text(self) -> str:
        return '\n'.join(self.contents)

    def markdown(self):
        sio = StringIO()
        sio.write(f"_{self.role}_: ")
        sio.write('\n\n'.join(self.contents))
        result = sio.getvalue()
        sio.close()
        return result

    def __repr__(self):
        return str(self)

    @classmethod
    def from_json_dict(cls, json_dict: Dict[str, Any]) -> 'Message':
        author = json_dict['author']
        role = author['role']
        parts = json_dict['content']['parts']
        return cls(role=role, contents=parts)
