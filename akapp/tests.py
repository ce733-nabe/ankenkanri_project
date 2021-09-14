import datetime
from django.test import TestCase
from .models import Anken


class AnkenModelTests(TestCase):

    def test_anken_has_date(self):
        """
        作成した日記データに日付が付与されているか確認        
        """
        Anken.objects.create(pub_date='2021-09-14',
                ankenmei='A案件',
                iraibusho='A部署',
                iraisha='Aさん',
                nouki='2021-09-30',
                mitumorikousu='0',
                naiyou='AAA',
                genjouchi='0', 
                kitaikouka='0', 
                tantousha='W',  
                koumoku='案件', 
                joutai='対応中', 
                jissekikousu='0',)
        actual_anken = Anken.objects.get(pub_date='2021-09-14')
        print(actual_anken)
        self.assertIsInstance(actual_anken.pub_date, datetime.date)

    