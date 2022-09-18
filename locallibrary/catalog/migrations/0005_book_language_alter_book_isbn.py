# Generated by Django 4.1.1 on 2022-09-18 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_bookinstance_options_bookinstance_borrower_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.language'),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>', max_length=13, verbose_name='isbn'),
        ),
    ]