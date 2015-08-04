from openerp import fields, models

'''
This module create model of Course
'''

class Course(models.Model):
    '''
    This class create model of Course
    '''
    _name = 'openacademy.course'

    name = fields.Char(string='Title', required=True)  #  field reserved to identified name rec 
    description = fields.Text(string='Description', required=False)
    responsible_id = fields.Many2one('res.users',
                                     ondelete='set null',
                                     string="Responsible", index=True)
    session_ids = fields.One2many('openacademy.session', 'course_id', string="Sessions")


