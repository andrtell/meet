from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import reverse

def view(request):
    session = {
        "_session_key_id": request.session._session_key
    }
    for key, val in request.session.items():
        session[key] = val
    return JsonResponse(session)

def do_set(request, key, val):
    request.session[key] = val
    return HttpResponseRedirect(reverse('session_info_view'))

def do_del(request, key):
    del request.session[key]
    return HttpResponseRedirect(reverse('session_info_view'))
