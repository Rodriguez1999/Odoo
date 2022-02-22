# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    _name = 'open_academy.session'
    _description = 'Session'

    name = fields.Char(string='Session')
    date = fields.Date(date='Date')
    duration = fields.Float(float='Duration')
    seats = fields.Integer(int='Seats')