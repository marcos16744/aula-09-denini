def senha_segura(senha):
    if len(senha) < 8:
        return False
    tem_maiuscula = any(c.isupper() for c in senha)
    tem_minuscula = any(c.islower() for c in senha)
    tem_numero = any(c.isdigit() for c in senha)
    return tem_maiuscula and tem_minuscula and tem_numero


print(senha_segura("Senha123"))  
print(senha_segura("senha123"))  
