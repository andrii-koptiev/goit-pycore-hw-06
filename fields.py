from typing import Any, Optional


class Field:
    """Base class representing a generic data field."""

    def __init__(self, value: Any, required: bool = False) -> None:
        self.value: Any = value
        self.required: bool = required


class Name(Field):
    """Inherited class specifically for names (Required)."""

    def __init__(self, value: str) -> None:
        # Enforce that value must be a string and required is True
        super().__init__(value=value, required=True)

        # Simple validation block
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name field cannot be empty.")

    # Add name-specific functionality
    def to_uppercase(self) -> str:
        return self.value.upper()


class Phone(Field):
    """Phone number (optional): if given, must be exactly 10 ASCII digits."""

    def __init__(self, value: Optional[str] = None, required: bool = False) -> None:
        super().__init__(value=value, required=required)

        if value is None:
            if required:
                raise ValueError("Phone is required but no value was given.")
            return

        if not isinstance(value, str) or not (value.isascii() and value.isdigit()):
            raise ValueError("Phone number must contain only digits")
        if len(value) != 10:
            raise ValueError("Phone number should be 10 digits long")


class Record:
    """A contact: one required name and a list of phone numbers."""

    def __init__(self, name: str) -> None:
        self.name: Name = Name(name)
        self.phones: list[Phone] = []

    def add_phone(self, phone: str) -> None:
        new_phone = Phone(phone)
        if self.find_phone(new_phone.value) is not None:
            raise ValueError(f"Phone {phone} already exists.")
        self.phones.append(new_phone)

    def remove_phone(self, phone_to_remove: str) -> None:
        phone = self.find_phone(phone_to_remove)
        if phone is None:
            raise ValueError(f"Phone {phone_to_remove} not found.")
        self.phones.remove(phone)

    def edit_phone(self, phone_to_edit: str, new_phone: str) -> None:
        for index, phone in enumerate(self.phones):
            if phone.value == phone_to_edit:
                self.phones[index] = Phone(new_phone)
                return
        raise ValueError(f"Phone {phone_to_edit} not found.")

    def find_phone(self, phone_to_found: str) -> Optional[Phone]:
        for phone in self.phones:
            if phone.value == phone_to_found:
                return phone
        return None

    def __str__(self) -> str:
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value or '-' for p in self.phones)}"
