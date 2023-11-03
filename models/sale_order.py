# -*- coding: utf-8 -*-

from flectra import models, fields, api, _

class StatusPrepensa(models.Model):
    _inherit = 'sale.order'

    status_prepensa = fields.Selection([('pending','Sin procesar'),('process','En proceso'),('send','Enviado a producción')], default="pending", string="Estatus Prepensa")
    status_partner = fields.Selection([('undefined','Sin definir'),('trust','Cliente Confiable'),('deberon','Cliente moroso'),('ignore','No atender')], string="Estatus Cliente", related="partner_id.status_partner")

    status_pay = fields.Selection([('paid', 'Pagado'),('no_paid','No pagado'),('advance_payment', 'Anticipo'),('cancell','Cancelado')], default="no_paid", string="Estatus Pago")