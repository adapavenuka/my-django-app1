#import csv
from reportlab.pdfgen import canvas

from django.shortcuts import render
# from reportlab.pdfgen import canvas
from django.http import HttpResponse
from myapp.form import StudentForm
# from django.shortcuts import render
# from django.http import HttpResponse
#from myapp.functions.functions import handle_uploaded_file
#from myapp.models import Employee


#importing loading from django template
#from django.template import loader

# Create your views here.
#from django.http import HttpResponse

def index(request):
    if request.method=="POST":
        student=StudentForm(request.POST,request.FILES)
        if student.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("File Uploaded Succesfully")
    else:
        student=StudentForm()
        return render(request,'index.html',{'form':student})

# def getpdf(request):
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename = "file.pdf"'
#     p = canvas.Canvas(response)
#     p.setFont("Times-Roman", 55)
#     p.drawString(100,700,"Hello, Javatpoint")
#     p.showPage()
#     p.save()
#     return response
    #request.session['sname']='irfan'
    #request.session['semail']='irfan.sssit@gmail.com'
    #response= HttpResponse(content_type='text/csv')
    #response['Content-Disposition'] = 'attachment; filename="file.csv"'
    #employee = Employee.objects.all()
    #writer = csv.writer(response)
    #for employee in employee:
        #writer.writerow([employee.eid,employee.ename,employee.econtact])
    #writer.writerow(['1001','John','Domil','CA'])
    #writer.writerow(['1002','Amit','Mukhaji','LA','"Testing"'])
    #response.set_cookie('java-tutorial','javatpoint.com')
    #return response
#def getcookie(request):
    #tutorial = request.COOKIES['java-tutorial']
    #return HttpResponse("java tutorials@:"+ tutorial);
    #studentname=request.session['sname']
    #studentemail=request.session['semail']
    #return HttpResponse(studentname+""+studentemail);

    #try:
    #data=Employee.objects.get(id=12)

    #except ObjectDoesNotExist:
        #return HttpResponse("Exception: Data not found")
    #return HttpResponse(data);
    #if request.method == 'POST':
        #form = EmployeeForm(request.POST)
        #student = StudentForm(request.POST,request.FILES)
        #if student.is_valid():
            #handle_uploaded_file(request.FILES['file'])
           # return HttpResponse("Http request:"+request.method)
            #try:
                #return redirect('/')
            #except:
             #   pass
    #else:
       #student = StudentForm()
    #return render(request,"index.html",{'form':student})
   # student = StudentForm()
    #return render(request,"index.html",{'form':student})
   #template=loader.get_template('index..html')#getting our template
   #name={
        #'student':'sai'
   #}
   #return HttpResponse(template.render(name))#rendering the templates in HttpResponse

