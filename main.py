from TelefonesBr import TelefonesBr
from DatasBr import DatasBr
from AcessoCep import BuscaEndereco
import requests


telefone = '555599900202'

telefones_objeto = TelefonesBr(telefone)

cadastro = DatasBr()
print(cadastro.momento_cadastro)
print('Estamos em uma {}-feira do mês de {}, a data atual é {}, \ne a hora exata é {}, o número de telefone '
      '{} já foi cadastrado \nem seu endereço: '.format(
    cadastro.dia_semana(), cadastro.mes_cadastro(), cadastro.data_formatada(), cadastro.hora_formatada(),
    telefones_objeto)
)

cep = 98300000
objeto_cep = BuscaEndereco(cep)
localidade, uf = objeto_cep.acessa_via_cep()
print(localidade, uf)

print(objeto_cep)

