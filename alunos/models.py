from django.db import models

class Aluno(models.Model):
    # Informações Pessoais
    nome_completo = models.CharField(max_length=150)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=14, unique=True)   # 000.000.000-00
    rg = models.CharField(max_length=20, unique=True)
    
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)

    # Informações de Contato
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    telefone_emergencia = models.CharField(max_length=15, blank=True, null=True)  # Opcional

    # Endereço
    cep = models.CharField(max_length=9)  # formato 00000-000
    endereco = models.CharField(max_length=200)  # Rua, Avenida, etc
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100, blank=True, null=True)  # Opcional
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    
    UF_CHOICES = [
        ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'),
        ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'),
        ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins'),
    ]
    uf = models.CharField(max_length=2, choices=UF_CHOICES)

    # Informações Acadêmicas
    numero_matricula = models.CharField(max_length=20, unique=True)
    curso = models.CharField(max_length=100)
    serie_ano = models.CharField(max_length=20)

    TURNO_CHOICES = [
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno'),
    ]
    turno = models.CharField(max_length=1, choices=TURNO_CHOICES)

    # Observações
    observacoes = models.TextField(blank=True, null=True)  # Opcional

    def __str__(self):
        return f"{self.nome_completo} ({self.numero_matricula})"
