# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    _name = 'open_academy.session'
    _description = 'Session'

    name = fields.Char(string='Session')
    date = fields.Date(date='Date', default=fields.Date.today)
    duration = fields.Float(float='Duration')
    seats = fields.Integer(int='Seats')
    instructor_id = fields.Many2one('res.partner', string="Instructor", domain=['|', ('instructor', '=', True),('category_id.name', 'ilike', "Teacher")])
    course_id = fields.Many2one('open_academy.course',ondelete='cascade', string="Course", required=True)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")
    amount_seats = fields.Float(string="Taken seats", compute='_amount_seats')
    active = fields.Boolean(string='Active', default=True)
    

    @api.depends('seats', 'attendee_ids')
    def _amount_seats(self):
        for record in self:
            if not record.seats:
                record.amount_seats = 0.0
            else:
                record.amount_seats = 100.0 * len(record.attendee_ids) / record.seats