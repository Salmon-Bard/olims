"""Sample represents a physical sample submitted for testing
"""
# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# from dependencies.dependency import ClassSecurityInfo
# from lims import bikaMessageFactory as _
# from lims.utils import t, getUsers
# from lims.browser.widgets.datetimewidget import DateTimeWidget
# from lims.config import PROJECTNAME
# from lims.content.bikaschema import BikaSchema
# from lims.interfaces import ISample
# from lims.permissions import SampleSample
# from lims.workflow import doActionFor, isBasicTransitionAllowed
# from lims.workflow import skip
# from dependencies.dependency import DateTime
# from dependencies import atapi
# from dependencies.dependency import REFERENCE_CATALOG
# from dependencies.dependency import *
# from dependencies.dependency import DisplayList
# from dependencies.dependency import HoldingReference
# from dependencies.dependency import HistoryAwareMixin

# from dependencies.dependency import permissions
# from dependencies.dependency import getToolByName
# from dependencies.dependency import safe_unicode
# from dependencies.dependency import implements
#
# from lims.browser.fields import DateTimeField
# from lims.browser.widgets import ReferenceWidget
# from lims.browser.widgets import SelectionWidget as BikaSelectionWidget
#
# import sys
from lims.utils import to_unicode
from dependencies.dependency import DT2dt, dt2DT
import sys
from dependencies.dependency import getToolByName
from dependencies.dependency import safe_unicode
from lims import bikaMessageFactory as _
from openerp import fields, models
from fields.string_field import StringField
from fields.text_field import TextField
from fields.boolean_field import BooleanField
from fields.date_time_field import DateTimeField
from base_olims_model import BaseOLiMSModel
import datetime
SAMPLE_STATES = (
                ('sample_registered', 'Registered'),
                ('to_be_sampled', 'To Be Sampled'),
                ('sampled', 'Sampled'),
                ('to_be_preserved', 'To Be Preserved'),
                ('sample_received', 'Sample Received'),
                ('sample_due', 'Sample Due'),
                ('expired', 'Expired'),
                ('disposed', 'Disposed'),
                )
