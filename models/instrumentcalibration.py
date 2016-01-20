# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# from dependencies.dependency import ClassSecurityInfo
# from dependencies.dependency import schemata
# from dependencies import atapi
# from dependencies.dependency import *
# from dependencies.dependency import getToolByName
# from lims import bikaMessageFactory as _
# from lims.utils import t
# from lims.browser.widgets import DateTimeWidget, ReferenceWidget
# from lims.config import PROJECTNAME
# from lims.content.bikaschema import BikaSchema



from lims import bikaMessageFactory as _
from fields.string_field import StringField
from fields.text_field import TextField
from fields.date_time_field import DateTimeField
from fields.widget.widget import StringWidget, TextAreaWidget, DateTimeWidget
from openerp import fields, models, api
from base_olims_model import BaseOLiMSModel
from messagealert import write_message

#schema = BikaSchema.copy() + Schema((
schema = (StringField('AssetNumber',
                      required=1,
                      widget = StringWidget(
                            label=_("Asset Number"),
        )
    ),

    # ReferenceField('Instrument',
    #     allowed_types=('Instrument',),
    #     relationship='InstrumentCalibrationInstrument',
    #     widget=StringWidget(
    #         visible=False,
    #     )
    # ),

    fields.Many2one(string='Instrument',
                   comodel_name='olims.instrument',
                   required=False,

    ),


# ~~~~~~~ To be implemented ~~~~~~~
    # ComputedField('InstrumentUID',
    #     expression = 'context.getInstrument() and context.getInstrument().UID() or None',
    #     widget=ComputedWidget(
    #         visible=False,
    #     ),
    # ),

    DateTimeField('DateIssued',
        with_time = 1,
        with_date = 1,
        widget = DateTimeWidget(
            label=_("Report Date"),
            description=_("Calibration report date"),
        ),
    ),

    DateTimeField('DownFrom',
        with_time = 1,
        with_date = 1,
        widget = DateTimeWidget(
            label=_("From"),
            description=_("Date from which the instrument is under calibration"),
        ),
    ),

    DateTimeField('DownTo',
        with_time = 1,
        with_date = 1,
        widget = DateTimeWidget(
            label=_("To"),
            description=_("Date until the instrument will not be available"),
        ),
    ),

    StringField('Calibrator',
        widget = StringWidget(
            label=_("Calibrator"),
            description=_("The analyst or agent responsible of the calibration"),
        )
    ),

    TextField('Considerations',
        default_content_type = 'text/plain',
        allowed_content_types= ('text/plain', ),
        default_output_type="text/plain",
        widget = TextAreaWidget(
            label=_("Considerations"),
            description=_("Remarks to take into account before calibration"),
        ),
    ),

    TextField('WorkPerformed',
     #   default_content_type = 'text/plain',
     #   allowed_content_types= ('text/plain', ),
     #   default_output_type="text/plain",
        widget = TextAreaWidget(
            label=_("Work Performed"),
            description=_("Description of the actions made during the calibration"),
        ),
    ),

    fields.Many2one(string='Worker',
                   comodel_name='olims.lab_contact',
                   required=False,
                    #  vocabulary='getLabContacts',
                    # allowed_types=('LabContact',),
                    # relationship='LabContactInstrumentCalibration',
                    # widget=ReferenceWidget(
                    #     checkbox_bound=0,
                    #     label=_("Performed by"),
                    #     description=_("The person at the supplier who performed the task"),
                    #     size=30,
                    #     base_query={'inactive_state': 'active'},
                    #     showOn=True,
                    #     colModel=[{'columnName': 'UID', 'hidden': True},
                    #               {'columnName': 'JobTitle', 'width': '20', 'label': _('Job Title')},
                    #               {'columnName': 'Title', 'width': '80', 'label': _('Name')}
                    #              ],
                    # ),

    ),

    StringField('ReportID',
        widget = StringWidget(
            label=_("Report ID"),
            description=_("Report identification number"),
        )
    ),

    TextField('Remarks',
        default_content_type = 'text/plain',
        allowed_content_types= ('text/plain', ),
        default_output_type="text/plain",
        widget = TextAreaWidget(
            label=_("Remarks"),
        ),
    ),

)

#schema['title'].widget.label = 'Asset Number'
sourcemodel = "InstrumentCalibration"

class InstrumentCalibration(models.Model, BaseOLiMSModel): #BaseFolder
    _name = 'olims.instrument_calibration'
    # security = ClassSecurityInfo()
    # schema = schema
    # displayContentsTab = False

    @api.model
    def create(self, values):
        write_message(self, values, sourcemodel)
        new_record = super(InstrumentCalibration, self).create(values)
        return new_record

    @api.multi
    def write(self, data):
        write_message(self, data, sourcemodel)
        res = super(InstrumentCalibration, self).write(data)
        return res


    _at_rename_after_creation = True
    def _renameAfterCreation(self, check_auto_id=False):
        from lims.idserver import renameAfterCreation
        renameAfterCreation(self)

    def getLabContacts(self):
        bsc = getToolByName(self, 'bika_setup_catalog')
        # fallback - all Lab Contacts
        pairs = []
        for contact in bsc(portal_type='LabContact',
                           inactive_state='active',
                           sort_on='sortable_title'):
            pairs.append((contact.UID, contact.Title))
        return DisplayList(pairs)

#atapi.registerType(InstrumentCalibration, PROJECTNAME)
InstrumentCalibration.initialze(schema)