# Generated by Django 3.1.2 on 2020-11-19 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourproject', '0009_auto_20201113_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sell_product',
            name='branch',
            field=models.CharField(choices=[('Information Technology', 'Information Technology'), ('Mechanical Engineer', 'Mechanical Engineer'), ('Civil Engineer', 'Civil Engineer'), ('Computer Engineer', 'Computer Engineer')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='sell_product',
            name='year',
            field=models.CharField(choices=[('1', 'FE'), ('3', 'TE'), ('4', 'BE'), ('2', 'SE')], default='', max_length=50),
        ),
    ]