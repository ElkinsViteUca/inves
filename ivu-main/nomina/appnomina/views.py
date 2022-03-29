from urllib.request import Request
from django.shortcuts import redirect, render,HttpResponse
from appnomina.forms import CargoForm, DepartamentoForm, EmpleadoForm
#importamos el modelo
from .models import Cargo, Departamento, Empleado
# Create your views here.
def inicio(request):
    #return HttpResponse("<h1>Bienvenido a mi Sitio Web</h1>")
    return render(request, "inicio.html")
# def cargo(request):
# #     #return HttpResponse("<h1>Mantenimiento De Cargos...</h1>")
#     return render(request,"pages/cargo.html")
# def departamento(request):
# #     #return HttpResponse("<h1>Mantenimiento De departamentos</h1>")
#     return render(request,"pages/departamento.html")
def empleado(request):
#     #return HttpResponse("<h1>Mantenimiento De Empleados</h1>")
    return render(request,"pages/empleado.html")
#Creacion de la vista para crear cargo

def crearDepartamento(request):
    if request.method == "POST":
        print("entro por post")
        #instancio un objeto de tipo formulario cargo
        departamento_form = DepartamentoForm(request.POST)
        #verifico si los datos son validos
        if departamento_form.is_valid():
            #guardo el cargo
            departamento_form.save()
    else: 
        print("entro por get")  
        #instancio un objeto de tipo cargo
    # traigo todos los cargos
    departamento_form = DepartamentoForm()
    departamentos = Departamento.objects.all()
    return render(request, "pages/departamento.html", {'departamentoForm': departamento_form, 'departamentos':departamentos, 'accion':'Crear'})
    
def editarDepartamento(request,id):
    #verifico que los datos no esten vacios
    error,departamento_form=None,None
    try:
        #traigo el objeto cargo con el id asociado
        departamento = Departamento.objects.get(id=id)
        if request.method == "GET":
           departamento_form = DepartamentoForm(instance=departamento) 
        else:
           departamento_form = DepartamentoForm(request.POST,instance=departamento)
           if departamento_form.is_valid():
                #aqui guardo los cambios que se han modificado
                departamento_form.save()
                #recarga o actualiza nuevamente la pagina
                return redirect('departamento') 
    except Exception as e:
        error=e 
    # traigo todos los cargos
    #cargo_form = CargoForm()
    departamentos = Departamento.objects.all()
    return render(request, "pages/departamento.html", {'departamentoForm': departamento_form, 'departamentos':departamentos, 'accion':'Actualizar'})
#vista para eliminar
def eliminarDepartamento(request,id):
    #traigo el objeto cargo con el id asociado
    departamento = Departamento.objects.get(id=id)
    if request.method == 'POST':
        # eliminacion fisica del registro
        departamento.delete()    
        #refresca o actualiza el formulario cargo
        return redirect("departamento")
    return render(request,'pages/eliminar_departamento.html',{'departamento':departamento})      

#vista para modificar

def crearCargo(request):
    if request.method == "POST":
        print("entro por post")
        #instancio un objeto de tipo formulario cargo
        cargo_form = CargoForm(request.POST)
        #verifico si los datos son validos
        if cargo_form.is_valid():
            #guardo el cargo
            cargo_form.save()
    else: 
        print("entro por get")  
        #instancio un objeto de tipo cargo
    # traigo todos los cargos
    cargo_form = CargoForm()
    cargos = Cargo.objects.all()
    return render(request, "pages/cargo.html", {'cargoForm': cargo_form, 'cargos':cargos, 'accion':'Crear'})
    
#vista para modificar
def editarCargo(request,id):
    #verifico que los datos no esten vacios
    error,cargo_form=None,None
    try:
        #traigo el objeto cargo con el id asociado
        cargo = Cargo.objects.get(id=id)
        if request.method == "GET":
           cargo_form = CargoForm(instance=cargo) 
        else:
           cargo_form = CargoForm(request.POST,instance=cargo)
           if cargo_form.is_valid():
                #aqui guardo los cambios que se han modificado
                cargo_form.save()
                #recarga o actualiza nuevamente la pagina
                return redirect('cargo') 
    except Exception as e:
        error=e 
    # traigo todos los cargos
    #cargo_form = CargoForm()
    cargos = Cargo.objects.all()
    return render(request, "pages/cargo.html", {'cargoForm': cargo_form, 'cargos':cargos, 'accion':'Actualizar'})
#vista para eliminar
def eliminarCargo(request,id):
    #traigo el objeto cargo con el id asociado
    cargo = Cargo.objects.get(id=id)
    if request.method == 'POST':
        # eliminacion fisica del registro
        cargo.delete()    
        #refresca o actualiza el formulario cargo
        return redirect("cargo")
    return render(request,'pages/eliminar_cargo.html',{'cargo':cargo})  

#Empleado
def crearEmpleado(request):
    if request.method == "POST":
        print("entro por post")
        #instancio un objeto de tipo formulario cargo
        empleado_form = EmpleadoForm(request.POST)
        #verifico si los datos son validos
        if empleado_form.is_valid():
            #guardo el cargo
            empleado_form.save()
    else: 
        print("entro por get")  
        #instancio un objeto de tipo cargo
    # traigo todos los cargos
    empleado_form = EmpleadoForm()
    empleados = Empleado.objects.all()
    return render(request, "pages/empleado.html", {'empleadoForm': empleado_form, 'empleados':empleados, 'accion':'Crear'})
    
#vista para modificar
def editarEmpleado(request,id):
    #verifico que los datos no esten vacios
    error,empleado_form=None,None
    try:
        #traigo el objeto empleado con el id asociado
        empleado = Empleado.objects.get(id=id)
        if request.method == "GET":
           empleado_form = EmpleadoForm(instance=empleado) 
        else:
           empleado_form = EmpleadoForm(request.POST,instance=empleado)
           if empleado_form.is_valid():
                #aqui guardo los cambios que se han modificado
                empleado_form.save()
                #recarga o actualiza nuevamente la pagina
                return redirect('empleado') 
    except Exception as e:
        error=e 
    # traigo todos los empleados
    #cargo_form = CargoForm()
    empleados = Empleado.objects.all()
    return render(request, "pages/empleado.html", {'empleadoForm': empleado_form, 'empleados':empleados, 'accion':'Actualizar'})
#vista para eliminar
def eliminarEmpleado(request,id):
    #traigo el objeto cargo con el id asociado
    empleado = Empleado.objects.get(id=id)
    if request.method == 'POST':
        # eliminacion fisica del registro
        empleado.delete()    
        #refresca o actualiza el formulario cargo
        return redirect("empleado")
    return render(request,'pages/eliminar_empleado.html',{'empleado':empleado})  




