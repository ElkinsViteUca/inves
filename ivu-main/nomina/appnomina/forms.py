from django import forms 
from .models import Cargo, Departamento, Empleado

#formularios
class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = ['descripcion','estado']
        widgets = {
            'descripcion':forms.TextInput(attrs={
                'placeholder':'Ingrese cargo',
                'class':'form-group',
                'required':True
            }),            
        }
        
class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['descripcion' , 'estado']
        widgets = {
            'descripcion':forms.TextInput(attrs={
                'placeholder':'Ingrese Departamento',
                'class':'form-group',
                'required':True
            }), 
        }
    
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['id' , 'nombre', 'cedula','cargo','departamento', 'sueldo', 'estado']
        widgets = {
            
            'nombre':forms.TextInput(attrs={
                'placeholder':'Ingrese Empleado',
                'class':'form-group',
                'type' : 'text', 
                'required':True
            }),            
             'cedula':forms.TextInput(attrs={
                'placeholder':'Escriba su cedula',
                'class':'form-group',
                
                'required':True
            }),

             'cargo':forms.Select(attrs={
                'placeholder':'Elija el Cargo',
                'class':'form-group',
                'required':True
            }),            
             
              'departamento':forms.Select(attrs={
                'placeholder':'Ingrese Departamento',
                'class':'form-group',
                'required':True
            }),            
            
            'sueldo':forms.TextInput(attrs={
                'placeholder':'Ingrese Sueldo',
                'class':'form-group',
                'type' : 'number',
                'required':True
            }),
        }