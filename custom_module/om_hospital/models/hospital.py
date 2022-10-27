# -*- coding: utf-8 -*-

from odoo import models, fields, api


class om_hospital(models.Model):
    _name = 'om.hospital'
    _description = 'hospital management tool'

    name = fields.Char(string='Name')
    Age = fields.Integer(string='Age')
    Gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', default='male', required=True)
    Medical_History = fields.Text(string='prev-records')
    bill_paid = fields.Boolean(string='payment_info', default=False)
    active = fields.Boolean(string='Active', default=True)
#     _name = 'om_hospital.om_hospital'
#     _description = 'om_hospital.om_hospital'
#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
