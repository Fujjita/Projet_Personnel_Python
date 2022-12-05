import random
import tkinter as tk
#-------------------------------------------------------------------------------
root = tk.Tk()
root.geometry("1200x900")
root.title("Projet Personnel")
#-------------------------------------------------------------------------------
class quest :
    def __init__(self, ques, rep, diffi, num, act):
        self.ques = ques
        self.rep = rep
        self.diffi = diffi
        self.num = num
        self.act = act
#-------------------------------------------------------------------------------
def addval() :
    nom = len(questions)
    add1 = ques.get()
    add2 = repo.get()
    add3 = diff.get()
    add4 = nom + 1
    add4 = int(add4)
    add5 = "oui"
    add = quest(add1, add2, add3, add4, add5)
    questions.append(add)
    ques.set("")
    repo.set("")
    diff.set("")
    frm1.destroy()
    frm2.destroy()
    frm5.destroy()
    menuques()
#-------------------------------------------------------------------------------
def modval() :
    temp = quest("","","","","")
    mod4 = nume.get()
    mod4 = int(mod4)
    mod4 = mod4 - 1
    add1 = ques.get()
    add2 = repo.get()
    add3 = diff.get()
    add4 = mod4 + 1
    temp.act = questions[mod4].act
    questions[mod4] = quest(add1, add2, add3, add4, temp.act)
    frm1.destroy()
    frm2.destroy()
    frm5.destroy()
    menuques()
#-------------------------------------------------------------------------------
def act() :
    temp = quest("","","","","")
    mod4 = nume.get()
    mod4 = int(mod4)
    mod4 = mod4 - 1
    temp.act = questions[mod4].act
    if temp.act == "oui" :
        add5 = "non"
        add4 = mod4 + 1
        questions[mod4].num = add4
        questions[mod4].act = add5
        menuques()
    elif temp.act == "non" :
        add5 = "oui"
        add4 = mod4 + 1
        questions[mod4].num = add4
        questions[mod4].act = add5
        menuques()
#-------------------------------------------------------------------------------
def sup() :
    supr = nume.get()
    supr = int(supr)
    supr = supr - 1
    questions.pop(supr)
    for x in questions :
        if x.num > supr :
            x.num = x.num - 1
        else :
            continue
    menuques()
#-------------------------------------------------------------------------------
def correct() :
    cor = int(q)
    cor = cor - 1
    print(cor)
    if rep.get() == questions[cor].rep :
        reponses.append("1")
        mvreponses.append("na")
    else :
        reponses.append("0")
        mvreponses.append(rep)

#-------------------------------------------------------------------------------
def ref() :
    btn15.destroy()
    lbl0.destroy()
    frm0.destroy()

    lbl19 = tk.Label(root, text="MARTINEZ, Sébastien. La Méthode Martinez, (réf. du 30 octobre 2022), La Méthode Martinez [en ligne], adresse URL : https://www.sebastien-martinez.com/guide-etudiant/comment-etudier-efficacement/")
    lbl19.pack()

    global btn16
    btn16 = tk.Button(root, text="Menu Principal", command=menuprinc)
    btn16.pack()
#-------------------------------------------------------------------------------
def o() :
    global o
    o = 0
    menuprinc()
#-------------------------------------------------------------------------------
def menuprinc() :

    btn0.destroy()
    lbl1.destroy()
    frm1.destroy()
    lbl19.destroy()
    btn16.destroy()

    global lbl0
    lbl0 = tk.Label(root, text="Projet Personnel\nJonathan Dubois 2022-2023", font=('Times', 20))
    lbl0.pack(padx=10, pady=10)

    global frm0
    frm0 = tk.Frame(root)
    frm0.columnconfigure(0, weight=1)

    btn1 = tk.Button(frm0, text="Créer vos questions", font=('Times', 16), command=menuques)
    btn1.grid(row=0, column=0)

    btn2 = tk.Button(frm0, text="Étudier", font=('Times', 16), command=study)
    btn2.grid(row=0, column=1)

    btn3 = tk.Button(frm0, text="Quitter", font=('Times', 16), command=exit)
    btn3.grid(row=0, column=2)

    global btn15
    btn15 = tk.Button(root, text="Références", command=ref)
    btn15.place(x=0, y=0)

    frm0.pack()
