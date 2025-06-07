# Executar
# powershell -ExecutionPolicy Bypass -File .\setup.ps1

# Caminho do ambiente virtual
$envDir = "env"

# Verifica se Python está instalado
if (!(Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "Python não está instalado. Por favor, instale o Python primeiro." -ForegroundColor Red
    exit 1
}

# Cria o ambiente virtual, se ainda não existir
if (!(Test-Path $envDir)) {
    Write-Host "Criando ambiente virtual em '$envDir' ..." -ForegroundColor Cyan
    python -m venv $envDir
} else {
    Write-Host "Ambiente virtual '$envDir' já existe." -ForegroundColor Yellow
}

# Caminhos internos do venv
$venvPython = Join-Path $envDir "Scripts\python.exe"
$venvPip = Join-Path $envDir "Scripts\pip.exe"
$venvBin = Join-Path $envDir "Scripts"

# Instala o Poetry dentro do ambiente virtual
Write-Host "Instalando Poetry no ambiente virtual..." -ForegroundColor Cyan
& $venvPip install poetry

# Adiciona o Scripts do venv ao PATH para acessar poetry
$env:PATH = "$venvBin;$env:PATH"

# Verifica se poetry foi instalado com sucesso
if (!(Get-Command poetry -ErrorAction SilentlyContinue)) {
    Write-Host "Poetry não foi encontrado mesmo após a instalação." -ForegroundColor Red
    exit 1
}

# Verifica se pyproject.toml existe
if (!(Test-Path "./pyproject.toml")) {
    Write-Host "Nenhum pyproject.toml encontrado no diretório atual. Não é possível executar 'poetry install'." -ForegroundColor Red
    exit 1
}

# Executa poetry install
Write-Host "Executando 'poetry install'..." -ForegroundColor Cyan
poetry install

# Mensagem final
Write-Host "`nAmbiente 'env' configurado com sucesso!" -ForegroundColor Green
Write-Host "Para ativá-lo manualmente, execute:" -ForegroundColor Yellow
Write-Host "`tenv\Scripts\Activate.ps1"
