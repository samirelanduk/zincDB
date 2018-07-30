# Generated by Django 2.0.2 on 2018-07-28 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atom_pdb_identifier', models.IntegerField()),
                ('name', models.CharField(max_length=32)),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('z', models.FloatField()),
                ('element', models.CharField(max_length=8)),
                ('liganding', models.BooleanField()),
            ],
            options={
                'db_table': 'atoms',
            },
        ),
        migrations.CreateModel(
            name='Chain',
            fields=[
                ('id', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('chain_pdb_identifier', models.CharField(max_length=128)),
                ('sequence', models.TextField()),
            ],
            options={
                'db_table': 'chains',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ChainCluster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'chain_clusters',
            },
        ),
        migrations.CreateModel(
            name='Metal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atom_pdb_identifier', models.IntegerField()),
                ('name', models.CharField(max_length=32)),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('z', models.FloatField()),
                ('element', models.CharField(max_length=8)),
                ('residue_name', models.CharField(max_length=32)),
                ('residue_pdb_identifier', models.IntegerField()),
                ('insertion_pdb_identifier', models.CharField(max_length=128)),
                ('chain_pdb_identifier', models.CharField(max_length=128)),
                ('omission', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'metals',
            },
        ),
        migrations.CreateModel(
            name='Pdb',
            fields=[
                ('id', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=1024)),
                ('classification', models.CharField(blank=True, max_length=1024, null=True)),
                ('keywords', models.CharField(blank=True, max_length=2048, null=True)),
                ('deposited', models.DateField(blank=True, null=True)),
                ('resolution', models.FloatField(blank=True, null=True)),
                ('organism', models.CharField(blank=True, max_length=1024, null=True)),
                ('expression', models.CharField(blank=True, max_length=1024, null=True)),
                ('technique', models.CharField(blank=True, max_length=1024, null=True)),
                ('rfactor', models.FloatField(blank=True, null=True)),
                ('assembly', models.IntegerField(blank=True, null=True)),
                ('skeleton', models.BooleanField()),
            ],
            options={
                'db_table': 'PDBs',
            },
        ),
        migrations.CreateModel(
            name='Residue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('residue_pdb_identifier', models.IntegerField()),
                ('insertion_pdb_identifier', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('chain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zinc.Chain')),
            ],
            options={
                'db_table': 'residues',
                'ordering': ['residue_pdb_identifier'],
            },
        ),
        migrations.CreateModel(
            name='ZincSite',
            fields=[
                ('id', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('copies', models.IntegerField()),
            ],
            options={
                'db_table': 'zinc_sites',
            },
        ),
        migrations.CreateModel(
            name='ZincSiteCluster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'zincsite_clusters',
            },
        ),
        migrations.AddField(
            model_name='zincsite',
            name='cluster',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='zinc.ZincSiteCluster'),
        ),
        migrations.AddField(
            model_name='zincsite',
            name='pdb',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zinc.Pdb'),
        ),
        migrations.AddField(
            model_name='residue',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zinc.ZincSite'),
        ),
        migrations.AddField(
            model_name='metal',
            name='pdb',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zinc.Pdb'),
        ),
        migrations.AddField(
            model_name='metal',
            name='site',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zinc.ZincSite'),
        ),
        migrations.AddField(
            model_name='chain',
            name='cluster',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='zinc.ChainCluster'),
        ),
        migrations.AddField(
            model_name='chain',
            name='pdb',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zinc.Pdb'),
        ),
        migrations.AddField(
            model_name='atom',
            name='residue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zinc.Residue'),
        ),
    ]
