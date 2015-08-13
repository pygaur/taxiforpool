import locale

from django.db.models import get_model
from django.http import HttpResponse
from django.utils import simplejson

from smart_selects.utils import unicode_sorter


def filterchain(request, app, model, field, manager=None):
    model_class = get_model(app, model)
    queryset = model_class._default_manager
    results = list(queryset.all().values_list('option_name'))
    results.sort(cmp=locale.strcoll, key=lambda x: unicode_sorter(unicode(x)))
    json = simplejson.dumps(results)
    return HttpResponse(json, mimetype='application/json')
