# Generated by Django 4.1.1 on 2022-10-04 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0003_alter_product_options_product_product_category_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="set_as_banner",
            field=models.BooleanField(default=False, verbose_name="setAsBanner"),
        ),
        migrations.AlterField(
            model_name="product",
            name="is_documented",
            field=models.BooleanField(default=False, verbose_name="isDocumented"),
        ),
        migrations.AlterField(
            model_name="product",
            name="is_high_resolution",
            field=models.BooleanField(default=False, verbose_name="isHighResolution"),
        ),
        migrations.AlterField(
            model_name="product",
            name="is_responsive",
            field=models.BooleanField(default=False, verbose_name="isResponsive"),
        ),
    ]
