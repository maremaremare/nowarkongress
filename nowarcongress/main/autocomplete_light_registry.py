# -*- coding: utf-8 -*-
import autocomplete_light
from person.models import Person

# # This will generate a PersonAutocomplete class
# autocomplete_light.register(Person,
#     # Just like in ModelAdmin.search_fields
#     search_fields=['name'],
#     # This will actually html attribute data-placeholder which will set
#     # javascript attribute widget.autocomplete.placeholder.
#     autocomplete_js_attributes={'placeholder': u'Начните вводить имя человека',},
# )



autocomplete_light.register(Person, 
    autocomplete_light.AutocompleteModelTemplate, 
    search_fields=['name'],
    autocomplete_js_attributes={'placeholder': u'Начните вводить имя человека',},
    choice_template='personautocomplete.html')