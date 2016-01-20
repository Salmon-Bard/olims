# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# from dependencies.dependency import ClassSecurityInfo
# from lims.utils import t
# from lims.config import PROJECTNAME
# from lims.content.bikaschema import BikaSchema
# from lims.vocabularies import CatalogVocabulary
# from magnitude import mg, MagnitudeError
# from dependencies.dependency import mg
# from dependencies.dependency import *
# from dependencies.dependency import HoldingReference
# from OLiMS.dependencies.dependency import itemgetter
# from dependencies.dependency import check as CheckAuthenticator

from dependencies.dependency import DisplayList
import sys
from lims import bikaMessageFactory as _
from dependencies.dependency import getToolByName
from operator import itemgetter
import json
from openerp import fields, models
from base_olims_model import BaseOLiMSModel
from fields.string_field import StringField
from fields.text_field import TextField
from fields.boolean_field import BooleanField
from fields.widget.widget import StringWidget, TextAreaWidget, \
                                BooleanWidget
# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# schema = BikaSchema.copy() + Schema((
schema = (StringField('Container',
        required=1,
        widget=StringWidget(
            label=_('Title'),
            description=_('Title is required.'),
        ),
    ),
    TextField('Description',
        widget=TextAreaWidget(
            label=_('Description'),
            description=_('Used in item listings and search results.'),
        ),
    ),
    fields.Many2one(string='Container Type',
        required = False,
        comodel_name='olims.container_type',
#         vocabulary_display_path_bound = sys.maxint,
#         allowed_types = ('ContainerType',),
#         vocabulary = 'getContainerTypes',
#         relationship = 'ContainerContainerType',
#         referenceClass = HoldingReference,
#         widget = ReferenceWidget(
#             checkbox_bound = 0,
#             label=_("Container Type"),
#         ),
    ),
    StringField('Capacity',
        required = 1,
        default = "0 ml",
        widget = StringWidget(
            label=_("Capacity"),
            description=_("Maximum possible size or volume of samples."),
        ),
    ),
    BooleanField('PrePreserved',
        validators = ('container_prepreservation_validator'),
        default = False,
        widget = BooleanWidget(
            label=_("Pre-preserved"),
            description = _(
                "Check this box if this container is already preserved." + \
                "Setting this will short-circuit the preservation workflow " + \
                "for sample partitions stored in this container."),
        ),
    ),
    fields.Many2one(string='Pre-preserved',
        required = False,
        comodel_name='olims.preservation',
        help="If this container is pre-preserved, then the preservation " +\
                "method could be selected here."
#         vocabulary_display_path_bound = sys.maxint,
#         allowed_types = ('Preservation',),
#         vocabulary = 'getPreservations',
#         relationship = 'ContainerPreservation',
#         referenceClass = HoldingReference,
#         widget = ReferenceWidget(
#             checkbox_bound = 0,
#             label=_("Preservation"),
#             description = _(
#                 "If this container is pre-preserved, then the preservation "
#                 "method could be selected here."),
#         ),
    ),
)#)
# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# schema['description'].widget.visible = True
# schema['description'].schemata = 'default'

class Container(models.Model, BaseOLiMSModel):#(BaseContent):
    _name = 'olims.container'
    _rec_name = 'Container'
# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
#     security = ClassSecurityInfo()
#     displayContentsTab = False
#     schema = schema

    _at_rename_after_creation = True
    def _renameAfterCreation(self, check_auto_id=False):
        from lims.idserver import renameAfterCreation
        renameAfterCreation(self)
        
# ~~~~~~~ To be implemented ~~~~~~~
#     def getJSCapacity(self, **kw):
#         """Try convert the Capacity to 'ml' or 'g' so that JS has an
#         easier time working with it.  If conversion fails, return raw value.
#         """
#         default = self.Schema()['Capacity'].get(self)
#         try:
#             mgdefault = default.split(' ', 1)
#             mgdefault = mg(float(mgdefault[0]), mgdefault[1])
#         except:
#             mgdefault = mg(0, 'ml')
#         try:
#             return str(mgdefault.ounit('ml'))
#         except:
#             pass
#         try:
#             return str(mgdefault.ounit('g'))
#         except:
#             pass
#         return str(default)

    def getContainerTypes(self):
        bsc = getToolByName(self, 'bika_setup_catalog')
        items = [('','')] + [(o.UID, o.Title) for o in
                               bsc(portal_type='ContainerType')]
        o = self.getContainerType()
        if o and o.UID() not in [i[0] for i in items]:
            items.append((o.UID(), o.Title()))
        items.sort(lambda x,y: cmp(x[1], y[1]))
        return DisplayList(list(items))

    def getPreservations(self):
        bsc = getToolByName(self, 'bika_setup_catalog')
        items = [('','')] + [(o.UID, o.Title) for o in
                               bsc(portal_type='Preservation',
                                   inactive_state = 'active')]
        o = self.getPreservation()
        if o and o.UID() not in [i[0] for i in items]:
            items.append((o.UID(), o.Title()))
        items.sort(lambda x,y: cmp(x[1], y[1]))
        return DisplayList(list(items))

Container.initialze(schema)
# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# registerType(Container, PROJECTNAME)

# ~~~~~~~ To be implemented ~~~~~~~
# class ajaxGetContainers:
# 
#     catalog_name='bika_setup_catalog'
#     contentFilter = {'portal_type': 'Container',
#                      'inactive_state': 'active'}
# 
#     def __init__(self, context, request):
#         self.context = context
#         self.request = request
# 
#     def __call__(self):
# 
#         CheckAuthenticator(self.request)
#         searchTerm = 'searchTerm' in self.request and self.request[
#             'searchTerm'].lower() or ''
#         page = self.request['page']
#         nr_rows = self.request['rows']
#         sord = self.request['sord']
#         sidx = self.request['sidx']
#         rows = []
# 
#         # lookup objects from ZODB
#         catalog = getToolByName(self.context, self.catalog_name)
#         brains = catalog(self.contentFilter)
#         brains = searchTerm and \
#             [p for p in brains if p.Title.lower().find(searchTerm) > -1] \
#             or brains
# 
#         rows = [{'UID': p.UID,
#                  'container_uid': p.UID,
#                  'Container': p.Title,
#                  'Description': p.Description}
#                 for p in brains]
# 
#         rows = sorted(rows, cmp=lambda x, y: cmp(x.lower(
#         ), y.lower()), key=itemgetter(sidx and sidx or 'Container'))
#         if sord == 'desc':
#             rows.reverse()
#         pages = len(rows) / int(nr_rows)
#         pages += divmod(len(rows), int(nr_rows))[1] and 1 or 0
#         ret = {'page': page,
#                'total': pages,
#                'records': len(rows),
#                'rows': rows[(int(page) - 1) * int(nr_rows): int(page) * int(nr_rows)]}
#         return json.dumps(ret)
