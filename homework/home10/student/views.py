from django.shortcuts import render,redirect,get_object_or_404
from .forms import StudentForm
from .models import Student
from django.db.models import Q


def home(request):
    query = request.GET.get('q')
    if query:
        students = Student.objects.filter(Q(name__icontains=query))
    else:
        students = Student.objects.all().order_by('id')
    return render(request, 'home.html', {'students': students})



def add_student(request):
    if request.method == "POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm(instance=student)
    return render(request, 'edit_student.html', {'form': form})

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('home')
