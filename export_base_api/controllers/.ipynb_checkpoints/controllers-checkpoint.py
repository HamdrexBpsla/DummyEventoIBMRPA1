# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import Response
import json

class ExportBaseController(http.Controller):
    
    
    @http.route('/api/bases', auth='public', method=['GET'], csrf=False)
    def get_bases(self, **kw):
        try:
            bases = http.request.env['helpdesk.ticket'].sudo().search_read([('x_studio_fecha_del_caso',"=",'2021-08-31')],['user_id','partner_id','x_studio_fecha_del_caso','x_studio_it_atix','x_studio_numero_ticket_proveedor_masivo','x_studio_nivel_1','x_studio_nivel_2','x_studio_nivel_3','x_studio_nivel_1_p','x_studio_nivel_2_p','x_studio_nivel_3_p','x_studio_notas','x_studio_detalles_de_trabajo'])
            
            res = json.dumps(bases, ensure_ascii=False).encode('utf-8')
            return Response(res, content_type='application/json;charset=utf-8', status=200)
        except Exception as e:
            return Response(json.dumps({'error':str(e)}), content_type='application/json;charset=utf-8', status=505)
        