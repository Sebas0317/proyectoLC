from django.contrib import admin
from .models import GastosEnvio,Cupon

@admin.register(GastosEnvio)
class GastosEnvioAdmin(admin.ModelAdmin):
    list_display = ('monto',)  # Campo que se mostrará en la lista de registros

class CuponAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descuento')
    
admin.site.register(Cupon, CuponAdmin)  

# <div class="coupon">
#                     <form method="post">
#                         {% csrf_token %}
#                         <input type="text" name="cupon_codigo" placeholder="Coupon Code" />
#                         <button type="submit">Aplicar código</button>
#                     </form>
#                 </div>