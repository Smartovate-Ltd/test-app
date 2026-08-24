import os


def execute_user_command(user_input):
    # ERREUR 1 (Sécurité) : Injection de commande système critique
    os.system("echo " + user_input)

    # ERREUR 2 (Syntaxe) : Erreur 'no' au lieu de 'not'
    if no user_input:
        return False
    return True
