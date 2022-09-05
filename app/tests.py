from django.test import TestCase
from .models import Journals, Profile
from django.contrib.auth.models import User



class JournalTest(TestCase):
    def setUp(self):
        self.new_user = User(username='Michelle')
        self.new_user.save()

        self.new_profile = Profile(owner=self.new_user)
        self.new_profile.save()

        self.new_journal = Journals(body='Test Journal', posted_by= self.new_profile)
        self.new_journal.save()


    def test_instance(self):
        self.assertTrue(isinstance(self.new_journal, Journals))

    def test_save_method(self):
        self.new_journal.save()
        journals = Journals.objects.all()
        self.assertTrue(len(journals) > 0 )
