"""
This module contains shared/common base models within the entire app
"""

import uuid
from django.db import models


class BaseModel(models.Model):
    """
    Base model for other models to inherit
    """
    id = models.CharField(
        max_length=64, primary_key=True, db_index=True, default=uuid.uuid4, editable=False
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Indicate this model is abstract class
        """
        abstract = True
