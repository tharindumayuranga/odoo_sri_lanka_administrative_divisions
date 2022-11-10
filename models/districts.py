# -*- coding: utf-8 -*-

import json
from odoo import models, fields, api


class Districts(models.Model):
    _name = 'ad.districts'
    _description = 'sri lanka districts'

    name = fields.Char("District")
    province_id = fields.Many2one('ad.provinces', string='Province')
 