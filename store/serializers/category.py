from rest_framework.serializers import ModelSerializer

from store.models import Category


class CategorySerializer(ModelSerializer):
    # TODO: Update, Delete category name
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "seller",
        ]
