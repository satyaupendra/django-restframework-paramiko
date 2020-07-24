from django.shortcuts import render

# Create your views here.

# Create your views here.
from rest_framework.views import APIView
from .serializers import ParamikoSerializer
from .models import ParamikoModel
from rest_framework.response import Response
import paramiko

class SshConnectionView(APIView):
    def post(self,request):
        user_name=request.data['user_name']
        passwd=request.data['password']
        ip=request.data['ip']
        pathToFile=request.data['pathToFile']
        #print(request.data) 
        serializer=ParamikoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #print(ip)
            ssh_client=paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(hostname=ip,username=user_name,password=passwd)
            cmd="python {pathToFile}".format(pathToFile=pathToFile)
            stdin,stdout,stderr=ssh_client.exec_command(cmd)
            # stdout=stdout.readlines()
            print("Hello")
            return Response(stdout)
        return Response(serializer.errors)