# Generated by Django 5.1.2 on 2024-10-15 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "insta_id",
                    models.CharField(max_length=30, verbose_name="인스타 아이디"),
                ),
                (
                    "is_following",
                    models.BooleanField(default=False, verbose_name="팔로잉 여부"),
                ),
                (
                    "is_follower",
                    models.BooleanField(default=False, verbose_name="팔로워 여부"),
                ),
                (
                    "like_count",
                    models.IntegerField(default=0, verbose_name="좋아요 횟수"),
                ),
            ],
        ),
    ]