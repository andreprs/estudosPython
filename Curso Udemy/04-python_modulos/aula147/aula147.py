import subprocess

# Windows - ping 127.0.0.1

proc = subprocess.run(['ping', '127.0.0.1'], capture_output=True, text=True)
print(proc.stderr)  # eventual erro que pode retornar
print(proc.stdout)  # saída do comando em si
print(proc.returncode)  # retorno do processo (em caso de sucesso retorna 0)
print(proc.args)  # argumentos que foram passados
