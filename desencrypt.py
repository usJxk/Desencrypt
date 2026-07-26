from cryptography.fernet import Fernet
import os
import json

# Variables de configuración
file_to_encrypt = "keyText.txt"
file_json_report = "reporte.json"

# Generar la llave
key = Fernet.generate_key()
f = Fernet(key)

# Crear el archivo
if os.path.exists(file_to_encrypt):
    print(f"[!] El archivo {file_to_encrypt} ya existe.")
else:
    try:
        with open(file_to_encrypt, "w", encoding="utf-8") as file:
            file.write("Hola mundo")
        print(f"[!] El archivo {file_to_encrypt} ha sido creado.")
    except Exception as e:
        print(f"[!] El archivo no pudo ser creado: {e}")

# Lee el archivo
with open(file_to_encrypt, "rb") as file:
    message_content = file.read()

# Encriptar el contenido
encrypted_content = f.encrypt(message_content)

# Estructurar todos los datos
data = [{
    'FILE_NAME': file_to_encrypt,
    'ORIGINAL_CONTENT': message_content.decode('utf-8'),
    'ENCRYPTED_CONTENT': encrypted_content.decode('utf-8'),
    'SECRET_KEY': key.decode('utf-8')
}]

with open(file_json_report, "w", encoding="utf-8") as fp:
    json.dump(data, fp, indent=4)
print(f"[!] Datos guardados con éxito en {file_json_report}")

# Se elimina el archivo original
if os.path.exists(file_to_encrypt):
    os.remove(file_to_encrypt)
    print(f"[!] El archivo {file_to_encrypt} ha sido eliminado.")

# Desencriptacion
try:
    decrypted_bytes = f.decrypt(encrypted_content)
    print(f"[+] Archivo desencriptado con éxito. Contenido: {decrypted_bytes.decode('utf-8')}")
except Exception as e:
    print(f"[!] El archivo no fue desencriptado: {e}")
