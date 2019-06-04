# Generated by Django 2.2 on 2019-06-04 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_chaininteraction'),
    ]

    operations = [
        migrations.CreateModel(
            name='Residue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('residue_number', models.IntegerField()),
                ('insertion_code', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('atomium_id', models.CharField(max_length=128)),
                ('chain_identifier', models.CharField(max_length=128)),
                ('chain_signature', models.CharField(blank=True, max_length=128)),
                ('chain', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Chain')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ZincSite')),
            ],
            options={
                'db_table': 'residues',
                'ordering': ['residue_number'],
            },
        ),
    ]
