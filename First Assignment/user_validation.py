import re
from typing import Optional


class UserValidation:
    """Handles validation for user email, username, phone number, and national ID."""

    @staticmethod
    def validate_email(email: Optional[str]) -> bool:
        """Check if an email address is properly formatted."""
        if not email:
            return False

        pattern = re.compile(r"^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$")
        match = pattern.match(email.strip())
        return bool(match)

    @staticmethod
    def validate_username(username: Optional[str]) -> bool:
        """Check if a username is valid (3–20 chars, letters/numbers/underscores only)."""
        if not username:
            return False

        pattern = re.compile(r"^[A-Za-z0-9_]{3,20}$")
        return bool(pattern.fullmatch(username))

    @staticmethod
    def validate_phone_number(phone: Optional[str]) -> bool:
        """Check if an Egyptian phone number or one with country code (+20) is valid."""
        if not phone:
            return False

        # Strip spaces just in case and check digits only
        phone = phone.strip()
        if not phone.isdigit():
            return False

        localPattern = re.compile(r"^(010|011|012|015)\d{8}$")
        internationalPattern = re.compile(r"^20(10|11|12|15)\d{8}$")

        return bool(localPattern.fullmatch(phone) or internationalPattern.fullmatch(phone))

    @staticmethod
    def validate_national_id(nationalId: Optional[str]) -> bool:
        """Check if the Egyptian national ID is correctly formatted."""
        if not nationalId:
            return False

        if not re.fullmatch(r"\d{14}", nationalId):
            return False

        century = nationalId[0]
        month = int(nationalId[3:5])
        day = int(nationalId[5:7])
        govCode = int(nationalId[7:9])

        # Validate century (2 = 1900s, 3 = 2000s)
        if century not in ("2", "3"):
            return False

        if not (1 <= month <= 12):
            return False

        if not (1 <= day <= 31):
            return False

        if not (1 <= govCode <= 88):
            return False

        return True
