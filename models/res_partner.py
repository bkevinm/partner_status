# -*- coding: utf-8 -*-

from flectra import models, fields, api, _

class StatusPartners(models.Model):
    _inherit = 'res.partner'

    status_partner = fields.Selection([('undefined','Sin definir'),('trust','Cliente Confiable'),('deberon','Cliente moroso'),('ignore','No atender')], string="Estatus Cliente", default="undefined")