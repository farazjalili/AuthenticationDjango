from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import jwt
import json
import datetime
from django.contrib.sessions.models import Session
# Create your views here.


def login_jwt(request):
    #username = request.POST.get['username']
    #password = request.POST.get['password']
    username = 'fjalili'
    password = '12345678'
    user = authenticate(username=username, password=password)
    if user is None:
        return Response(json.dumps({'Error': "Invalid credentials"}), status=400, content_type="application/json")
    else:
        # No backend authenticated the credentials
        payload = {
            'id': user.id,
            'email': user.email,
        }
        jwt_token = {'token': jwt.encode(payload, "SECRET_KEY")}
        jwt_token['token'] = jwt_token['token'].decode('utf-8')
        return HttpResponse(json.dumps(jwt_token), status=200, content_type="application/json")


def login_session(request):
    username = 'fjalili'
    password = '12345678'
    user = authenticate(username=username, password=password)


    if user is None:
        return Response(json.dumps({'Error': "Invalid credentials"}), status=400, content_type="application/json")
    else:
        # TODO : Check Browser support save cookies or Not !
        '''
        when use below line :
        The "Set-Cookie" header is sent from the web server and the browser sends the cookie back to the server in an HTTP header called "Cookie"
        The Set-Cookie HTTP response header is used to send cookies from the server to the user agent, so the user agent can send them back to the server later.
        '''
        request.session['user_id'] = user.id
        return HttpResponse(json.dumps({'message': "success login"}), status=200, content_type="application/json")


def session_info(request):
    sessionInfo = Session.objects.get(pk=request.session.session_key)
    return HttpResponse(json.dumps({'expireDate': str(sessionInfo.expire_date) ,
                                    'session_data': sessionInfo.session_data ,
                                    'session_data_decode': sessionInfo.get_decoded() }), status=200, content_type="application/json")


def reset_password(request):
    #username = request.POST.get['username']
    #password = request.POST.get['password']
    username = 'fjalili'
    password = '12345678'
    user = User.objects.get(username=username)
    '''
    #The password is actually stored as a salted hash and thus can’t be edited directly.  
    and format is : hashtype$salt$hash (That’s a hash type, the salt, and the hash itself, separated by the dollar sign ($) character.)
    '''
    user.set_password(password)
    user.save()

def logout_session(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")


def checkPassword(_clearPass,_dbPass):
    encypt_pass = 'pbkdf2_sha256$150000$vHivSxLD9QXR$xpr7mfdB3grm3DEOY+xG5lWbRgG0gOfKq0WEeJ/O1fs='
    clear_pass = '12345678'
    # print check_password('12345678', 'pbkdf2_sha256$150000$vHivSxLD9QXR$xpr7mfdB3grm3DEOY+xG5lWbRgG0gOfKq0WEeJ/O1fs=')