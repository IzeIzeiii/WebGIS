from rest_framework.decorators import api_view
from .models import Course
from .serializers import CourseSerializer
from rest_framework.response import Response
from rest_framework import status

@api_view(["GET","POST"])
def course_list(req):
    if req.method == "GET":
        s=CourseSerializer(instance=Course.objects.all(),many=True)
        return Response(data=s.data,status=status.HTTP_200_OK)
    if req.method == "POST":
        s=CourseSerializer(data=req.data,partial=True)
        if s.is_valid():
            s.save(teacher=req.user)
            return Response(data=s.data,status=status.HTTP_201_CREATED)
        return Response(s.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET","PUT","DELETE"])
def course_detial(req,pk):
    try:
        dt=Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response(data={"msg":"没这课"},status=status.HTTP_404_NOT_FOUND)
    if req.method == "GET":
        s=CourseSerializer(instance=dt)
        return Response(data=s.data,status=status.HTTP_200_OK)
    if req.method == "PUT":
        s=CourseSerializer(instance=dt,data=req.data)
        if s.is_valid():
            s.save()
            return Response(data=s.data,status=status.HTTP_200_OK)
    if req.method == "DELETE":
        dt.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# import json
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
# from django.views import View

# course_dict = {"name": "课程名称", "introduction": "课程简介", "price": 0.11}

# @csrf_exempt
# def course_list(req):
#     if req.method == "GET":
#         # return HttpResponse(json.dumps(course_dict),content_type='application/json')
#         return JsonResponse(course_dict)
#     if req.method == "POST":
#         course = json.loads(req.body.decode("utf-8"))
#         # return JsonResponse(course,safe=False)
#         return HttpResponse(json.dumps(course),content_type='application/json')

# @method_decorator(csrf_exempt,name='dispatch')
# class CourseList(View):
#     def get(self):
#         return JsonResponse(course_dict)

#     def post(self,req):
#         course = json.loads(req.body.decode("utf-8"))
#         # return JsonResponse(course,safe=False)
#         return HttpResponse(json.dumps(course),content_type='application/json')