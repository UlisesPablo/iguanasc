

from odoo import models, fields, api

class Poliza(models.Model):
     _name = 'libros.poliza'

     name = fields.Char(string="Nombre",required=True)

     cost = fields.Float(string="Prima")
     date_contract = fields.Date("fecha de contrato")