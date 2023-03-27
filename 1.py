def ruleaza_dfa(dfa, input_string):
    stare_curenta = dfa['stare_initiala']
    for simbol in input_string:
        if simbol not in dfa['alfabet']:
            return False
        stare_curenta = dfa['tranzitii'].get((stare_curenta, simbol), None)
        if stare_curenta is None:
            return False
    return stare_curenta in dfa['stari_finale']


def citire_fisier(nume_fisier):
    dfa = {}
    with open(nume_fisier, 'r') as f:
        tranzitii = {}
        stari_finale = set()
        linii = f.readlines()
        for linie in linii:
            parti = linie.strip().split()
            if len(parti) == 3:
                stare, simbol, stare_urmatoare = parti
                tranzitii[(stare, simbol)] = stare_urmatoare
            elif linie == linii[-1]:
                for parte in parti:
                    stari_finale.add(parte)
            else:
                print(f"Linii ignorate: {linie.strip()}")

        alfabet = set()
        stari = set()
        for (stare, simbol) in tranzitii:
            alfabet.add(simbol)
            stari.add(stare)
            stari.add(tranzitii[(stare, simbol)])
        stare_initiala = "q" + min([x[1] for x in stari])
        dfa['alfabet'] = alfabet
        dfa['stari'] = stari
        dfa['stare_initiala'] = stare_initiala
        dfa['stari_finale'] = stari_finale
        dfa['tranzitii'] = tranzitii
    return dfa


dfa = citire_fisier('Test1.txt')
input_string = input("Input: ")

if ruleaza_dfa(dfa, input_string):
    print("Acceptat")
else:
    print("Respins")
