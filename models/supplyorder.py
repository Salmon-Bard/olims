# # ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~

# from dependencies.dependency import *
# from dependencies.dependency import ClassSecurityInfo
# from lims import bikaMessageFactory as _
# from lims.browser.widgets import DateTimeWidget
# from lims.browser.widgets import ReferenceWidget as BikaReferenceWidget
# from lims.config import PROJECTNAME
# from lims.content.bikaschema import BikaSchema
# from lims.interfaces import ISupplyOrder
# from lims.utils import t
# from dependencies.dependency import DateTime
# from dependencies.dependency import PersistentMapping
# from dependencies.dependency import Decimal
# from dependencies import atapi
# from dependencies.dependency import View
# from dependencies.dependency import IConstrainTypes
# from dependencies.dependency import implements



from lims import bikaMessageFactory as _
from openerp import fields, models
from fields.string_field import StringField
from fields.text_field import TextField
from fields.date_time_field import DateTimeField

from fields.widget.widget import TextAreaWidget, StringWidget, DateTimeWidget
from models.base_olims_model import BaseOLiMSModel


#schema = BikaSchema.copy() + Schema((
schema = (

  fields.Many2one(string='Contact',
        comodel_name='olims.contact',
        requried =True,
#         vocabulary_display_path_bound=sys.maxsize,
    #   allowed_types=('Contact',),
    #   referenceClass=HoldingReference,
    #   relationship='SupplyOrderContact',
    #   widget=BikaReferenceWidget(
    #     render_own_label=True,
    #     showOn=True,
    #     colModel=[
    #       {'columnName': 'UID', 'hidden': True},
    #       {'columnName': 'Fullname', 'width': '50', 'label': _('Name')},
    #       {'columnName': 'EmailAddress', 'width': '50', 'label': _('Email Address')},
    #     ],
    ),

    fields.Char(string='OrderNumber',
                compute='compute_order_id',
    ),

    fields.Many2one(string='Invoice',
        comodel_name='olims.invoice',
        requried =False,
         help =    'contact',
    # vocabulary_display_path_bound=sys.maxsize,
    #                allowed_types=('Invoice',),
    #                referenceClass=HoldingReference,
    #                relationship='OrderInvoice',
    ),

    DateTimeField(
      'OrderDate',
      required=1,
      default_method='current_date',
      widget=DateTimeWidget(
        label=_("Order Date"),
        size=12,
        render_own_label=True,
        visible={
          'edit': 'visible',
          'view': 'visible',
          'add': 'visible',
          'secondary': 'invisible'
        },
      ),
    ),
    DateTimeField('DateDispatched',
                  widget=DateTimeWidget(
                      label=_("Date Dispatched"),
                      ),
                  ),
    TextField('Remarks',
        searchable=True,
        default_content_type='text/plain',
        allowed_content_types=('text/plain', ),
        default_output_type="text/plain",
        widget = TextAreaWidget(
            macro="bika_widgets/remarks",
            label=_("Remarks"),
            append_only=True,
        ),
    ),
    fields.Many2many(string='Products',
        comodel_name='olims.lab_product',
        requried =False,
    ),
    fields.Float(string='SubTotal',
                compute='compute_subtotal'
    ),
    fields.Float(string='VAT',
                compute='compute_VATAmount'
    ),
    fields.Float(string='Total',
                compute='compute_Total'
    ),
# ~~~~~~~ To be implemented ~~~~~~~
    # ComputedField('ClientUID',
    #               expression = 'here.aq_parent.UID()',
    #               widget = ComputedWidget(
    #                   visible=False,
    #                   ),
    #               ),
    # ComputedField('ProductUID',
    #               expression = 'context.getProductUIDs()',
    #               widget = ComputedWidget(
    #                   visible=False,
    #                   ),
    #               ),
)


#schema['title'].required = False

# class SupplyOrderLineItem(PersistentMapping):
#     pass

