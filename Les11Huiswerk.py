import pdb

def favoriete_kleur():
    # Print de favoriete kleur
    print("Mijn favoriete kleur is blauw")

def start_debuggen():
    # Gebruik set_trace om de debugger te starten
    pdb.set_trace()
    favoriete_kleur()

if __name__ == "__main__":
    start_debuggen()

