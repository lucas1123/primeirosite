# Generated by Django 2.0.8 on 2018-09-21 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeMarca', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50)),
                ('chassi', models.DecimalField(decimal_places=2, max_digits=20)),
                ('cor', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('motor', models.CharField(max_length=50)),
                ('potência', models.CharField(max_length=50)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.Marca')),
            ],
        ),
    ]
