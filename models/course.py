# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    _name = 'open_academy.course'
    _description = 'Course'

    name = fields.Char(string='Course')
    title = fields.Char(string='Title')
    description = fields.Text(string='Description')
    responsible_id = fields.Many2one('res.users', ondelete='set null', string="Responsible", index=True)
    session_ids = fields.One2many('open_academy.session', 'course_id', string="Sessions")

    _sql_constraints = [
        ('name_description_check', 'CHECK(name != description)', "El nombre del curso debe ser diferente a su descripcion."),
        ('name_unique', 'UNIQUE(name)', "El nombre del curso debe ser unico dentro de la lista existente."),
    ]