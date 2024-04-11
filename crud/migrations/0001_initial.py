
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('dataNascimento', models.DateField()),
                ('email', models.CharField(max_length=50)),
                ('paisDestino', models.CharField(max_length=50)),
            ],
        ),
    ]
