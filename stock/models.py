from django.db import models
from invoice.models import Invoice_item


# Create your models here.
class Item_category(models.Model):
    category_name = models.CharField(
        max_length=25,
        unique=True,
        verbose_name='Categoria',
    )
    class Meta:
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.category_name


class Equipament_type(models.Model):
    equipament_type = models.CharField(
        max_length=25,
        unique=True,
        verbose_name='Tipo do equipamento'
    )
    class Meta:
        verbose_name_plural = 'Tipos de equipamento'

    def __str__(self):
        return self.equipament_type


class Status_item(models.Model):
    status_name = models.CharField(
        max_length=25, 
        unique=True,
        verbose_name='Status'
    )

    class Meta:
        verbose_name_plural = 'Tipos de status'

    

    def __str__(self):
        return self.status_name



class Locals(models.Model):
    local_name = models.CharField(max_length=20, unique=True)


    class Meta:
        verbose_name= 'Localidade'
        verbose_name_plural = 'Localidades'
    
    def __str__(self):
        return self.local_name


class Stock(models.Model):
  

    custom_id = models.CharField(max_length=10, unique=True, null=True, blank=True )
    
    
    item = models.ForeignKey(
        Invoice_item,
        on_delete=models.PROTECT,
        related_name='item_nota',
        verbose_name='Item da nota',
    )



    category = models.ForeignKey(
        Item_category,
        on_delete=models.PROTECT,
        related_name='item_category',
        null=True,
        blank=True,
        verbose_name='Categoria'
    )
    status = models.ForeignKey(
        Status_item,
        on_delete=models.PROTECT,
        related_name='status_item',
        verbose_name='Status do item'
    )
    item_type = models.ForeignKey(
        Equipament_type,
        on_delete=models.PROTECT,
        related_name='equipament',
        verbose_name='Tipo de equipamento'

    )
    local = models.ForeignKey(
        Locals,
        on_delete=models.PROTECT,
        verbose_name='Localidade'
    )

    serial_number = models.CharField(
        max_length=40,
        unique=True,
        verbose_name='Número de série'
    )
    property_number = models.CharField(
        max_length=40,
        unique=True,
        null=True,
        blank=True,
        verbose_name='Patrimônio'
    )

    request_unit = models.CharField(
        max_length=10,
        default='703',
        blank=True,
        null=True,
        verbose_name='Unidade solicitante',
    )

    pay_unit = models.CharField(
        max_length=10,
        null=True,
        blank=True, 
        verbose_name='Unidade pagante'
    )

    warranty = models.DateField(
        null=True,
        blank=True,
        verbose_name='Garantia'

    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criado em'
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Atualizaddo em'
    )

    class Meta:
        verbose_name ='Estoque'
        verbose_name_plural = 'Estoque'


    def __str__(self):
        return str(self.serial_number)



    def save(self, **kwargs):
        PREFIX_TAGS = {
            "Notebook avançado":"NTAV-",
            "Notebook office":"NTOFF-",
            "Telefone":"TEL-",
            "Headset":"HDSET-",
            "Chip":"CHP-",
            "Periferico":"PER-"
        }
        category = self.category
        item = self.item

        is_new_item = self.pk is None
        super().save(**kwargs)

        if is_new_item:
            print("Entrei em novo item")
            print("Categoria:", category.category_name)
            if category.category_name == "Computador":
               print("Entrei no if da categoria")
               nomalized_name = str(item.name_item)
               nomalized_name = nomalized_name.strip()
               print("Nomalized:", nomalized_name)
               print("Nome do item entrando:", item.name_item)
               prefix = PREFIX_TAGS.get(nomalized_name, "ERR-")
               print("Prefixo obtido: ", prefix)
            else:
                prefix = PREFIX_TAGS.get(category.category_name, "CATERR-")
            
            self.custom_id = f"{prefix}{self.id}"
        

            return super().save(update_fields=["custom_id"])
        return super().save(**kwargs)
        


