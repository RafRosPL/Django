# Generated by Django 3.2.5 on 2021-07-06 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='guestion_text',
            new_name='question_text',
        ),
    ]
