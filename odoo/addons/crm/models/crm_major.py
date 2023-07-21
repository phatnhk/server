# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class Major(models.Model):
    _name = 'crm.major'

    name = fields.Char("Tên ngành học")
    code = fields.Char("Code ngành học")
    code_major = fields.Char("Mã ngành học")
    course_ids = fields.One2many('crm.course', 'major_id', string="Mã môn học")

