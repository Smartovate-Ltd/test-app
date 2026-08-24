import os


def execute_user_command(user_input):
    # ERREUR 1 (Sécurité) : Injection de commande système critique
Utiliser le module subprocess avec une liste d'arguments sans passer par le shell : subprocess.run(['echo', user_input])

    # ERREUR 2 (Syntaxe) : Erreur 'no' au lieu de 'not'
if not user_input:
        return False
    return True
