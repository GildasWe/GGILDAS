import json
def charger_notes() :
    try :
        with open("NOTES.json","r") as fichier :
            return json.load(fichier)
    except FileNotFoundError :
        return {}
def sauvegarder_notes(NOTES) :
    with open("NOTES.json","w") as fichier :
        json.dump(NOTES,fichier)
def afficher_note(NOTES) :
    # aFFICHAGE PERSONNELLE
    print(NOTES)
    if NOTES :
        Un_etudiant = [etudiant for etudiant in NOTES][0]
        print("_"*(21*(len(NOTES[Un_etudiant])+1)+1))
        p="Nom et Prenoms"
        print(f"|{p:^{20}}",end="|")
        for matiere in NOTES[Un_etudiant].keys() :
            print(f"{matiere:^{20}}",end="|")
        print("\n","_"*(21*(len(NOTES[Un_etudiant])+1)))
        for etudiant, matieres in NOTES.items() :
            print(f"\n|{etudiant:^{20}}",end="|")
            for notes_etudiant in matieres.values() :
                for i in notes_etudiant :
                    print(f"{i:^{4}}",end=" ")
            print(" "*(20-5*len(notes_etudiant)),end="|")
        print("\n","_"*(21*(len(NOTES[Un_etudiant])+1)))    
    else :
        print("Aucune notes ni etudiants, veuillez ajouter pour afficher.")
    # autrement plus vite
    for etudiant,matieres in NOTES.items() :
        print(f"Les notes de {etudiant} :")
        for matiere,notes_etudiant in matieres.items() :
            print(f"{matiere} : {notes_etudiant}")
def ajouter_note(Nom_Etudiant,matiere,note,NOTES):
    if  Nom_Etudiant not in NOTES :
        NOTES[Nom_Etudiant] = {}
    while matiere.strip() not in NOTES[Nom_Etudiant] :
        reponse = input(f"Cette matière n'y est pas pour l'etudiant {Nom_Etudiant}, voulez-vous ajouter cette matière? OUI / NON\n") 
        if reponse.lower() == "oui" :
            NOTES[Nom_Etudiant][matiere] = []
        else :
            print("Opération annulée.")
            return NOTES 
    try :
        note=float(note)
        if note < 0 and note > 20 :
            return "La note doit etre compris entre 0 et 20"
    except ValueError :
        return "La note doit etre un réel."
    NOTES[Nom_Etudiant][matiere].append(note)
    return "Note ajoutée avec succès."
def modifier_note(NOTES) :
    Nom_etudiant = input("Entrez le nom de l'etudiant :")
    if Nom_etudiant.strip() not in NOTES  :
        print("Etudiant non trouvé.")
    else :
        matiere = input("Entrez la matière :")
        if matiere.strip() not in NOTES[Nom_etudiant] :
            print("Matrière non troutrée.")
        else :
            index_note = int(input("Entrez l'indice de la note à modifier (Ex: 1,2,3,...):"))
            if index_note <= len(NOTES[Nom_etudiant][matiere]) :
                nouvelle_note = float(input("Entrez la nouvelle note:"))
                NOTES[Nom_etudiant][matiere][index_note-1] = nouvelle_note
                print("Note modifiée avec succès.")
            else :
                print("Indice invalide.")
    return NOTES
def supprimer_note(NOTES) :
    Nom_etudiant = input("Entrez le nom de l'etudiant:")
    if Nom_etudiant.strip() not in NOTES :
        print("Etudiant introuvable :")
    else :
        matiere = input("Entrez la matière:")
        if matiere.strip() not in NOTES[Nom_etudiant] : 
            print("Matière introuvable.")
        else :
            indice_suppression = int(input("Entrez l'indice de la note à supprimer:"))
            while indice_suppression < 0 or indice_suppression > len(NOTES[Nom_etudiant][matiere]) :
                indice_suppression = int(input("Indice introuvable, ressayez:"))
            NOTES[Nom_etudiant][matiere].pop(indice_suppression - 1)
            print("Note supprimer avec succès.")
    return NOTES
def main() :
    NOTES = charger_notes()
    while True :
        print("\n Options :")
        print(" 1. Ajouter une note \n 2. Afficher les notes \n 3. Modifier une note \n 4. Supprimer une note\n 5. Quitter")
        choix = input("Entrez votre choix:")
        if choix.strip() == "1" :
            Nom_Etudiant=input("Entrez le nom de l'etudiant:")
            while not Nom_Etudiant :
                Nom_Etudiant=input("Vous n'avez rien entré, veuillez ressayer:")
            matiere = input("Entrez la matiere:")
            note = float(input("Entrez la note :"))
            resultat = ajouter_note(Nom_Etudiant,matiere,note,NOTES)
            print(resultat)
        elif choix.strip() == "2" :
            afficher_note(NOTES)
        elif choix.strip() == "3" :
            NOTES = modifier_note(NOTES)
            sauvegarder_notes(NOTES)
        elif choix.strip() == "4" :
            NOTES = supprimer_note(NOTES)
            sauvegarder_notes(NOTES)
        elif choix.strip() == "5" :
            sauvegarder_notes(NOTES)
            break
        else :
            print("Choix invalide, veuillez ressayer.")
if __name__ == "__main__" :
    main()