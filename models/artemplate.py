"""
    AnalysisRequests often use the same configurations.
    ARTemplate includes all AR fields, including preset AnalysisProfile
"""
# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# from dependencies.dependency import ClassSecurityInfo
# from dependencies.dependency import *
# from dependencies.dependency import HoldingReference
# from dependencies.dependency import RecordsField
# from lims.interfaces import IARTemplate
# from lims.browser.widgets import RecordsWidget as BikaRecordsWidget
# from lims.browser.widgets import ARTemplatePartitionsWidget
# from lims.browser.widgets import ARTemplateAnalysesWidget
# from lims.browser.widgets import RecordsWidget
# from lims.browser.widgets import ReferenceWidget
# from lims.config import PROJECTNAME
# from lims.content.bikaschema import BikaSchema
# from dependencies.dependency import Interface, implements
from dependencies.dependency import getToolByName
from lims import bikaMessageFactory as _
import sys
from openerp import fields, models
from base_olims_model import BaseOLiMSModel
from fields.widget.widget import BooleanWidget, TextAreaWidget
from fields.boolean_field import BooleanField
from fields.string_field import StringField
from fields.text_field import TextField

# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# schema = BikaSchema.copy() + Schema(
schema = (StringField('name',
              required=1,        
    ),
    TextField('Description',
        widget=TextAreaWidget(
            description = _('Used in item listings and search results.'),
                            )
    ),
    ## SamplePoint and SampleType references are managed with
    ## accessors and mutators below to get/set a string value
    ## (the Title of the object), but still store a normal Reference.
    ## Form autocomplete widgets can then work with the Titles.

    fields.Many2one(string='Sample Point',
                    comodel_name='olims.sample_point',
                    help="Location where sample was taken",
                    required=False,
            #        vocabulary_display_path_bound = sys.maxint,
#         allowed_types = ('SamplePoint',),
#         relationship = 'ARTemplateSamplePoint',
#         referenceClass = HoldingReference,
#         accessor = 'getSamplePoint',
#         edit_accessor = 'getSamplePoint',
#         mutator = 'setSamplePoint',
#         widget=ReferenceWidget(
#             label = _("Sample Point"),
#             description = _("Location where sample was taken"),
#             visible={'edit': 'visible', 'view': 'visible', 'add': 'visible',
#                      'secondary': 'invisible'},
#             catalog_name='bika_setup_catalog',
#             base_query={'inactive_state': 'active'},
#             showOn=True,
#         ),
                    ),

# ~~~~~~~ To be implemented ~~~~~~~
#     ComputedField(
#         "SamplePointUID",
#         expression="context.Schema()['SamplePoint'].get(context) and context.Schema()['SamplePoint'].get(context).UID() or ''",
#         widget=ComputedWidget(
#             visible=False,
#         ),
#     ),

    fields.Many2one(string='SampleType',
                    comodel_name='olims.sample_type',
                    help="Create a new sample of this type",
                    required=False,
#      #         vocabulary_display_path_bound = sys.maxint,
#         allowed_types = ('SampleType',),
#         relationship = 'ARTemplateSampleType',
#         referenceClass = HoldingReference,
#         accessor = 'getSampleType',
#         edit_accessor = 'getSampleType',
#         mutator = 'setSampleType',
#         widget=ReferenceWidget(
#             label = _("Sample Type"),
#             description = _("Create a new sample of this type"),
#             visible={'edit': 'visible', 'view': 'visible', 'add': 'visible',
#                      'secondary': 'invisible'},
#             catalog_name='bika_setup_catalog',
#             base_query={'inactive_state': 'active'},
#             showOn=True,
#         ),
    ),

# ~~~~~~~ To be implemented ~~~~~~~
#     ComputedField(
#         "SampleTypeUID",
#         expression="context.Schema()['SampleType'].get(context) and context.Schema()['SampleType'].get(context).UID() or ''",
#         widget=ComputedWidget(
#             visible=False,
#         ),
#     ),
    BooleanField('ReportDryMatter',
        default = False,
        widget = BooleanWidget(
            label = _("Report as Dry Matter"),
            description = _("These results can be reported as dry matter"),
        ),
    ),
    TextField('Remarks',
        searchable = True,
        default_content_type = 'text/plain',
        allowed_content_types= ('text/plain', ),
        default_output_type="text/plain",
        widget = TextAreaWidget(
            macro = "bika_widgets/remarks",
            label = _("Remarks"),
            append_only = True,
        ),
    ),
          
        fields.Many2many(string='Partitions',
                       comodel_name='olims.partition_ar_template',

#         schemata = 'Sample Partitions',
#         required = 0,
#         type = 'artemplate_parts',
#         subfields = ('part_id',
#                      'Container',
#                      'Preservation',
#                      'container_uid',
#                      'preservation_uid'),
#         subfield_labels = {'part_id': _('Partition'),
#                            'Container': _('Container'),
#                            'Preservation': _('Preservation')},
#         subfield_sizes = {'part_id': 15,
#                            'Container': 35,
#                            'Preservation': 35},
#         subfield_hidden = {'preservation_uid': True,
#                            'container_uid': True},
#         default = [{'part_id':'part-1',
#                     'Container':'',
#                     'Preservation':'',
#                     'container_uid':'',
#                     'preservation_uid':''}],
#         widget=ARTemplatePartitionsWidget(
#             label = _("Sample Partitions"),
#             description = _("Configure the sample partitions and preservations " + \
#                             "for this template. Assign analyses to the different " + \
#                             "partitions on the template's Analyses tab"),
#             combogrid_options={
#                 'Container': {
#                     'colModel': [
#                         {'columnName':'container_uid', 'hidden':True},
#                         {'columnName':'Container', 'width':'30', 'label':_('Container')},
#                         {'columnName':'Description', 'width':'70', 'label':_('Description')}],
#                     'url': 'getcontainers',
#                     'showOn': True,
#                     'width': '550px'
#                 },
#                 'Preservation': {
#                     'colModel': [
#                         {'columnName':'preservation_uid', 'hidden':True},
#                         {'columnName':'Preservation', 'width':'30', 'label':_('Preservation')},
#                         {'columnName':'Description', 'width':'70', 'label':_('Description')}],
#                     'url': 'getpreservations',
#                     'showOn': True,
#                     'width': '550px'
#                 },
#             },
#          ),
        ),      

    fields.Many2one(string='AnalysisProfile',
                    comodel_name='olims.analysis_profile',
                    help="The Analysis Profile selection for this template",
                    required=False,
#         schemata = 'Analyses',
#         required = 0,
#         multiValued = 0,
#         allowed_types = ('AnalysisProfile',),
#         relationship = 'ARTemplateAnalysisProfile',
#         widget=ReferenceWidget(
#             label = _("Analysis Profile"),
#             description =_("The Analysis Profile selection for this template"),
#             visible={'edit': 'visible', 'view': 'visible', 'add': 'visible',
#                      'secondary': 'invisible'},
#             catalog_name='bika_setup_catalog',
#             base_query={'inactive_state': 'active'},
#             showOn=True,
#         ),
    ),

# ~~~~~~~ To be implemented ~~~~~~~
#     RecordsField('Analyses',
#         schemata = 'Analyses',
#         required = 0,
#         type = 'artemplate_analyses',
#         subfields = ('service_uid', 'partition'),
#         subfield_labels = {'service_uid': _('Title'),
#                            'partition': _('Partition')},
#         default = [],
#         widget = ARTemplateAnalysesWidget(
#             label = _("Analyses"),
#             description=_("Select analyses to include in this template"),
#         )
#     ),
#     # Custom settings for the assigned analysis services
#     # https://jira.bikalabs.com/browse/LIMS-1324
#     # Fields:
#     #   - uid: Analysis Service UID
#     #   - hidden: True/False. Hide/Display in results reports
# ~~~~~~~ To be implemented ~~~~~~~
#     RecordsField('AnalysisServicesSettings',
#          required=0,
#          subfields=('uid', 'hidden',),
#          widget=ComputedWidget(visible=False),
#     ),
    fields.Many2many(string='Analyses',
                       comodel_name='olims.records_field_artemplates',
    ),
)#,
#)

# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# schema['description'].widget.visible = True
# schema['title'].widget.visible = True
# schema['title'].validators = ('uniquefieldvalidator',)
# # Update the validation layer after change the validator in runtime
# schema['title']._validationLayer()

class ARTemplate(models.Model, BaseOLiMSModel):#(BaseContent):
    _name = 'olims.ar_template'
# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
#     security = ClassSecurityInfo()
#     schema = schema
#     displayContentsTab = False
#     implements(IARTemplate)

    _at_rename_after_creation = True
    def _renameAfterCreation(self, check_auto_id=False):
        from lims.idserver import renameAfterCreation
        renameAfterCreation(self)
# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
#     security.declarePublic('AnalysisProfiles')
# ~~~~~~~ To be implemented ~~~~~~~
#     def AnalysisProfiles(self, instance=None):
#         instance = instance or self
#         bsc = getToolByName(instance, 'bika_setup_catalog')
#         items = []
#         for p in bsc(portal_type='AnalysisProfile',
#                       inactive_state='active',
#                       sort_on = 'sortable_title'):
#             p = p.getObject()
#             title = p.Title()
#             items.append((p.UID(), title))
#         items = [['','']] + list(items)
#         return DisplayList(items)

    def getClientUID(self):
        return self.aq_parent.UID()

    def getAnalysisServiceSettings(self, uid):
        """ Returns a dictionary with the settings for the analysis
            service that match with the uid provided.
            If there are no settings for the analysis service and
            template, returns a dictionary with the key 'uid'
        """
        sets = [s for s in self.getAnalysisServicesSettings() \
                if s.get('uid','') == uid]
        return sets[0] if sets else {'uid': uid}

    def isAnalysisServiceHidden(self, uid):
        """ Checks if the analysis service that match with the uid
            provided must be hidden in results.
            If no hidden assignment has been set for the analysis in
            this template, returns the visibility set to the analysis
            itself.
            Raise a TypeError if the uid is empty or None
            Raise a ValueError if there is no hidden assignment in this
                template or no analysis service found for this uid.
        """
        if not uid:
            raise TypeError('None type or empty uid')
        sets = self.getAnalysisServiceSettings(uid)
        if 'hidden' not in sets:
            uc = getToolByName(self, 'uid_catalog')
            serv = uc(UID=uid)
            if serv and len(serv) == 1:
                return serv[0].getObject().getRawHidden()
            else:
                raise ValueError('%s is not valid' % uid)
        return sets.get('hidden', False)

ARTemplate.initialze(schema)    
# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# registerType(ARTemplate, PROJECTNAME)
