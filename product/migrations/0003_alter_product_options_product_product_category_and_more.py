# Generated by Django 4.1.1 on 2022-10-04 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0002_alter_productcategory_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={"verbose_name_plural": "Product"},
        ),
        migrations.AddField(
            model_name="product",
            name="product_category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="product.productsubcategory",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="last_update",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="published",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