#schema = BikaSchema.copy() + Schema((
schema = (StringField('name',
              compute='compute_smapleName',        
    ),
    fields.Char('SampleID',
        required=0,
        compute='compute_smapleId',
        help=_("The ID assigned to the client's sample by the lab"),
        # mode="rw",
        # read_permission=permissions.View,
        # write_permission=permissions.ModifyPortalContent,
        # widget=StringWidget(
        #     label=_("Sample ID"),
        #     description=_("The ID assigned to the client's sample by the lab"),
        #     visible={'edit': 'invisible',
        #              'view': 'invisible'},
        #     render_own_label=True,
        # ),
    ),
    StringField('ClientReference',
        searchable=True,
        # mode="rw",
        # read_permission=permissions.View,
        # write_permission=permissions.ModifyPortalContent,
        # widget=StringWidget(
        #     label=_("Client Reference"),
        #     visible={'edit': 'visible',
        #              'view': 'visible',
        #              'header_table': 'visible',
        #              'sample_registered': {'view': 'visible', 'edit': 'visible'},
        #              'to_be_sampled':     {'view': 'visible', 'edit': 'visible'},
        #              'sampled':           {'view': 'visible', 'edit': 'visible'},
        #              'to_be_preserved':   {'view': 'visible', 'edit': 'visible'},
        #              'sample_due':        {'view': 'visible', 'edit': 'visible'},
        #              'sample_received':   {'view': 'visible', 'edit': 'visible'},
        #              'expired':           {'view': 'visible', 'edit': 'invisible'},
        #              'disposed':          {'view': 'visible', 'edit': 'invisible'},
        #              },
        #     render_own_label=True,
        # ),
    ),
    StringField('ClientSampleID',
        searchable=True,
        # mode="rw",
        # read_permission=permissions.View,
        # write_permission=permissions.ModifyPortalContent,
        # widget=StringWidget(
        #     label=_("Client SID"),
        #     visible={'edit': 'visible',
        #              'view': 'visible',
        #              'header_table': 'visible',
        #              'sample_registered': {'view': 'visible', 'edit': 'visible'},
        #              'to_be_sampled':     {'view': 'visible', 'edit': 'visible'},
        #              'sampled':           {'view': 'visible', 'edit': 'visible'},
        #              'to_be_preserved':   {'view': 'visible', 'edit': 'visible'},
        #              'sample_due':        {'view': 'visible', 'edit': 'visible'},
        #              'sample_received':   {'view': 'visible', 'edit': 'visible'},
        #              'expired':           {'view': 'visible', 'edit': 'invisible'},
        #              'disposed':          {'view': 'visible', 'edit': 'invisible'},
        #              },
        #     render_own_label=True,
        # ),
    ),

    fields.Many2one(string='LinkedSample',
                   comodel_name='olims.sample',
        # vocabulary_display_path_bound=sys.maxsize,
        # multiValue=1,
        # allowed_types=('Sample',),
        # relationship='SampleSample',
        # referenceClass=HoldingReference,
        # mode="rw",
        # read_permission=permissions.View,
        # write_permission=permissions.ModifyPortalContent,
        # widget=ReferenceWidget(
        #     label=_("Linked Sample"),
        # ),,

    ),

    fields.Many2one(string='SampleType',
                   comodel_name='olims.sample_type',
                   readonly=True,
        # vocabulary_display_path_bound=sys.maxsize,
        # allowed_types=('SampleType',),
        # relationship='SampleSampleType',
        # referenceClass=HoldingReference,
        # mode="rw",
        # read_permission=permissions.View,
        # write_permission=permissions.ModifyPortalContent,
        # widget=ReferenceWidget(
        #     label=_("Sample Type"),
        #     render_own_label=True,
        #     visible={'edit': 'visible',
        #              'view': 'visible',
        #              'header_table': 'visible',
        #              'sample_registered': {'view': 'visible', 'edit': 'visible'},
        #              'to_be_sampled':     {'view': 'visible', 'edit': 'invisible'},
        #              'sampled':           {'view': 'visible', 'edit': 'invisible'},
        #              'to_be_preserved':   {'view': 'visible', 'edit': 'invisible'},
        #              'sample_due':        {'view': 'visible', 'edit': 'invisible'},
        #              'sample_received':   {'view': 'visible', 'edit': 'invisible'},
        #              'expired':           {'view': 'visible', 'edit': 'invisible'},
        #              'disposed':          {'view': 'visible', 'edit': 'invisible'},
        #              },
        #     catalog_name='bika_setup_catalog',
        #     base_query={'inactive_state': 'active'},
        #     showOn=True,
        # ),

    ),

    # ComputedField('SampleTypeTitle',
    #     searchable=True,
    #     expression="here.getSampleType() and here.getSampleType().Title() or ''",
    #     widget=ComputedWidget(
    #         visible=False,
    #     ),
    # ),
    fields.Many2one(string='SamplePoint',
                   comodel_name='olims.sample_point',
        # # vocabulary_display_path_bound=sys.maxsize,
        # allowed_types=('SamplePoint',),
        # relationship = 'SampleSamplePoint',
        # referenceClass = HoldingReference,
        # mode="rw",
        # read_permission=permissions.View,
        # write_permission=permissions.ModifyPortalContent,
        # widget=ReferenceWidget(
        #     label=_("Sample Point"),
        #     render_own_label=True,
        #     visible={'edit': 'visible',
        #              'view': 'visible',
        #              'header_table': 'visible',
        #              'sample_registered': {'view': 'visible', 'edit': 'visible'},
        #              'to_be_sampled':     {'view': 'visible', 'edit': 'invisible'},
        #              'sampled':           {'view': 'visible', 'edit': 'invisible'},
        #              'to_be_preserved':   {'view': 'visible', 'edit': 'invisible'},
        #              'sample_due':        {'view': 'visible', 'edit': 'invisible'},
        #              'sample_received':   {'view': 'visible', 'edit': 'invisible'},
        #              'expired':           {'view': 'visible', 'edit': 'invisible'},
        #              'disposed':          {'view': 'visible', 'edit': 'invisible'},
        #              },
        #     catalog_name='bika_setup_catalog',
        #     base_query={'inactive_state': 'active'},
        #     showOn=True,
        # ),

    ),
# ~~~~~~~ To be implemented ~~~~~~~
#     ComputedField('SamplePointTitle',
#         searchable = True,
#         expression = "here.getSamplePoint() and here.getSamplePoint().Title() or ''",
#         widget = ComputedWidget(
#             visible=False,
#         ),
#     ),


    fields.Many2one(string='StorageLocation',
                   comodel_name='olims.storage_location',
        # # vocabulary_display_path_bound=sys.maxsize,
        # allowed_types=('SamplePoint',),
        # relationship = 'SampleSamplePoint',
        # referenceClass = HoldingReference,
        # mode="rw",
        # read_permission=permissions.View,
        # write_permission=permissions.ModifyPortalContent,
        # widget=ReferenceWidget(
        #     label=_("Sample Point"),
        #     render_own_label=True,
        #     visible={'edit': 'visible',
        #              'view': 'visible',
        #              'header_table': 'visible',
        #              'sample_registered': {'view': 'visible', 'edit': 'visible'},
        #              'to_be_sampled':     {'view': 'visible', 'edit': 'invisible'},
        #              'sampled':           {'view': 'visible', 'edit': 'invisible'},
        #              'to_be_preserved':   {'view': 'visible', 'edit': 'invisible'},
        #              'sample_due':        {'view': 'visible', 'edit': 'invisible'},
        #              'sample_received':   {'view': 'visible', 'edit': 'invisible'},
        #              'expired':           {'view': 'visible', 'edit': 'invisible'},
        #              'disposed':          {'view': 'visible', 'edit': 'invisible'},
        #              },
        #     catalog_name='bika_setup_catalog',
        #     base_query={'inactive_state': 'active'},
        #     showOn=True,
        # ),

    ),

    # ~~~~~~~ To be implemented ~~~~~~~, when we have storage location
    # ReferenceField(
    #     'StorageLocation',
    #     allowed_types='StorageLocation',
    #     relationship='AnalysisRequestStorageLocation',
    #     mode="rw",
    #     read_permission=permissions.View,
    #     write_permission=permissions.ModifyPortalContent,
    #     widget=ReferenceWidget(
    #         label=_("Storage Location"),
    #         description=_("Location where sample is kept"),
    #         size=20,
    #         render_own_label=True,
    #         visible={'edit': 'visible',
    #                  'view': 'visible',
    #                  'header_table': 'visible',
    #                  'sample_registered': {'view': 'visible', 'edit': 'visible'},
    #                  'to_be_sampled':     {'view': 'visible', 'edit': 'visible'},
    #                  'sampled':           {'view': 'visible', 'edit': 'visible'},
    #                  'to_be_preserved':   {'view': 'visible', 'edit': 'visible'},
    #                  'sample_due':        {'view': 'visible', 'edit': 'visible'},
    #                  'sample_received':   {'view': 'visible', 'edit': 'visible'},
    #                  'expired':           {'view': 'visible', 'edit': 'visible'},
    #                  'disposed':          {'view': 'visible', 'edit': 'invisible'},
    #                  },
    #         catalog_name='bika_setup_catalog',
    #         base_query={'inactive_state': 'active'},
    #         showOn=True,
    #     ),
    # ),

    BooleanField('SamplingWorkflowEnabled',
                 default_method='getSamplingWorkflowEnabledDefault'
    ),

    DateTimeField('DateSampled',
        # mode="rw",
        # read_permission=permissions.View,
        # write_permission=SampleSample,
        # widget = DateTimeWidget(
        #     label=_("Date Sampled"),
        #     size=20,
        #     visible={'edit': 'visible',
        #              'view': 'visible',
        #              'header_table': 'visible',
        #              'sample_registered': {'view': 'invisible', 'edit': 'invisible'},
        #              'to_be_sampled':     {'view': 'visible', 'edit': 'visible'},
        #              'sampled':           {'view': 'visible', 'edit': 'invisible'},
        #              'to_be_preserved':   {'view': 'visible', 'edit': 'invisible'},
        #              'sample_due':        {'view': 'visible', 'edit': 'invisible'},
        #              'sample_received':   {'view': 'visible', 'edit': 'invisible'},
        #              'expired':           {'view': 'visible', 'edit': 'invisible'},
        #              'disposed':          {'view': 'visible', 'edit': 'invisible'},
        #              },
        #     render_own_label=True,
        # ),
    ),

    StringField('Sampler',
        # mode="rw",
        # read_permission=permissions.View,
        # write_permission=SampleSample,
        # vocabulary='getSamplers',
        # widget=BikaSelectionWidget(
        #     format='select',
        #     label=_("Sampler"),
        #     visible={'edit': 'visible',
        #              'view': 'visible',
        #              'header_table': 'visible',
        #              'sample_registered': {'view': 'invisible', 'edit': 'invisible'},
        #              'to_be_sampled':     {'view': 'visible', 'edit': 'visible'},
        #              'sampled':           {'view': 'visible', 'edit': 'invisible'},
        #              'to_be_preserved':   {'view': 'visible', 'edit': 'invisible'},
        #              'sample_due':        {'view': 'visible', 'edit': 'invisible'},
        #              'sample_received':   {'view': 'visible', 'edit': 'invisible'},
        #              'expired':           {'view': 'visible', 'edit': 'invisible'},
        #              'disposed':          {'view': 'visible', 'edit': 'invisible'},
        #              },
        #     render_own_label=True,
        # ),
    ),
    DateTimeField('SamplingDate',
                  readonly=True,
        # mode="rw",
        # read_permission=permissions.View,
        # write_permission=permissions.ModifyPortalContent,
        # widget = DateTimeWidget(
        #     label=_("Sampling Date"),
        #     visible={'edit': 'visible',
        #              'view': 'visible',
        #              'header_table': 'visible',
        #              'sample_registered': {'view': 'visible', 'edit': 'visible'},
        #              'to_be_sampled':     {'view': 'visible', 'edit': 'invisible'},
        #              'sampled':           {'view': 'visible', 'edit': 'invisible'},
        #              'to_be_preserved':   {'view': 'visible', 'edit': 'invisible'},
        #              'sample_due':        {'view': 'visible', 'edit': 'invisible'},
        #              'sample_received':   {'view': 'visible', 'edit': 'invisible'},
        #              'expired':           {'view': 'visible', 'edit': 'invisible'},
        #              'disposed':          {'view': 'visible', 'edit': 'invisible'},
        #              },
        #     render_own_label=True,
        # ),
    ),

    fields.Many2one(string='SamplingDeviation',
                   comodel_name='olims.sampling_deviation',
#         vocabulary_display_path_bound = sys.maxsize,
#         allowed_types = ('SamplingDeviation',),
#         relationship = 'SampleSamplingDeviation',
#         referenceClass = HoldingReference,
#         mode="rw",
#         read_permission=permissions.View,
#         write_permission=permissions.ModifyPortalContent,
#         widget=ReferenceWidget(
#             label=_("Sampling Deviation"),
#             render_own_label=True,
#             visible={'edit': 'visible',
#                      'view': 'visible',
#                      'header_table': 'visible',
#                      'sample_registered': {'view': 'visible', 'edit': 'visible'},
#                      'to_be_sampled':     {'view': 'visible', 'edit': 'visible'},
#                      'sampled':           {'view': 'visible', 'edit': 'visible'},
#                      'to_be_preserved':   {'view': 'visible', 'edit': 'visible'},
#                      'sample_due':        {'view': 'visible', 'edit': 'visible'},
#                      'sample_received':   {'view': 'visible', 'edit': 'invisible'},
#                      'expired':           {'view': 'visible', 'edit': 'invisible'},
#                      'disposed':          {'view': 'visible', 'edit': 'invisible'},
#                      },
#             catalog_name='bika_setup_catalog',
#             base_query={'inactive_state': 'active'},
#             showOn=True,
#         ),
    ),


    fields.Many2one(string='SampleCondition',
                   comodel_name='olims.sample_condition',
        # # vocabulary_display_path_bound=sys.maxsize,
        # allowed_types=('SamplePoint',),
        # relationship = 'SampleSamplePoint',
        # referenceClass = HoldingReference,
        # mode="rw",
        # read_permission=permissions.View,
        # write_permission=permissions.ModifyPortalContent,
        # widget=ReferenceWidget(
        #     label=_("Sample Point"),
        #     render_own_label=True,
        #     visible={'edit': 'visible',
        #              'view': 'visible',
        #              'header_table': 'visible',
        #              'sample_registered': {'view': 'visible', 'edit': 'visible'},
        #              'to_be_sampled':     {'view': 'visible', 'edit': 'invisible'},
        #              'sampled':           {'view': 'visible', 'edit': 'invisible'},
        #              'to_be_preserved':   {'view': 'visible', 'edit': 'invisible'},
        #              'sample_due':        {'view': 'visible', 'edit': 'invisible'},
        #              'sample_received':   {'view': 'visible', 'edit': 'invisible'},
        #              'expired':           {'view': 'visible', 'edit': 'invisible'},
        #              'disposed':          {'view': 'visible', 'edit': 'invisible'},
        #              },
        #     catalog_name='bika_setup_catalog',
        #     base_query={'inactive_state': 'active'},
        #     showOn=True,
        # ),

    ),

    DateTimeField('DateReceived',
        readonly=True,
        # mode="rw",
        # read_permission=permissions.View,
        # write_permission=permissions.ModifyPortalContent,
        # widget = DateTimeWidget(
        #     label=_("Date Received"),
        #     visible={'edit': 'visible',
        #              'view': 'visible',
        #              'header_table': 'visible',
        #              'sample_registered': {'view': 'invisible', 'edit': 'invisible'},
        #              'to_be_sampled':     {'view': 'invisible', 'edit': 'invisible'},
        #              'sampled':           {'view': 'invisible', 'edit': 'invisible'},
        #              'to_be_preserved':   {'view': 'invisible', 'edit': 'invisible'},
        #              'sample_due':        {'view': 'invisible', 'edit': 'invisible'},
        #              'sample_received':   {'view': 'visible', 'edit': 'invisible'},
        #              'expired':           {'view': 'visible', 'edit': 'invisible'},
        #              'disposed':          {'view': 'visible', 'edit': 'invisible'},
        #              },
        #     render_own_label=True,
        # ),
    ),

# ~~~~~~~ To be implemented ~~~~~~~
    fields.Many2one(string='Client',
           comodel_name = 'olims.client',
       ),
    # ComputedField('SampleTypeUID',
    #     expression = 'context.getSampleType().UID()',
    #     widget = ComputedWidget(
    #         visible=False,
    #     ),
    # ),
    # ComputedField('SamplePointUID',
    #     expression = 'context.getSamplePoint() and context.getSamplePoint().UID() or None',
    #     widget = ComputedWidget(
    #         visible=False,
    #     ),
    # ),
    BooleanField('Composite',
        # default = False,
        # mode="rw",
        # read_permission=permissions.View,
        # write_permission=permissions.ModifyPortalContent,
        # widget = BooleanWidget(
        #     label=_("Composite"),
        #     visible={'edit': 'visible',
        #              'view': 'visible',
        #              'header_table': 'visible',
        #              'sample_registered': {'view': 'visible', 'edit': 'visible'},
        #              'to_be_sampled':     {'view': 'visible', 'edit': 'visible'},
        #              'sampled':           {'view': 'visible', 'edit': 'visible'},
        #              'to_be_preserved':   {'view': 'visible', 'edit': 'visible'},
        #              'sample_due':        {'view': 'visible', 'edit': 'visible'},
        #              'sample_received':   {'view': 'visible', 'edit': 'visible'},
        #              'expired':           {'view': 'visible', 'edit': 'invisible'},
        #              'disposed':          {'view': 'visible', 'edit': 'invisible'},
        #              },
        #     render_own_label=True,
        # ),
    ),
    DateTimeField('DateExpired',
        readonly=True,
        # mode="rw",
        # read_permission=permissions.View,
        # write_permission=permissions.ModifyPortalContent,
        # widget = DateTimeWidget(
        #     label=_("Date Expired"),
        #     visible={'edit': 'visible',
        #              'view': 'visible',
        #              'header_table': 'visible',
        #              'sample_registered': {'view': 'invisible', 'edit': 'invisible'},
        #              'to_be_sampled':     {'view': 'invisible', 'edit': 'invisible'},
        #              'sampled':           {'view': 'invisible', 'edit': 'invisible'},
        #              'to_be_preserved':   {'view': 'invisible', 'edit': 'invisible'},
        #              'sample_due':        {'view': 'invisible', 'edit': 'invisible'},
        #              'sample_received':   {'view': 'invisible', 'edit': 'invisible'},
        #              'expired':           {'view': 'visible', 'edit': 'invisible'},
        #              'disposed':          {'view': 'visible', 'edit': 'invisible'},
        #              },
        #     render_own_label=True,
        # ),
    ),
  # ~~~~~~~ To be implemented ~~~~~~~
  #   ComputedField('DisposalDate',
  #       expression = 'context.disposal_date()',
  #       widget=DateTimeWidget(
  #           visible={'edit': 'visible',
  #                    'view': 'visible',
  #                    'header_table': 'visible',
  #                    'sample_registered': {'view': 'invisible', 'edit': 'invisible'},
  #                    'to_be_sampled':     {'view': 'visible', 'edit': 'invisible'},
  #                    'sampled':           {'view': 'visible', 'edit': 'invisible'},
  #                    'to_be_preserved':   {'view': 'visible', 'edit': 'invisible'},
  #                    'sample_due':        {'view': 'visible', 'edit': 'invisible'},
  #                    'sample_received':   {'view': 'visible', 'edit': 'invisible'},
  #                    'expired':           {'view': 'visible', 'edit': 'invisible'},
  #                    'disposed':          {'view': 'invisible', 'edit': 'invisible'},
  #                    },
  #           render_own_label=True,
  #       ),
  #   ),
    DateTimeField('DateDisposed',
        readonly=True,
        # mode="rw",
        # read_permission=permissions.View,
        # write_permission=permissions.ModifyPortalContent,
        # widget = DateTimeWidget(
        #     label=_("Date Disposed"),
        #     visible={'edit': 'visible',
        #              'view': 'visible',
        #              'header_table': 'visible',
        #              'sample_registered': {'view': 'invisible', 'edit': 'invisible'},
        #              'to_be_sampled':     {'view': 'invisible', 'edit': 'invisible'},
        #              'sampled':           {'view': 'invisible', 'edit': 'invisible'},
        #              'to_be_preserved':   {'view': 'invisible', 'edit': 'invisible'},
        #              'sample_due':        {'view': 'invisible', 'edit': 'invisible'},
        #              'sample_received':   {'view': 'invisible', 'edit': 'invisible'},
        #              'expired':           {'view': 'invisible', 'edit': 'invisible'},
        #              'disposed':          {'view': 'visible', 'edit': 'invisible'},
        #              },
        #     render_own_label=True,
        # ),
    ),
    BooleanField('AdHoc',
        # default=False,
        # mode="rw",
        # read_permission=permissions.View,
        # write_permission=permissions.ModifyPortalContent,
        # widget=BooleanWidget(
        #     label=_("Ad-Hoc"),
        #     visible={'edit': 'visible',
        #              'view': 'visible',
        #              'header_table': 'visible',
        #              'sample_registered': {'view': 'visible', 'edit': 'visible'},
        #              'to_be_sampled':     {'view': 'visible', 'edit': 'visible'},
        #              'sampled':           {'view': 'visible', 'edit': 'visible'},
        #              'to_be_preserved':   {'view': 'visible', 'edit': 'visible'},
        #              'sample_due':        {'view': 'visible', 'edit': 'visible'},
        #              'sample_received':   {'view': 'visible', 'edit': 'visible'},
        #              'expired':           {'view': 'visible', 'edit': 'invisible'},
        #              'disposed':          {'view': 'visible', 'edit': 'invisible'},
        #              },
        #    render_own_label=True,
        # ),
    ),
    TextField('Remarks',
        searchable=True,
        default_content_type='text/x-web-intelligent',
        # allowable_content_types = ('text/plain', ),
        # default_output_type="text/plain",
        # mode="rw",
        # read_permission=permissions.View,
        # write_permission=permissions.ModifyPortalContent,
        # widget=TextAreaWidget(
        #     macro="bika_widgets/remarks",
        #     label=_("Remarks"),
        #     append_only=True,
        # ),
    ),
    fields.Selection(string='state',
                     selection=SAMPLE_STATES,
                     default='sample_registered',
                     select=True,
                     required=True, readonly=True,
                     copy=False, track_visibility='always'
    ),
    ###ComputedField('Priority',
    ###    expression = 'context.getPriority() or None',
    ###    widget = ComputedWidget(
    ###        visible={'edit': 'visible',
    ###                 'view': 'visible'},
    ###        render_own_label=False,
    ###    ),
    ###),
)


