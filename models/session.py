# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Session(models.Model):
    _name = 'open_academy.session'
    _description = 'Session'

    name = fields.Char(string='Session' )
    date = fields.Date(date='Date', default=fields.Date.today)
    duration = fields.Float(float='Duration')
    seats = fields.Integer(int='Seats')
    instructor_id = fields.Many2one('res.partner', string="Instructor", domain=['|', ('instructor', '=', True),('category_id.name', 'ilike', "Teacher")])
    course_id = fields.Many2one('open_academy.course',ondelete='cascade', string="Course", required=True)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")
    amount_seats = fields.Float(string="Taken seats", compute='_amount_seats')
    active = fields.Boolean(string='Active', default=True)
    
    # porsentaje de asientos ocupados
    @api.depends('seats', 'attendee_ids')
    def _amount_seats(self):
        for record in self:
            if not record.seats:
                record.amount_seats = 0.0
            else:
                record.amount_seats = 100.0 * len(record.attendee_ids) / record.seats

    # Advertencias de limite de asistentes y cantidad de asientos validos
    @api.onchange('seats', 'attendee_ids')
    def _onchange_seats(self):
        if self.seats < 0: 
            return {
                'warning': {
                    'title': "Alert warning",
                    'message': "Value invalid, number negative",
                }
            }
        if self.seats < len(self.attendee_ids): 
            return {
                'warning': {
                    'title': "Alert warning",
                    'message': "There cannot be more members than chairs",
                }
            }
    # Restriccion de instructor como integrante de una sesion  
    @api.constrains('attendee_ids')
    def _check_instructor(self):
        for record in self.attendee_ids:
            if record == self.instructor_id:
                raise ValidationError("The instructor not is a attendee")

