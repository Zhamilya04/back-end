from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from students.models import Student
from students.serializers import StudentSerializer
from django.views.decorators.csrf import csrf_exempt
import json



@csrf_exempt
def handle_student(request):
    if request.method == 'GET':
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return JsonResponse(data=serializer.data, status=200, safe=False)
    if request.method == 'POST':
        data = json.loads(request.body)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, status=200)
        return JsonResponse(data=serializer.errors, status=400)
    return JsonResponse({'message': 'Request is not supported'}, status=400, safe=False)


def get_student(pk):
    try:
        student = Student.objects.get(id=pk)
        return {
            'student': student,
            'status': 200
        }
    except Student.DoesNotExist as e:
        return {
            'student': None,
            'status': 404
        }




@csrf_exempt
def handle_student(request, pk):
    result = get_student(pk)

    if result['status'] == 404:
        return JsonResponse({'message': 'Student not found'}, status=404, safe=False)

    student = result['student']

    if request.method == 'GET':
        serializer = StudentySerializer(student)
        return JsonResponse(serializer.data, status=200, safe=False)
    if request.method == 'PUT':
        data = json.loads(request.body)
        serializer = StudentSerializer(data=data, instance=student)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, status=200)
        return JsonResponse(data=serializer.errors, status=400)
    if request.method == 'DELETE':
        category.delete()
        return JsonResponse({'message': 'Student is deleted successfully!'}, status=200, safe=False)
    return JsonResponse({'message': 'Request is not supported'}, status=400, safe=False)

