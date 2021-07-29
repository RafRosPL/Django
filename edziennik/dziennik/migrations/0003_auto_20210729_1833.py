# Generated by Django 3.2.5 on 2021-07-29 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dziennik', '0002_auto_20210729_1814'),
    ]

    operations = [
        migrations.CreateModel(
            name='Klasa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=128)),
                ('klasa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dziennik.klasa')),
            ],
        ),
        migrations.CreateModel(
            name='Nauczyciel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('klasa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dziennik.klasa')),
                ('przedmiot', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dziennik.przedmiot')),
            ],
        ),
        migrations.AddField(
            model_name='ocena',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dziennik.student'),
        ),
        migrations.AddField(
            model_name='przedmiot',
            name='klasa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dziennik.klasa'),
        ),
    ]
