# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Provinces(models.Model):
    _name = 'ad.provinces'
    _description = 'sri lanka provinces'

    name = fields.Char("Province")

