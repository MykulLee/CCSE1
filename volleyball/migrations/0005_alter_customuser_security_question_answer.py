# Generated by Django 5.1.4 on 2025-02-04 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volleyball', '0004_rename_security_answer_customuser_security_question_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='security_question_answer',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