#-------------------------------------------------------------------------------
def menuques() :

    global o
    if o == 0 :
        global lbl
        lbl = tk.Label(root, text="", font=('Times', 20))
        lbl.pack(padx=10, pady=10)
    else :
        pass
    o += 1

    lbl0.destroy()
    frm0.destroy()
    lbl.destroy()
    btn15.destroy()

    global lbl1
    lbl1 = tk.Label(root, text="Questions :", font=('Times', 20))
    lbl1.pack(padx=10, pady=10)

    n = len(questions)
    for i in range(n):
        lbl = tk.Label(root, text=f"{questions[i].num}.  Question : {questions[i].ques}  Réponse : {questions[i].rep}  Difficulté : {questions[i].diffi}  Activée :  {questions[i].act}", font=('Times', 16))
        lbl.pack(padx=10, pady=10)
        i += 1

    global frm1
    frm1 = tk.Frame(root)
    frm1.columnconfigure(0, weight=1)

    btn4 = tk.Button(frm1, text="Ajouter une question", font=('Times', 16), command=addquestion)
    btn4.grid(row=0, column=0)

    btn5 = tk.Button(frm1, text="Modifier une question", font=('Times', 16), command=modquestion)
    btn5.grid(row=0, column=1)

    btn6 = tk.Button(frm1, text="Supprimer une question", font=('Times', 16), command=suprquestion)
    btn6.grid(row=0, column=2)

    btn7 = tk.Button(frm1, text="Menu principal", font=('Times', 16), command=menuprinc)
    btn7.grid(row=0, column=3)

    frm1.pack()

#-------------------------------------------------------------------------------
def addquestion() :

    lbl1.destroy()
    frm1.destroy()
    btn15.destroy()

    global frm2
    frm2 = tk.Frame(root)
    frm2.columnconfigure(0, weight=1)

    lbl2 = tk.Label(frm2, text = "Question", font=('Times', 16))
    lbl2.grid(row=0, column=0)
    ent0 = tk.Entry(frm2, textvariable = ques, font=('Times', 16))
    ent0.grid(row=0, column=1)

    lbl3 = tk.Label(frm2, text = "Réponse", font=('Times', 16))
    lbl3.grid(row=0, column=2)
    ent1 = tk.Entry(frm2, textvariable = repo, font=('Times', 16))
    ent1.grid(row=0, column=3)

    frm2.pack()

    global frm5
    frm5 = tk.Frame(root)
    frm5.columnconfigure(0, weight=1)

    lbl4 = tk.Label(frm5, text = "Difficulté (Facile, Moyen, Difficile)", font=('Times', 16))
    lbl4.grid(row=0, column=0)

    ent2 = tk.Entry(frm5, textvariable = diff, font=('Times', 16))
    ent2.grid(row=0, column=1)

    btn11 = tk.Button(frm5, text="Entrer", font=('Times', 16), command=addval)
    btn11.grid(row=1, column=0, sticky=tk.E)

    frm5.pack()

    global lbl
    lbl.destroy()
