from datetime import datetime
class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def mes_cadastro(self):
        meses_do_ano = [
            'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro',
            'outubro', 'novembro', 'dezembro'
        ]
        mes_cad = self.momento_cadastro.month -1
        return meses_do_ano[mes_cad]

    def dia_semana(self):
        dias_da_semana = [
            'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo'
        ]
        sem_cad = self.momento_cadastro.weekday()
        return dias_da_semana[sem_cad]

    def data_formatada(self):
        data_for = self.momento_cadastro.strftime('%d/%m/%Y')
        return data_for

    def hora_formatada(self):
        hora_for = self.momento_cadastro.strftime('%H:%M:%S')
        return hora_for