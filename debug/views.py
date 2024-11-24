from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect

def session_dump(request):
    session = {
        "_session_key_id": request.session._session_key
    }
    for key, val in request.session.items():
        session[key] = val
    return JsonResponse(session)


def session_put(request, key, val):
    request.session[key] = val
    return redirect('debug_session_dump')


def session_del(request, key):
    try:
        del request.session[key]
    except KeyError:
        pass

    return redirect('debug_session_dump')
