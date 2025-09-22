from django.shortcuts import render, redirect, get_object_or_404
from .models import Aluno
from .forms import AlunoForm

# Listar alunos
def lista_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'alunos/lista.html', {'alunos': alunos})

# Cadastrar novo aluno
def novo_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_alunos')
        else:
            print("Erros de validação:", form.errors)
    else:
        form = AlunoForm()
    return render(request, 'alunos/form.html', {'form': form})

# Editar aluno
def editar_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    form = AlunoForm(request.POST or None, instance=aluno)
    print("Instância passada ao formulário:", aluno)
    if form.is_valid():
        try:
            form.save()
            return redirect('lista_alunos')
        except Exception as e:
            print("Erro ao salvar aluno editado:", e)
    else:
        print("Erros de validação ao editar:", form.errors)
    return render(request, 'alunos/form.html', {'form': form})

# Detalhes do aluno
def detalhes_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    return render(request, 'alunos/detalhes.html', {'aluno': aluno})

# Remover aluno
def remover_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    if request.method == 'POST':
        aluno.delete()
        return redirect('lista_alunos')
    return render(request, 'alunos/confirma_exclusao.html', {'aluno': aluno})

