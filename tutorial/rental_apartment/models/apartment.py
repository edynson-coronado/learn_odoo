# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class HomeApartment(models.Model):
    _name = 'home.apartment'

    name = fields.Char(
        string='Number',
        default='/',
        readonly=True,
        required=True
    )
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('posted', 'Publicado'),
        ('done', 'Contratado'),
    ], string='Estado',
        required=True,
        default='draft'
    )
    type = fields.Selection([
        ('sale', 'Sale'),
        ('rental', 'Renta')
    ], string='Tipo', required=True)
    date = fields.Date(
        string='Date',
        required=True,
        default=fields.Date.context_today
    )
    journal_id = fields.Many2one(
        comodel_name='account.journal',
        domain=[('bool_rental', '=', True)],
        required=True
    )
    service_ids = fields.Many2many(
        comodel_name='service.apartment',
        relation='service_apartment_rel',
        string='Servicios'
    )
    count_service = fields.Integer(
        string='Servicios',
        compute='_compute_service',
        store=True
    )
    street = fields.Char(
        string='Street',
        required=True
    )
    l10n_pe_district = fields.Many2one(
        string='District',
        comodel_name='l10n_pe.res.city.district'
    )
    city_id = fields.Many2one(
        string='Province',
        comodel_name='res.city'
    )
    country_id = fields.Many2one(
        string='Country',
        comodel_name='res.country'
    )
    reference = fields.Char(
        string='Dirección'
    )

    def action_post(self):
        for obj in self:
            to_write = {
                'state': 'posted'
            }
            if obj.name == '/':
                sequence = obj._get_sequence()
                if not sequence:
                    raise ValidationError('Please define a sequence on your journal.')
                to_write['name'] = sequence.next_by_id(sequence_date=obj.date)
            obj.write(to_write)

    def action_done(self):
        self.write({
            'state': 'done'
        })

    def _get_sequence(self):
        self.ensure_one()
        obj_journal = self.journal_id
        return obj_journal.sequence_id

    @api.constrains('name', 'type')
    def _check_name_type(self):
        for obj in self:
            rec = self.search([
                ('name', '=', obj.name),
                ('type', '=', obj.type)
            ])
            if len(rec) > 1:
                raise ValidationError('Tag name and type already exists!')

    @api.depends('service_ids')
    def _compute_service(self):
        for obj in self:
            list_obj_service = obj.service_ids
            obj.count_service = len(list_obj_service)

    @api.onchange('street', 'l10n_pe_district', 'city_id', 'country_id')
    def _onchange_reference(self):
        for obj in self:
            reference = '{}{}{}{}'.format(
                obj.street and ':' + obj.street or '',
                obj.l10n_pe_district and '-' + obj.l10n_pe_district.name or '',
                obj.city_id and '-' + obj.city_id.name or '',
                obj.country_id and '-' + obj.country_id.name or ''
            )
            obj.reference = reference


class ServiceApartment(models.Model):
    _name = 'service.apartment'

    name = fields.Char(
        string='Servicio',
        required=True
    )
    sequence = fields.Integer(default=10)
    apartment_ids = fields.Many2many(
        comodel_name='home.apartment',
        relation='service_apartment_rel',
        string='Apartments'
    )

    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'Tag name already exists!'),
    ]
