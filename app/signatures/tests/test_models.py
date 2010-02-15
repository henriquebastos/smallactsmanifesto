from datetime import datetime as dt
from django.test import TestCase
from django.db import IntegrityError
from signatures.models import Signatory


__all__ = ['TestModels']


def factory(**kwargs):
    param = dict(name="Henrique Bastos", 
                 email="henrique@bastos.net",
                 url="http://henriquebastos.net", 
                 location="Rio de Janeiro/Brazil",
                 confirmation_key="somecrazyhash")
    param.update(**kwargs)
    return Signatory(**param)


class TestModels(TestCase):
    def test_add_new_signatory(self):
        s = factory()
        s.save()
        self.assertEquals(s.id, 1L)
        self.assertTrue(isinstance(s.signed_at, dt))

    def test_raises_on_duplicated_email(self):
        s1 = factory()
        s2 = factory()

        s1.save()
        self.assertEquals(s1.id, 1L)
        self.assertRaises(IntegrityError, s2.save)

    def test_add_with_empty_url(self):
        s = factory(url="")
        s.save()
        self.assertEquals(s.id, 1L)

    def test_raises_on_blank_name(self):
        s = factory(name=None)
        self.assertRaises(IntegrityError, s.save)

    def test_raises_on_blank_email(self):
        s = factory(email=None)
        self.assertRaises(IntegrityError, s.save)

    def test_raises_on_blank_location(self):
        s = factory(location=None)
        self.assertRaises(IntegrityError, s.save)

    def test_ordered_asc(self):
        sb = factory(name="b", email="b@b.com")
        sb.save()
        sc = factory(name="c", email="c@b.com")
        sc.save()
        sa = factory(name="a", email="a@b.com")
        sa.save()

        ordered_list = list(Signatory.objects.all())
        self.assertEquals(ordered_list, [sa, sb, sc])


