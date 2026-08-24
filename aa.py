import os

def process_data(user_input):
    # Faille de sécurité CRITICAL (Injection de commande)
    os.system("rm -rf " + user_input)
    
    # Mauvaise pratique / Typos (LOW / MEDIUM)
    unused_var = 100
    return True
