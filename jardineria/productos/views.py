from django.shortcuts import render, redirect
from .models import Producto,Boleta, detalle_boleta
from .forms import ProductoForm,RegistroUserForm,ContactoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from productos.compra import Carrito

# Create your views here.
def index(request):
    return render(request, 'index.html')

def somos(request):
    return render(request, 'somos.html')
def galeria(request):
    return render(request, 'galeria.html')
def contacto(request):
    return render(request, 'contacto.html')            

@login_required
def otra(request):
    plantas = Producto.objects.raw('Select * from productos_producto')
    datos={
        'productos':plantas
    }
    return render(request, 'otra.html', datos)




    '''
    autitos = Vehiculo.objects.all()    #similar al select * from Vehiculo
    datos ={
        'vehiculos':autitos
    }
    return render(request, 'otra.html', datos)
    '''
@login_required
def crear(request):
    if request.method=="POST":
        productoform=ProductoForm(request.POST,request.FILES)
        if productoform.is_valid():
            productoform.save()     #similar al insert en función
            return redirect ('otra')
    else:
        productoform=ProductoForm()
    return render (request, 'crear.html', {'productoform': productoform})






@login_required
def eliminar(request, id): 
    productoEliminado = Producto.objects.get(nombre=id) #similar a select * from... where...
    productoEliminado.delete()
    return redirect ('otra')



@login_required
def modificar(request, id): 
    productoModificado=Producto.objects.get(nombre=id) #buscamos el objeto
    datos ={
        'form':ProductoForm(instance=productoModificado)
    }
    if request.method=="POST":
        formulario = ProductoForm(data=request.POST, instance=productoModificado)
        if formulario.is_valid():
            formulario.save()
            return redirect ('otra')
    return render(request, 'modificar.html', datos)



def registrar(request):
    data = {
        'form' : RegistroUserForm()
    }
    if request.method=="POST":
        formulario = RegistroUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], 
                                password = formulario.cleaned_data["password1"])
            login(request, user)
            return redirect ('index')
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)


def mostrar(request):
    plantas = Producto.objects.all()
    datos={
        'plantas': plantas
    }
    return render(request, 'mostrar.html', datos)








def tienda(request):
    plantas = Producto.objects.all()
    datos={
        'plantas':plantas
    }
    return render(request, 'tienda.html', datos)


def agregar_producto(request,id):
    carrito_compra= Carrito(request)
    producto = Producto.objects.get(nombre=id)
    carrito_compra.agregar(producto=producto)
    return redirect('tienda')

def eliminar_producto(request, id):
    carrito_compra= Carrito(request)
    producto = Producto.objects.get(nombre=id)
    carrito_compra.eliminar(producto=producto)
    return redirect('tienda')

def restar_producto(request, id):
    carrito_compra= Carrito(request)
    producto = Producto.objects.get(nombre=id)
    carrito_compra.restar(producto=producto)
    return redirect('tienda')

def limpiar_carrito(request):
    carrito_compra= Carrito(request)
    carrito_compra.limpiar()
    return redirect('tienda')    


def generarBoleta(request):
    precio_total=0
    for key, value in request.session['carrito'].items():
        precio_total = precio_total + int(value['precio']) * int(value['cantidad'])
    boleta = Boleta(total = precio_total)
    boleta.save()
    productos = []
    for key, value in request.session['carrito'].items():
            producto = Producto.objects.get(nombre = value['producto_id'])
            cant = value['cantidad']
            subtotal = cant * int(value['precio'])
            detalle = detalle_boleta(id_boleta = boleta, id_producto = producto, cantidad = cant, subtotal = subtotal)
            detalle.save()
            productos.append(detalle)
    datos={
        'productos':productos,
        'fecha':boleta.fechaCompra,
        'total': boleta.total
    }
    request.session['boleta'] = boleta.id_boleta
    carrito = Carrito(request)
    carrito.limpiar()
    return render(request, 'detallecarrito.html',datos)



    


