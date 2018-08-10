from django.http import HttpResponse, HttpResponseRedirect


def home(request):

    response = HttpResponse(content_type='application/json')
    response = HttpResponse(content_type='text/html')
    response.write("<p>Content</p>")
    response.write("<p>is</p>")
    response.write("<p>added</p>")
    response.write("<p>not</p>")
    response.write("<p>replaced</p>")
    response.status_code = 404
    #you can fake a 404 and get user info through the request
    response.content = "<p>Page not found</p>"

    return response


def redirect_adm(request):
    return HttpResponseRedirect('/admin')
