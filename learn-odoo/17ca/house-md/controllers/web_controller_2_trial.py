from odoo import http
from odoo.http import request

# This was Trial 2 for topics 'Rendering Templates'
class WebController(http.Controller):
    @http.route('/trial/product/catalog',auth='public',type='http',website=True)
    def product_catalog(self,search=None,category_id=None, sort_by='name'):

        domain=[]

        if search:
            domain+=[('name','ilike',search)]

        if category_id:
            domain+=[('categ_id','=',int(category_id))]

        # this will show patient based on search - static
        products=request.env['product.template'].search(domain,order=f'{sort_by} asc')

        # this is category_id filter in patients
        categories=request.env['product.category'].search([])

        return request.render('house-md.rendering_template_for_products_sales',{
            'products':products,
            'categories':categories,
            'search':search,
            'select_category_id':int(category_id) if category_id else None,
            'sort_by':sort_by,
        })