#schema['title'].required = False


class Sample(models.Model, BaseOLiMSModel): #BaseFolder, HistoryAwareMixin
    _name = 'olims.sample'

    def compute_smapleId(self):
        for record in self:
            record.SampleID = 'S-0' + str(record.id)

    def compute_smapleName(self):
        for record in self:
            record.name = record.SampleID
    # implements(ISample)
    # security = ClassSecurityInfo()
    # displayContentsTab = False
    # schema = schema

    def actionToBeSampled(self,cr,uid,ids,context=None):
        self.write(cr, uid, ids, {
            'state': 'to_be_sampled',
        })
        return True

    _at_rename_after_creation = True

    def _renameAfterCreation(self, check_auto_id=False):
        from lims.idserver import renameAfterCreation
        renameAfterCreation(self)

    def _getCatalogTool(self):
        from lims.catalog import getCatalog
        return getCatalog(self)

    def Title(self):
        """ Return the Sample ID as title """
        return safe_unicode(self.getId()).encode('utf-8')

    def getSamplingWorkflowEnabledDefault(self):
        return self.bika_setup.getSamplingWorkflowEnabled()

    def getContactTitle(self):
        return ""

    def getClientTitle(self):
        proxies = self.getAnalysisRequests()
        if not proxies:
            return ""
        value = proxies[0].aq_parent.Title()
        return value

    def getProfilesTitle(self):
        return ""

    def getAnalysisCategory(self):
        analyses = []
        for ar in self.getAnalysisRequests():
            analyses += list(ar.getAnalyses(full_objects=True))
        value = []
        for analysis in analyses:
            val = analysis.getCategoryTitle()
            if val not in value:
                value.append(val)
        return value

    def getAnalysisService(self):
        analyses = []
        for ar in self.getAnalysisRequests():
            analyses += list(ar.getAnalyses(full_objects=True))
        value = []
        for analysis in analyses:
            val = analysis.getServiceTitle()
            if val not in value:
                value.append(val)
        return value

    def getAnalysts(self):
        analyses = []
        for ar in self.getAnalysisRequests():
            analyses += list(ar.getAnalyses(full_objects=True))
        value = []
        for analysis in analyses:
            val = analysis.getAnalyst()
            if val not in value:
                value.append(val)
        return value

    # Forms submit Title Strings which need
    # to be converted to objects somewhere along the way...
    def setSampleType(self, value, **kw):
        """ Accept Object, Title or UID, and convert SampleType title to UID
        before saving.
        """
        if hasattr(value, "portal_type") and value.portal_type == "SampleType":
            pass
        else:
            bsc = getToolByName(self, 'bika_setup_catalog')
            sampletypes = bsc(portal_type='SampleType', title=to_unicode(value))
            if sampletypes:
                value = sampletypes[0].UID
            else:
                sampletypes = bsc(portal_type='SampleType', UID=value)
                if sampletypes:
                    value = sampletypes[0].UID
                else:
                    value = None
        for ar in self.getAnalysisRequests():
            ar.Schema()['SampleType'].set(ar, value)
        return self.Schema()['SampleType'].set(self, value)

    # Forms submit Title Strings which need
    # to be converted to objects somewhere along the way...
    def setSamplePoint(self, value, **kw):
        """ Accept Object, Title or UID, and convert SampleType title to UID
        before saving.
        """
        if hasattr(value, "portal_type") and value.portal_type == "SamplePoint":
            pass
        else:
            bsc = getToolByName(self, 'bika_setup_catalog')
            sampletypes = bsc(portal_type='SamplePoint', title=to_unicode(value))
            if sampletypes:
                value = sampletypes[0].UID
            else:
                sampletypes = bsc(portal_type='SamplePoint', UID=value)
                if sampletypes:
                    value = sampletypes[0].UID
                else:
                    value = None
        for ar in self.getAnalysisRequests():
            ar.Schema()['SamplePoint'].set(ar, value)
        return self.Schema()['SamplePoint'].set(self, value)

    def setClientReference(self, value, **kw):
        """ Set the field on Analysis Requests.
        """
        for ar in self.getAnalysisRequests():
            ar.Schema()['ClientReference'].set(ar, value)
        self.Schema()['ClientReference'].set(self, value)

    def setClientSampleID(self, value, **kw):
        """ Set the field on Analysis Requests.
        """
        for ar in self.getAnalysisRequests():
            ar.Schema()['ClientSampleID'].set(ar, value)
        self.Schema()['ClientSampleID'].set(self, value)

    def setAdHoc(self, value, **kw):
        """ Set the field on Analysis Requests.
        """
        for ar in self.getAnalysisRequests():
            ar.Schema()['AdHoc'].set(ar, value)
        self.Schema()['AdHoc'].set(self, value)

    def setComposite(self, value, **kw):
        """ Set the field on Analysis Requests.
        """
        for ar in self.getAnalysisRequests():
            ar.Schema()['Composite'].set(ar, value)
        self.Schema()['Composite'].set(self, value)

    #security.declarePublic('getAnalysisRequests')

    def getAnalysisRequests(self):
        tool = getToolByName(self, REFERENCE_CATALOG)
        ar = ''
        ars = []
        uids = [uid for uid in
                tool.getBackReferences(self, 'AnalysisRequestSample')]
        for uid in uids:
            reference = uid
            ar = tool.lookupObject(reference.sourceUID)
            ars.append(ar)
        return ars

    #security.declarePublic('getAnalyses')

    def getAnalyses(self, contentFilter):
        """ return list of all analyses against this sample
        """
        analyses = []
        for ar in self.getAnalysisRequests():
            analyses += ar.getAnalyses(**contentFilter)
        return analyses

    def getSamplers(self):
        return getUsers(self, ['LabManager', 'Sampler'])

    def disposal_date(self):
        """ Calculate the disposal date by returning the latest
            disposal date in this sample's partitions """

        parts = self.objectValues("SamplePartition")
        dates = []
        for part in parts:
            date = part.getDisposalDate()
            if date:
                dates.append(date)
        if dates:
            dis_date = dt2DT(max([DT2dt(date) for date in dates]))
        else:
            dis_date = None
        return dis_date

    def getLastARNumber(self):
        ARs = self.getBackReferences("AnalysisRequestSample")
        prefix = self.getSampleType().getPrefix()
        ar_ids = sorted([AR.id for AR in ARs if AR.id.startswith(prefix)])
        try:
            last_ar_number = int(ar_ids[-1].split("-R")[-1])
        except:
            return 0
        return last_ar_number

    def workflow_script_sample_receive(self,cr,uid,ids,context=None):
        datereceive = datetime.datetime.now()
        self.write(cr, uid, ids, {
            'state': 'sample_received','DateReceived': datereceive,
        })
        return True
    # def workflow_script_receive(self):
        # workflow = getToolByName(self, 'portal_workflow')
        # self.setDateReceived(DateTime())
        # self.reindexObject(idxs=["review_state", "getDateReceived"])
        # # Receive all self partitions that are still 'sample_due'
        # parts = self.objectValues('SamplePartition')
        # sample_due = [sp for sp in parts
        #               if workflow.getInfoFor(sp, 'review_state') == 'sample_due']
        # for sp in sample_due:
        #     workflow.doActionFor(sp, 'receive')
        # # when a self is received, all associated
        # # AnalysisRequests are also transitioned
        # for ar in self.getAnalysisRequests():
        #     doActionFor(ar, "receive")

    def workflow_script_preserve(self):
        """This action can happen in the Sample UI, so we transition all
        self partitions that are still 'to_be_preserved'
        """
        workflow = getToolByName(self, 'portal_workflow')
        parts = self.objectValues("SamplePartition")
        tbs = [sp for sp in parts
               if workflow.getInfoFor(sp, 'review_state') == 'to_be_preserved']
        for sp in tbs:
            doActionFor(sp, "preserve")
        # All associated AnalysisRequests are also transitioned
        for ar in self.getAnalysisRequests():
            doActionFor(ar, "preserve")
            ar.reindexObject()

    def workflow_script_expire(self,cr,uid,ids,context=None):
        expired_date = datetime.datetime.now()
        self.write(cr, uid, ids, {
            'state': 'expired', 'DateExpired': expired_date,
        })
        return True
        # self.setDateExpired(DateTime())
        # self.reindexObject(idxs=["review_state", "getDateExpired", ])

    def workflow_script_dispose(self,cr,uid,ids,context=None):
        date_disposed = datetime.datetime.now()
        self.write(cr, uid, ids, {
            'state': 'disposed', 'DateDisposed': date_disposed
        })
        return True
        # self.setDateDisposed(DateTime())
        # self.reindexObject(idxs=["review_state", "getDateDisposed", ])

    def workflow_script_sample(self,cr,uid,ids,context=None):
        self.write(cr, uid, ids, {
            'state': 'sampled',
        })
        return True

        # if skip(self, "sample"):
        #     return
        # workflow = getToolByName(self, 'portal_workflow')
        # parts = self.objectValues('SamplePartition')
        # # This action can happen in the Sample UI.  So we transition all
        # # partitions that are still 'to_be_sampled'
        # tbs = [sp for sp in parts
        #        if workflow.getInfoFor(sp, 'review_state') == 'to_be_sampled']
        # for sp in tbs:
        #     doActionFor(sp, "sample")
        # # All associated AnalysisRequests are also transitioned
        # for ar in self.getAnalysisRequests():
        #     doActionFor(ar, "sample")
        #     ar.reindexObject()

    def workflow_script_to_be_preserved(self,cr,uid,ids,context=None):
        self.write(cr, uid, ids, {
            'state': 'to_be_preserved',
        })
        return True
        # if skip(self, "to_be_preserved"):
        #     return
        # workflow = getToolByName(self, 'portal_workflow')
        # parts = self.objectValues('SamplePartition')
        # # Transition our children
        # tbs = [sp for sp in parts
        #        if workflow.getInfoFor(sp, 'review_state') == 'to_be_preserved']
        # for sp in tbs:
        #     doActionFor(sp, "to_be_preserved")
        # # All associated AnalysisRequests are also transitioned
        # for ar in self.getAnalysisRequests():
        #     doActionFor(ar, "to_be_preserved")
        #     ar.reindexObject()

    def workflow_script_sample_due(self,cr,uid,ids,context=None):
        self.write(cr, uid, ids, {
            'state': 'sample_due',
        })
        return True
        # if skip(self, "sample_due"):
        #     return
        # # All associated AnalysisRequests are also transitioned
        # for ar in self.getAnalysisRequests():
        #     doActionFor(ar, "sample_due")
        #     ar.reindexObject()

    def workflow_script_reinstate(self):
        if skip(self, "reinstate"):
            return
        workflow = getToolByName(self, 'portal_workflow')
        parts = self.objectValues('SamplePartition')
        self.reindexObject(idxs=["cancellation_state", ])
        # Re-instate all self partitions
        for sp in [sp for sp in parts
                   if workflow.getInfoFor(sp, 'cancellation_state') == 'cancelled']:
            workflow.doActionFor(sp, 'reinstate')
        # reinstate all ARs for this self.
        ars = self.getAnalysisRequests()
        for ar in ars:
            if not skip(ar, "reinstate", peek=True):
                ar_state = workflow.getInfoFor(ar, 'cancellation_state')
                if ar_state == 'cancelled':
                    workflow.doActionFor(ar, 'reinstate')

    def workflow_script_cancel(self):
        if skip(self, "cancel"):
            return
        workflow = getToolByName(self, 'portal_workflow')
        parts = self.objectValues('SamplePartition')
        self.reindexObject(idxs=["cancellation_state", ])
        # Cancel all partitions
        for sp in [sp for sp in parts
                   if workflow.getInfoFor(sp, 'cancellation_state') == 'active']:
            workflow.doActionFor(sp, 'cancel')
        # cancel all ARs for this self.
        ars = self.getAnalysisRequests()
        for ar in ars:
            if not skip(ar, "cancel", peek=True):
                ar_state = workflow.getInfoFor(ar, 'cancellation_state')
                if ar_state == 'active':
                    workflow.doActionFor(ar, 'cancel')

    def guard_receive_transition(self):
        """Prevent the receive transition from being available:
        - if object is cancelled
        - if any related ARs have field analyses with no result.
        """
        # Can't do anything to the object if it's cancelled
        if not isBasicTransitionAllowed(self):
            return False
        # check if any related ARs have field analyses with no result.
        for ar in self.getAnalysisRequests():
            field_analyses = ar.getAnalyses(getPointOfCapture='field',
                                            full_objects=True)
            no_results = [a for a in field_analyses if a.getResult() == '']
            if no_results:
                return False
        return True

#atapi.registerType(Sample, PROJECTNAME)

Sample.initialze(schema)