from odoo import models, fields, api

class poliza(models.Model):
     _name = 'contabilidad.poliza'

     name = fields.Char(string="Nombre", required=True)

     duration = fields.Integer(string="Plazo", required=True)   
     cost = fields.Float(string="Prima")
     date_cotract = fields.Date("Fecha de Contrato")