#-------------------------------------------------------------------------------
def modquestion() :

    lbl1.destroy()
    frm1.destroy()

    global frm3
    frm3 = tk.Frame(root)
    frm3.columnconfigure(0, weight=1)

    lbl5 = tk.Label(frm3, text = "Quelle question voulez-vous modifier ?", font=('Times', 16))
    lbl5.grid(row=0, column=0)
    ent3 = tk.Entry(frm3, textvariable = nume, font=('Times', 16))
    ent3.grid(row=0, column=1)

    frm3.pack()

    global frm4
    frm4 = tk.Frame(root)
    frm4.columnconfigure(0, weight=1)

    lbl6 = tk.Label(frm4, text = "Question", font=('Times', 16))
    lbl6.grid(row=0, column=0)
    ent4 = tk.Entry(frm4, textvariable = ques, font=('Times', 16))
    ent4.grid(row=0, column=1)

    lbl7 = tk.Label(frm4, text = "Réponse", font=('Times', 16))
    lbl7.grid(row=0, column=2)
    ent5 = tk.Entry(frm4, textvariable = repo, font=('Times', 16))
    ent5.grid(row=0, column=3)

    frm4.pack()

    global lbl8
    lbl8 = tk.Label(root, text = "Difficulté (Facile, Moyen, Difficile)", font=('Times', 16))
    lbl8.pack()
    global ent6
    ent6 = tk.Entry(root, textvariable = diff, font=('Times', 16))
    ent6.pack()

    global btn11
    btn11 = tk.Button(root, text="Entrer", font=('Times', 16), command=modval)
    btn11.pack(padx=10, pady=10)

    global btn12
    btn12 = tk.Button(root, text="Activer/Désactiver", font=('Times', 16), command=act)
    btn12.pack(padx=10, pady=10)
#-------------------------------------------------------------------------------
def suprquestion() :

    lbl1.destroy()
    frm1.destroy()

    global frm6
    frm6 = tk.Frame(root)
    frm6.columnconfigure(0, weight=1)

    lbl9 = tk.Label(frm6, text = "Quelle question voulez-vous supprimer ?", font=('Times', 16))
    lbl9.grid(row=0, column=0)
    ent7 = tk.Entry(frm6, textvariable = nume, font=('Times', 16))
    ent7.grid(row=0, column=1)

    frm6.pack()

    btn13 = tk.Button(root, text="Supprimer", font=('Times', 16), command=sup)
    btn13.pack(padx=10, pady=10)
#-------------------------------------------------------------------------------
def study() :

    global lbl
    lbl0.destroy()
    frm0.destroy()
    lbl.destroy()

    trucs = ["Si vous avez besoin de silence absolu, préférez une bibliothèque car vous n’y trouverez que des étudiants comme vous, cherchant à travailler au calme.",
     "Si vous préférez être seul au calme, étudiez dans votre chambre ou bureau, en veillant à ne pas être dérangé et en évitant toute source de distraction comme la télévision ou le téléphone portable.",
     "Si vous n’arrivez à vous concentrer qu’avec des bruits environnants, vous pouvez étudier en extérieur dans un jardin public.",
     "Vous pouvez étudier seul dans votre chambre avec de la musique pas trop forte.",
     "Il est important d’étudier soit en plein jour à l’extérieur, soit dans une pièce très bien éclairée. Vous ne vous abimerez pas les yeux et garderez l’esprit bien éveillé.",
     "Trouvez l’endroit qui vous convient le mieux, comme vous le ressentez, là où il vous sera facile de rester motivé, concentré et où vous aurez envie de travailler. Une fois cet endroit trouvé, faites en votre lieu de prédilection habituel pour étudier.",
     "Trouvez le moment idéal pour vous de la journée ou du soir. Celui où vous sentirez votre concentration au plus haut.",
     "Divisez vos révisions en séquences de 30 à 50 minutes maximum. Entre chaque séquence de travail, faites une pause, profitez-en pour aller prendre l’air.",
     "Apprenez à connaitre la limite de votre concentration et reconnaissez quand vous êtes épuisés. Ne combattez pas la fatigue"]
    t = random.randrange(0,8)

    global frm7
    frm7 = tk.Frame(root)
    frm7.columnconfigure(0, weight=1)

    lbl11 = tk.Label(frm7, text = trucs[t], font=('Times', 16))
    lbl11.grid(row=0, column=0)

    global a
    global q
    a = ""
    x = len(questions)
    for i in range(x):
        if questions[i].diffi == "Facile" :
            lbl10 = tk.Label(root, text = f"Question : {questions[i].ques}", font=('Times', 16), bg='#0f0')
            lbl10.pack()
            ent7 = tk.Entry(root, textvariable = rep, font=('Times', 16))
            ent7.pack()
            ent7.wait_variable(rep)
            btn14 = tk.Button(root, text="Entrer", font=('Times', 16), command=correct)
            btn14.pack()
            q += 1
            i += 1
        elif questions[i].diffi == "Moyen" :
            lbl10 = tk.Label(root, text = f"Question : {questions[i].ques}", font=('Times', 16), bg='#ff0')
            lbl10.pack()
            ent7 = tk.Entry(root, textvariable = rep, font=('Times', 16))
            ent7.pack()
            ent7.wait_variable(rep)
            btn14 = tk.Button(root, text="Entrer", font=('Times', 16), command=correct)
            btn14.pack()
            q += 1
            i += 1
        elif questions[i].diffi == "Difficile" :
            lbl10 = tk.Label(root, text = f"Question : {questions[i].ques}", font=('Times', 16), bg='#f00')
            lbl10.pack()
            ent7 = tk.Entry(root, textvariable = rep, font=('Times', 16))
            ent7.pack()
            ent7.wait_variable(rep)
            btn14 = tk.Button(root, text="Entrer", font=('Times', 16), command=correct)
            btn14.pack()
            q += 1
            i += 1
    frm7.pack()
    btn17 = tk.Button(root, text="Terminer", font=('Times', 16), command=resultat)
    btn17.pack()


