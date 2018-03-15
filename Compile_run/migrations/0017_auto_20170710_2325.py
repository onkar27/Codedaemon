# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-10 17:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Compile_run', '0016_remove_problem_session_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='Problem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Problem'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.User'),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='Problem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Problem'),
        ),
        migrations.AlterField(
            model_name='user_problem',
            name='Problem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Problem'),
        ),
        migrations.AlterField(
            model_name='user_problem',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.User'),
        ),
        migrations.DeleteModel(
            name='Problem',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]