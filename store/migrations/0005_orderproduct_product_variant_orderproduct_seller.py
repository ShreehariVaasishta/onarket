# Generated by Django 4.0.3 on 2022-04-06 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('store', '0004_order_orderproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='product_variant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.variant'),
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='seller',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.seller'),
        ),
    ]