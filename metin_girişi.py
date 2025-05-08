from Main3 import execute_command

def get_query():
    result = execute_command()  # Ses veya metin girişini alır
    print(f"Alınan komut: {result}")
    return result
