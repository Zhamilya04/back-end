from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from todo_app.models import TodoList, Todo
from todo_app.serializers import TodoListSerializer, TodoSerializer
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json
from lecture_5.settings import STATIC_URL

def home_page(request):
    todolists = TodoList.objects.all()
    return render(request, 'todo_app/index.html', {'STATIC_URL': STATIC_URL, 'todolists': todolists})

def about_page(request):
    return render(request, 'todo_app/about.html')


def category_page(request, pk):
    todolist = TodoList.objects.get(id=pk)
    return render(request, 'todo_app/category.html', {'STATIC_URL': STATIC_URL, 'todolist': todolist})

@csrf_exempt
def todolist_handler(request):
    if request.method == 'GET':
        todolist = TodoList.objects.all()
        serializer = TodoListSerializer(todolists, many=True)
        return JsonResponse(serializer.data, status=200, safe=False)
    if request.method == 'POST':
        data = json.loads(request.body)
        serializer = TodoListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, status=200)
        return JsonResponse(data=serializer.errors, status=400)
    return JsonResponse({'message': 'Request is not supported'}, status=400)


def get_category(pk):
    try:
        todolist = TodoList.objects.get(id=pk)
        return {
            'status': 200,
            'todolist': todolist
        }
    except TodoList.DoesNotExist as e:
        return {
            'status': 404,
            'todolist': None
        }


@csrf_exempt
def todolist_handler(request, pk):
    result = get_todolist(pk)

    if result['status'] == 404:
        return JsonResponse({'message': 'TodoList not found'}, status=404)

    todolist = result['todolist']

    if request.method == 'GET':
        serializer = TodoListSerializer(todolist)
        return JsonResponse(serializer.data, status=200)
    if request.method == 'PUT':
        data = json.loads(request.body)
        serializer = TodoListSerializer(data=data, instance=todolist)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data)
        return JsonResponse(data=serializer.errors, status=400)
    if request.method == 'DELETE':
        todolist.delete()
        return JsonResponse({'message': 'TodoList deleted successfully!'})
    return JsonResponse({'message': 'Request is not supported'}, status=400)


@csrf_exempt
def todolist_todo_handler(request, pk):
    result = get_todolist(pk)

    if result['status'] == 404:
        return JsonResponse({'message': 'TodoList not found'}, status=404)

    category = result['todolist']

    if request.method == 'GET':
        todo = todolist.product_set.all()
        serializer = TodoSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        data = json.loads(request.body)
        data['todolist_id'] = pk
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    return JsonResponse({'message': 'Request is not supported'}, status=400)


def get_product(pk):
    try:
        todo = Todo.objects.get(id=pk)
        return {
            'status': 200,
            'product': todo
        }
    except Todo.DoesNotExist as e:
        return {
            'status': 404,
            'todo': None
        }


@csrf_exempt
def todo_handler(request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        data = json.loads(request.body)
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    return JsonResponse({'message': 'Request is not supported'}, status=400)


@csrf_exempt
def todo_handler(request, pk):
    result = get_todo(pk)

    if result['status'] == 404:
        return JsonResponse({'message': 'Todo not found'}, status=404)

    todo = result['todo']

    if request.method == 'GET':
        serializer = TodoSerializer(product)
        return JsonResponse(serializer.data)
    if request.method == 'PUT':
        data = json.loads(request.body)
        serializer = TodoSerializer(instance=todo, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, safe=False, status=400)
    if request.method == 'DELETE':
        todo.delete()
        serializer = TodoSerializer(product)
        return JsonResponse(serializer.data, status=200, safe=False)
    return JsonResponse({'message': 'Request is not supported'}, status=400)

