from movimentation.models import Movimentation_type

MOVIMENTATION_STATUS_MAP = {
    'EM_ESTOQUE' : 'ENTRADA',
    'ATIVO' : 'SAIDA',
    'EM_TRANFERENCIA' : 'SAIDA'
}


STATUS_TO_MOV_CODE = {
    'Em estoque': 'ENTRADA',
    'Ativo': 'SAIDA',
    'Transferido': 'SAIDA',
}




mov_types = {
    mt.code: mt
    for mt in Movimentation_type.objects.all()
}
        

print(mov_types.keys())