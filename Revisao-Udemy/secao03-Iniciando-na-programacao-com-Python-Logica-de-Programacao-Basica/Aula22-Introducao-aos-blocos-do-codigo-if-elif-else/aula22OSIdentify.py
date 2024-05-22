import platform

# Obter o nome do sistema operacional
os_name = platform.system()
print(f"Sistema Operacional: {os_name}")

# Obter a versão do sistema operacional
os_version = platform.version()
print(f"Versão do Sistema Operacional: {os_version}")

# Obter detalhes adicionais sobre o sistema operacional
os_details = platform.platform()
print(f"Detalhes do Sistema Operacional: {os_details}")
