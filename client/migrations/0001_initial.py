# Generated by Django 5.1.2 on 2024-10-24 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clients',
            fields=[
                ('client_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('date_of_birth', models.DateField()),
                ('country', models.CharField(max_length=150)),
                ('account_balance', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'clients',
                'constraints': [models.UniqueConstraint(fields=('email',), name='unique_email_constraint')],
            },
        ),
    ]
