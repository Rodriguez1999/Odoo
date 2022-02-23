# -*- coding: utf-8 -*-
from odoo import fields, models
from . import partner


class Partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    instructor = fields.Boolean(string = "Instructor", default=False)
    session_ids = fields.Many2many('open_academy.session', string="Att-Sessi", readonly=True)