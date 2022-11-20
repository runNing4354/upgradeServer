# Generated by Django 4.1.3 on 2022-11-20 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listen', '0002_listencarefree_audio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('answer', models.IntegerField()),
                ('audio', models.FileField(null=True, upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='Sound',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('answer', models.IntegerField()),
                ('audio', models.FileField(null=True, upload_to='uploads/')),
            ],
        ),
        migrations.RenameModel(
            old_name='ListenCareFree',
            new_name='Emotion',
        ),
    ]