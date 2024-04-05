"""
This module contains custom file upload validators.
"""

from math import ceil
import mimetypes
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from core.settings import FILE_UPLOAD_MAX_MEMORY_SIZE


class Validators:
    """
    This class contains static methods for password validators
    and file type and size validators.
    """
    @staticmethod
    def convert_to_megabyte(file_size):
        """
        This method converts file size to megabytes.
        """
        file_size_in_mb = round(file_size / (1000 * 1000))
        return ceil(file_size_in_mb)

    @staticmethod
    def validate_file_size(document):
        """
        This method validates file size and type.
        """
        allowed_content_types = ['application/pdf',
                                 'image/jpeg', 'image/jpg', 'image/png']
        if not document:
            messages.error("No file selected.....")

        if document.size > FILE_UPLOAD_MAX_MEMORY_SIZE:
            messages.error(
                f"File shouldn't be larger than {Validators.convert_to_megabyte(FILE_UPLOAD_MAX_MEMORY_SIZE)}MB."
            )

        fs = FileSystemStorage()
        filename = fs.save(document.name, document)
        file_type = mimetypes.guess_type(filename)[0]
        if file_type not in allowed_content_types:
            messages.error(
                "Invalid file, please upload an image file with extensions (png, jpg or jpeg).")
        return document

    @staticmethod
    def validate_password(password: str, confirm_password: str):
        """
        This method validate password and confirm password fields
        """
        if confirm_password != password:
            return False
        return True

    @staticmethod
    def validate_password_length(password: str):
        """
        This method validates password length.
        """
        if len(password) >= 10:
            return True
        return False
