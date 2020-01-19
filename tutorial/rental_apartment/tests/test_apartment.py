# coding: utf-8

from odoo.tests.common import TransactionCase


class TestApartment(TransactionCase):

    def setUp(self):
        super(TestApartment, self).setUp()
        self.obj_journal = self.env['account.journal'].search([], limit=1)
        self.model_apartment = self.env['home.apartment']
    
    def test_done_apartment(self):
        obj_apartment = self.model_apartment.create({
            'street': 'Av. Brasil',
            'journal_id': self.obj_journal.id,
            'type': 'rental'
        })
        obj_apartment.action_post()
        self.assertEqual(obj_apartment.state, 'posted')
        print('----------------TEST OK - DONE APARTMENT ------------------')