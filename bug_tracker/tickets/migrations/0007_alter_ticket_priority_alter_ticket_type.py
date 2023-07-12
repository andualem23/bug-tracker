# Generated by Django 4.2.3 on 2023-07-05 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0006_alter_ticket_priority_alter_ticket_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='priority',
            field=models.CharField(choices=[('High', 'High'), ('None', 'None'), ('Low', 'Low'), ('Medium', 'Medium')], max_length=40),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='type',
            field=models.CharField(choices=[('Feature request', 'Feature Request'), ('Traning/documents request', 'Traning/documents Request'), ('Other Comments', 'Other Comments'), ('Bugs/Errors', 'Bugs/Errors')], max_length=40),
        ),
    ]