#-------------------------------------------------------------------------------
def resultat() :
    c = 0
    f = 0

    global frm8
    frm8 = tk.Frame(root)
    frm8.columnconfigure(0, weight=1)

    global lbl12
    lbl12 = tk.Label(frm8, text = "Résultats", font=('Times', 16))
    lbl12.grid(row=1, column=0)

    a = len(questions)
    for i in range(a):
        b = a - 1
        if reponses[b] == "1" :
            lbl30 = tk.Label(root, text = f"1Question : {questions[b].ques}", font=('Times', 16))
            lbl30.pack()
            lbl31 = tk.Label(root, text = f"2Réponse : {questions[b].rep}", font=('Times', 16))
            lbl31.pack()
        elif reponses[b] == "0" :
            lbl32 = tk.Label(root, text = f"3Question : {questions[b].ques}", font=('Times', 16))
            lbl32.pack()
            lbl33 = tk.Label(root, text = f"4Réponse : {questions[b].rep}", font=('Times', 16))
            lbl33.pack()
            lbl34 = tk.Label(root, text = f"5Question : {mvreponses[b]}", font=('Times', 16))
            lbl34.pack()
            c += 1
    d = len(questions) - c
    e = (d / len(questions)) * 100
    e = int(e)

    lbl18 = tk.Label(frm8, text = f"Score : {d}/{len(questions)} ou {e}% ", font=('Times', 16))
    lbl18.grid(row=1, column=0)

    frm8.pack()
    menuprinc()
#-------------------------------------------------------------------------------
def add31() :
    add3 = "Facile"
#-------------------------------------------------------------------------------
def add32() :
    add3 = "Moyen"
#-------------------------------------------------------------------------------
def add33() :
    add3 = "Difficile"
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
questions = []
reponses = []
mvreponses = []
ques = tk.StringVar()
repo = tk.StringVar()
diff = tk.StringVar()
nume = tk.StringVar()
rep = tk.StringVar()

btn0 = tk.Button(root, text="Commencer", font=('Times', 16), command=o)
btn0.pack(padx=10, pady=10)

global lbl1
lbl1 = tk.Label(root, text="", font=('Times', 20))
lbl1.pack(padx=10, pady=10)

global frm1
frm1 = tk.Frame(root)
frm1.columnconfigure(0, weight=1)

lbl20 = tk.Label(frm1, text="", font=('Times', 16))
lbl20.grid(row=0, column=0)

frm1.pack()

global lbl19
lbl19 = tk.Label(root, text="", font=('Times', 20))
lbl19.pack(padx=10, pady=10)

btn16 = tk.Button(root, text="", font=('Times', 16), command=o)
btn16.pack(padx=0, pady=0)

global q
q = 0

root.mainloop()
