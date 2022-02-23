# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    _name = 'open_academy.session'
    _description = 'Session'

    name = fields.Char(string='Session')
    date = fields.Date(date='Date')
    duration = fields.Float(float='Duration')
    seats = fields.Integer(int='Seats')
    instructor_id = fields.Many2one('res.partner', string="Instructor")
    course_id = fields.Many2one('open_academy.course',ondelete='cascade', string="Course", required=True)