class SupplyOrder(models.Model, BaseOLiMSModel): #BaseFolder
    _name='olims.supply_order'
    def compute_subtotal(self):
        if self.Products:
            for records in self.Products:
                if records.Quantity and records.Price:
                    quantity = records.Quantity
                    product_price_excluding_VAT = records.Price
                    self.SubTotal +=  int(quantity) * product_price_excluding_VAT
    def compute_order_id(self):
        order_string = 'O-'
        for record in self:
            record.OrderNumber = order_string + str(record.id)
    def compute_VATAmount(self):
        if self.Products:
            for records in self.Products:
                if records.Quantity and records.Price:
                    vat_amount = records.VAT
                    self.VAT +=  (vat_amount * records.TotalPrice)/100
    def compute_Total(self):
        for recod in self:
            recod.Total = self.SubTotal + self.VAT
    # implements(ISupplyOrder, IConstrainTypes)
    #
    # security = ClassSecurityInfo()
    # displayContentsTab = False
    # schema = schema

    # _at_rename_after_creation = True
    # supplyorder_lineitems = []
    #
    # def _renameAfterCreation(self, check_auto_id=False):
    #     from lims.idserver import renameAfterCreation
    #     renameAfterCreation(self)
    #
    # def getInvoiced(self):
    #     if self.getInvoice():
    #         return True
    #     else:
    #         return False
    #
    # def Title(self):
    #     """ Return the OrderNumber as title """
    #     return safe_unicode(self.getOrderNumber()).encode('utf-8')
    #
    # def getOrderNumber(self):
    #     return safe_unicode(self.getId()).encode('utf-8')
    #
    # def getContacts(self):
    #     adapter = getAdapter(self.aq_parent, name='getContacts')
    #     return adapter()
    #
    # #security.declarePublic('getContactUIDForUser')
    #
    # def getContactUIDForUser(self):
    #     """ get the UID of the contact associated with the authenticated
    #         user
    #     """
    #     user = self.REQUEST.AUTHENTICATED_USER
    #     user_id = user.getUserName()
    #     r = self.portal_catalog(
    #         portal_type='Contact',
    #         getUsername=user_id
    #     )
    #     if len(r) == 1:
    #         return r[0].UID
    #
    # #security.declareProtected(View, 'getTotalQty')
    #
    # def getTotalQty(self):
    #     """ Compute total qty """
    #     if self.supplyorder_lineitems:
    #         return sum(
    #             [obj['Quantity'] for obj in self.supplyorder_lineitems])
    #     return 0
    #
    # #security.declareProtected(View, 'getSubtotal')
    #
    # def getSubtotal(self):
    #     """ Compute Subtotal """
    #     if self.supplyorder_lineitems:
    #         return sum(
    #             [(Decimal(obj['Quantity']) * Decimal(obj['Price'])) for obj in self.supplyorder_lineitems])
    #     return 0
    #
    # #security.declareProtected(View, 'getVATAmount')
    #
    # def getVATAmount(self):
    #     """ Compute VAT """
    #     return Decimal(self.getTotal()) - Decimal(self.getSubtotal())
    #
    # #security.declareProtected(View, 'getTotal')
    #
    # def getTotal(self):
    #     """ Compute TotalPrice """
    #     total = 0
    #     for lineitem in self.supplyorder_lineitems:
    #         total += Decimal(lineitem['Quantity']) * \
    #                  Decimal(lineitem['Price']) *  \
    #                  ((Decimal(lineitem['VAT']) /100) + 1)
    #     return total
    #
    # def workflow_script_dispatch(self):
    #     """ dispatch order """
    #     self.setDateDispatched(DateTime())
    #     self.reindexObject()
    #
    # #security.declareProtected(View, 'getProductUIDs')
    #
    # def getProductUIDs(self):
    #     """ return the uids of the products referenced by order items
    #     """
    #     uids = []
    #     for orderitem in self.objectValues('XupplyOrderItem'):
    #         product = orderitem.getProduct()
    #         if product is not None:
    #             uids.append(orderitem.getProduct().UID())
    #     return uids
    #
    # #security.declarePublic('current_date')
    #
    # def current_date(self):
    #     """ return current date """
    #     return DateTime()


#atapi.registerType(SupplyOrder, PROJECTNAME)
SupplyOrder.initialze(schema)