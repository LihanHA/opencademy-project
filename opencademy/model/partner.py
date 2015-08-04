# -*- coding: utf-8 -*-
from openerp import fields, models

class Partner(models.Model):
    _inherit = 'res.partner' #Para heradar del modelo 
    # Add a new column to the res.partner model, by default partners are not
    # instructors
    instructor = fields.Boolean(default=False)
    session_ids = fields.Many2many('openacademy.session',
                                   string="Session as attendee",
                                   readonly=True) #este campo solo es informativo y no puedo agregar mas registros

