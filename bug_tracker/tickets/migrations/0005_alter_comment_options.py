# Generated by Django 4.2.1 on 2023-06-06 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0004_comment_ticket_alter_comment_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_at']},
        ),
    ]
