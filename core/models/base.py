from django.db import models


class BaseModel(models.Model):
    """Asbtract base model which can be inherited in all models which has common fields"""

    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
