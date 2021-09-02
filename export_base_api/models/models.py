# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class export_base_api(models.Model):
#     _name = 'export_base_api.export_base_api'
#     _description = 'export_base_api.export_base_api'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
