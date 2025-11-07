# ==================== views.py ====================
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Cliente
from .forms import ClienteForm

@login_required(login_url='login')
def listar_clientes(request):
    clientes = Cliente.objects.filter(ativo=True)
    return render(request, 'clientes/listar.html', {'clientes': clientes})

@login_required(login_url='login')
def criar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Cliente cadastrado com sucesso!')
                return redirect('listar_clientes')
            except Exception as e:
                messages.error(request, f'Erro ao cadastrar cliente: {str(e)}')
    else:
        form = ClienteForm()

    return render(request, 'clientes/form.html', {
        'form': form,
        'titulo': 'Novo Cliente'
    })

@login_required(login_url='login')
def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Cliente atualizado com sucesso!')
                return redirect('listar_clientes')
            except Exception as e:
                messages.error(request, f'Erro ao atualizar cliente: {str(e)}')
    else:
        form = ClienteForm(instance=cliente)

    return render(request, 'clientes/form.html', {
        'form': form,
        'titulo': 'Editar Cliente'
    })

@login_required(login_url='login')
def deletar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    cliente.ativo = False
    cliente.save()
    messages.success(request, f'Cliente {cliente.nome} removido com sucesso!')
    return redirect('listar_clientes')

@login_required(login_url='login')
def visualizar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'clientes/visualizar.html', {'cliente': cliente})
