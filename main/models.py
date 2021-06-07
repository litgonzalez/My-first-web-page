from django.db import models

class Persona(models.Model):
    nombre = models.CharField("Nombre/s", max_length=150)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha_carga = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido)

class Categoria(models.Model):
    nombre = models.CharField(max_length=70, verbose_name='Categoría')
    descripcion = models.TextField("Descripción",null=True, blank=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    codigo = models.CharField(max_length=150, null=True, unique=True, verbose_name='código')
    nombre = models.CharField(max_length=150, verbose_name='Nombre')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)
    disponible = models.BooleanField(default=True)
    fecha_carga = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s - %s' % (self.codigo, self.nombre)

class Orden_compra(models.Model):
    orden = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Persona, on_delete=models.CASCADE)
    producto = models.ManyToManyField(Producto, help_text="Selecciona tus productos manteniendo CTRL presionado")
    metodos = (
        ('DB', 'Débito'),
        ('CR', 'Crédito'),
        ('EF', 'Efectivo')
        )
    metodopago= models.CharField(max_length=50, choices=metodos, verbose_name="Método de pago")

    class Meta:
        verbose_name_plural = "Órdenes de compra"
    
    def __str__(self):
        return '%s - %s' % (self.orden, self.cliente)

class Contacto(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre')
    apellido = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    comentario = models.TextField("Comentario",null=True, blank=True)
    novedades = models.BooleanField(default=True, verbose_name='Me gustaría recibir novedades de 3DHUB')

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido)
