class Relogio:
    def __init__(self, hora, minuto, segundo):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo

    def exibir_horario(self):
        return f"{self.hora:02}:{self.minuto:02}:{self.segundo:02}"
