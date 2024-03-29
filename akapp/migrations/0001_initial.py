# Generated by Django 3.2.6 on 2021-09-10 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(verbose_name='日付')),
                ('ankenmei', models.CharField(max_length=200, verbose_name='案件名')),
                ('iraibusho', models.CharField(max_length=200, verbose_name='依頼部署')),
                ('iraisha', models.CharField(max_length=200, verbose_name='依頼者')),
                ('nouki', models.DateTimeField(verbose_name='納期')),
                ('mitumorikousu', models.IntegerField(default=0, verbose_name='見積工数(H)')),
                ('naiyou', models.TextField(max_length=1000, verbose_name='内容')),
                ('genjouchi', models.CharField(max_length=200, verbose_name='現状値')),
                ('kitaikouka', models.CharField(max_length=200, verbose_name='期待効果')),
                ('tantousha', models.CharField(choices=[('0', '藤井'), ('1', '亀井'), ('2', '渡邊'), ('3', '藤田'), ('4', '猿渡'), ('5', '馬見塚'), ('6', '星野')], max_length=200, verbose_name='担当者')),
                ('koumoku', models.CharField(choices=[('0', '案件'), ('1', '案件_別途報告'), ('2', '創意工夫展開'), ('3', '自己研鑽'), ('4', 'お知らせ'), ('5', 'その他')], max_length=200, verbose_name='項目')),
                ('joutai', models.CharField(choices=[('0', '対応中'), ('1', '完了'), ('2', '一時休止'), ('3', '未着手'), ('4', '指定しない')], max_length=200, verbose_name='状態')),
                ('jissekikousu', models.IntegerField(default=0, verbose_name='実績工数(H)')),
            ],
        ),
        migrations.CreateModel(
            name='Shuho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(verbose_name='日付')),
                ('naiyou', models.TextField(max_length=1000, verbose_name='内容')),
                ('categori', models.CharField(choices=[('0', '環境構築'), ('1', '前処理'), ('2', '分析手法'), ('3', 'エッジ・設備'), ('4', 'その他')], max_length=200, verbose_name='カテゴリ')),
                ('anken', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='akapp.anken')),
            ],
        ),
    ]
