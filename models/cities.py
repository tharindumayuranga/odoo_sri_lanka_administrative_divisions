# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Cities(models.Model):
    _name = 'ad.cities'
    _description = 'sri lanka cities'

    name = fields.Char("City")
    districts_id = fields.Many2one('ad.districts', string='Districts')
    