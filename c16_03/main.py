note1 = ('eleve1', 'math', 13)
note2 = ('eleve1', 'physique', 15)
note3 = ('eleve1', 'math', 13)
note4 = ('eleve1', 'eco', 12)
note5 = ('eleve1', 'eco', 13)
note6 = ('eleve1', 'math', 12)
note7 = ('eleve2', 'math', 13)
note8 = ('eleve2', 'math', 14)

notes = [note1, note2, note3, note4, note5, note6,note7,note8]

print(notes)

# 4a
noteelv1=[]
for n in notes :
  if n[0]=="eleve1":
    noteelv1.append(n[2])
  moy =sum(noteelv1)/len(noteelv1)
print("La moyenne de l'élève est:",moy)

#4b
note_eleve_maths=[]
for n in notes :
  if n[0]=="eleve1":
    if n[1]=="math":
      note_eleve_maths.append(n[2])
      print(note_eleve_maths)
      moy2 =sum(note_eleve_maths)/len(note_eleve_maths)
print("La moyenne de l'élève en maths est:",moy2)

#4c
def moyenne_tuples(notes,matiere,eleve):
  note_filtres=[]
  for n in notes :
    if n[0]== eleve:
      if n[1]==matiere:
        note_filtres.append(n[2])
  moy3 =sum(note_filtres)/len(note_filtres)
  print(f'La moyenne de l {eleve} en {matiere} est:{moy3}')
  return(moy3)

moyenne_tuples(notes,"math","eleve1")

#5 
class Note:
  def __init__(self, eleve, matiere, valeur): #La méthode pour créer un objet
    self.eleve = eleve
    self.matiere = matiere
    self.valeur = valeur


  def afficher(self):
    print('eleve', self.eleve, 'matiere', self.matiere, 'note', self.valeur)


onote = Note('eleve1', 'maths', 13)
print(onote.eleve)
print(onote.matiere)
print(onote.valeur)
Note.afficher(onote)


onotes2 = [Note(*note) for note in notes]

#6 

def __str__(self):
    return f"{self.__class__.__name__}('{self.eleve}','{self.matiere}','{self.valeur}')"

    