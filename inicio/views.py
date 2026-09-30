from django.shortcuts import render

# Create your views here.
def index(request):
    productos =[
        {"codigo":1, "nombre":"producto 1", "descripción":"Descripción Producto 1","stock":"10","precio":"$1.000.-"},
        {"codigo":2, "nombre":"producto 2", "descripción":"Descripción Producto 2","stock":"20","precio":"$2.000.-"},
        {"codigo":3, "nombre":"producto 3", "descripción":"Descripción Producto 3","stock":"30","precio":"$3.000.-"},
        {"codigo":4, "nombre":"producto 4", "descripción":"Descripción Producto 4","stock":"40","precio":"$4.000.-"},
    ]
    return render(request, 'inicio/default.html',{"articulos":productos})