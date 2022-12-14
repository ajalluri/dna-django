from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import time 
import json 
from rest_framework.decorators import authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from .models import User
@api_view(["GET"])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))

def get_user_data(request,userid):
    
    # json_file_path = "./userapp/static/users.json"

    # with open(json_file_path, 'r') as j:
    #     data = json.loads(j.read())
    
    # for x in data:
    #     if list(x.keys())[0]==userid:
    #         return Response(x[userid])


    data = User.objects.all().filter(userid = userid).first()

    if data :

        return Response({"UserName":data.username,"Email":data.email,"designation" : data.designation,"skills":data.skills.split(",") })

   
    
    return Response({"Message":"UserID Not Found"})


@api_view(["POST"])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def store_user_data(request,userid):
    
    
    json_file_path = "./userapp/static/users.json"

    with open(json_file_path, 'r') as j:
        data = json.loads(j.read())
    
    for x in data:

        if list(x.keys())[0]==userid:

            user_infor = x[userid]
           
            user_infor["skills"] = ",".join(user_infor["skills"])

            print(user_infor)
            
            try :
                data = User.objects.all().filter(userid = userid).first()
                
                if data :
                    pass
                
                else:

                    usermodel = User(designation = user_infor["designation"],skills = user_infor["skills"],username = user_infor["userName"],email = user_infor["email"],userid=userid)
                    usermodel.save()

            except:
                return Response({"Message":"User Model is Wrong"})



    return Response({"Message":"UserID Data Stored in DataBase"})


@api_view(["GET","POST"])
def apitesting(request):
    print(request.META.get('HTTP_AUTHORIZATION', b''))
    return Response({"data":request.META.get('HTTP_AUTHORIZATION', b'')})