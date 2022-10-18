from django.forms import Form
from django.shortcuts import render, redirect


# Create your views here.
def form(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        gender = request.POST['gender']
        phone= request.POST['phone']
        address= request.POST['address']
        department= request.POST['subject']
        courses= request.POST['topic']
        code= request.POST['chapter']
        purpose= request.POST['purpose']
        materials= request.POST['material']
        form = Form.Objects.create_form(firstname=firstname, gender=gender, phone=phone, address=address, department= department,
                                        courses= courses, topic=code, purpose=purpose, material=materials)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form= form()
            return redirect('store/form')


    return render(request, "forms.html")
