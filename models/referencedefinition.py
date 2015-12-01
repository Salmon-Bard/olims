""" Reference Definitions represent standard specifications for
    reference samples used in quality control
"""
# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# from dependencies.dependency import ClassSecurityInfo
# from dependencies.dependency import DateTime
# from dependencies.dependency import *
# from lims.content.bikaschema import BikaSchema
# from lims.browser.fields import ReferenceResultsField
# from lims.browser.widgets import ReferenceResultsWidget
# from lims.config import PROJECTNAME
# import sys
# import time
# from lims import PMF, bikaMessageFactory as _
# from dependencies.dependency import implements

from openerp import fields, models
from base_olims_model import BaseOLiMSModel
from lims import bikaMessageFactory as _
from fields.boolean_field import BooleanField
from fields.widget.widget import BooleanWidget, TextAreaWidget
from fields.string_field import StringField
from fields.text_field import TextField




#schema = BikaSchema.copy() + Schema((
schema = (
# ~~~~~~~ To be implemented ~~~~~~~
    # ReferenceResultsField('ReferenceResults',
    #     schemata = 'Reference Values',
    #     required = 1,
    #     subfield_validators = {
    #         'result':'referencevalues_validator',
    #         'min':'referencevalues_validator',
    #         'max':'referencevalues_validator',
    #         'error':'referencevalues_validator'},
    #     widget = ReferenceResultsWidget(
    #         label=_("Reference Values"),
    #         description =_(
    #             "Click on Analysis Categories (against shaded background"
    #             "to see Analysis Services in each category. Enter minimum "
    #             "and maximum values to indicate a valid results range. "
    #             "Any result outside this range will raise an alert. "
    #             "The % Error field allows for an % uncertainty to be "
    #             "considered when evaluating results against minimum and "
    #             "maximum values. A result out of range but still in range "
    #             "if the % error is taken into consideration, will raise a "
    #             "less severe alert."),
    #     ),
    # ),
    StringField('name',
              required=1,        
    ),
    TextField('Description',
                widget=TextAreaWidget(
                    description = _('Used in item listings and search results.'),
                            )
    ),
    BooleanField('Blank',
        schemata = 'Description',
        default = False,
        widget = BooleanWidget(
            label=_("Blank"),
            description=_("Reference sample values are zero or 'blank'"),
        ),
    ),
    BooleanField('Hazardous',
        schemata = 'Description',
        default = False,
        widget = BooleanWidget(
            label=_("Hazardous"),
            description=_("Samples of this type should be treated as hazardous"),
        ),
    ),
)

# schema['title'].schemata = 'Description'
# schema['title'].widget.visible = True
# schema['description'].schemata = 'Description'
# schema['description'].widget.visible = True

class ReferenceDefinition(models.Model, BaseOLiMSModel): #BaseContent
    _name ='olims.reference_definition'
    # security = ClassSecurityInfo()
    # displayContentsTab = False
    # schema = schema

    _at_rename_after_creation = True
    def _renameAfterCreation(self, check_auto_id=False):
        from lims.idserver import renameAfterCreation
        renameAfterCreation(self)

#registerType(ReferenceDefinition, PROJECTNAME)
ReferenceDefinition.initialze(schema)