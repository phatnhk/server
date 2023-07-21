# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class Course(models.Model):
    _name = 'crm.course'

    name = fields.Char("Tên môn học")
    code = fields.Char("Mã môn học")
    cost = fields.Integer("Học phí")
    major_id = fields.Many2one('crm.major', string="Mã ngành", ondelete='set null')


