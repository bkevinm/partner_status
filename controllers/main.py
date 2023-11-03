# -*- coding: utf-8 -*-

from flectra.addons.website_self_cfdi_invoice.controllers.main import WebsiteSaleExtend

class WebsiteSalePartner(WebsiteSaleExtend):

    def values_postprocess(self, order, mode, values, errors, error_msg):
        res = super(WebsiteSaleExtend, self).values_postprocess(order, mode, values, errors, error_msg)
        if values.get('uso_cfdi'):
            order.write({'uso_cfdi':values.get('uso_cfdi')})
            res[0].update({'uso_cfdi':values.get('uso_cfdi')})
        if values.get('vat'):
            order.partner_id.write({'vat':values.get('vat')})
            res[0].update({'vat': values.get('vat')})
        if values.get('regimen_fiscal'):
            res[0].update({'regimen_fiscal':values.get('regimen_fiscal')})
        return res

