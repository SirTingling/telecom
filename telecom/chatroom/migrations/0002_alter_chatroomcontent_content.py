

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatroom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroomcontent',
            name='content',
            field=models.CharField(max_length=10000, null=True),
        ),
    ]
