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

    # Restricciones desde el sql de postgress
    _sql_constraints = [
        ('name_and_description_check', 'CHECK(name != description)', "El nombre del curso debe ser diferente a su descripcion."),
        ('name_unique', 'UNIQUE(name)', "El nombre del curso debe ser unico dentro de la lista existente."),
    ]

    # duplicar curso
    def copy(self, default=None):
        if default is None:
            default={}
        if not default.get('name'):
            default['name'] = "Copy of ["+self.name+"]"
        return super(Course, self).copy(default)