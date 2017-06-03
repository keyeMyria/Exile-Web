from django.shortcuts import HttpResponse


def response(data, status):
    method = ['POST', 'GET', 'OPTIONS', 'PUT', 'DELETE']
    response = HttpResponse(data, status=status,
                            content_type='application/json')
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Methods'] = method
    return response
# end def
