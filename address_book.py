from collections import UserDict
from typing import Optional

from fields import Record


class AddressBook(UserDict):
    """Collection of contact records, keyed by contact name."""

    def add_record(self, new_record: Record) -> None:
        name = new_record.name.value
        if name in self.data:
            raise ValueError(f"Contact {name} already exists.")
        self.data[name] = new_record

    def find(self, name: str) -> Optional[Record]:
        return self.data.get(name)

    def delete(self, name: str) -> None:
        if name not in self.data:
            raise ValueError(f"Contact {name} not found.")
        del self.data[name]
