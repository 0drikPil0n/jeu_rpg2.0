from Création_personnage.sous_classe import SousClasse
from personnage import Personnage
from classe import Classe
from sous_classe import SousClasse
from race import Race

# Races
humain = Race(nom="Humain",age_min=18, age_max=120)
ogre = Race(nom="Ogre",age_min=18, age_max=150)
nain = Race(nom="nain", age_min=15, age_max=250)
elf = Race(nom="Elf", age_min=16, age_max=500)
# Sous-classes
prince = SousClasse(nom="Prince",arme="Poignard",pv=200, degats=[20,15], atts_spe=[60,40])
princesse = SousClasse(nom="Princesse",arme="Dague",pv=175,degats=[30,10],atts_spe=[50])
roi = SousClasse(nom="Roi",arme="Épée",pv=250,degats=[50,40,20,20],atts_spe=[75])
reine = SousClasse(nom="Reine",arme="Épée",pv=225,degats=[60,30,30,10],atts_spe=[70])
fermier = SousClasse(nom="Fermier",arme="Houe",pv=100,degats=[10,8,8,5],atts_spe=[20])
forgeron = SousClasse(nom="Forgeron",arme="Marteau",pv=120,degats=[12,9,8,8],atts_spe=[25])
boucher = SousClasse(nom="Boucher",arme="Couteau",pv=110,degats=[10,10,8,6],atts_spe=[20])
pecheur = SousClasse(nom="Pêcheur",arme="Morue",pv=110,degats=[10,10,8,6],atts_spe=[20])
mage = SousClasse(nom="Mage",arme="Livre de sort",pv=250,degats=[40,30],atts_spe=[100])
sorcier = SousClasse(nom="Sorcier",arme="Baguette magique",pv=250,degats=[50,35,25],atts_spe=[110])
alchimiste = SousClasse(nom="Alchimiste",arme="Potions magiques",pv=250,degats=[50,35,25],atts_spe=[110])
shaman = SousClasse(nom="Shaman",arme="Invocation d'esprit",pv=230,degats=[60,40,20],atts_spe=[125,90])
archer = SousClasse(nom="Archer",arme="Arc",pv=150,degats=[100,40,40,40],atts_spe=[115,110])
cavalier = SousClasse(nom="Cavalier",arme="Lance",pv=300,degats=[40,20,20,10],atts_spe=[80,75])
infanterie = SousClasse(nom="Infantrie",arme="Fusil",pv=275,degats=[60,40,30,20],atts_spe=[100,90])
mercenaire = SousClasse(nom="Mercenaire",arme="Double dague",pv=200,degats=[75,40,30,30],atts_spe=[125,90])
# Classes
royaute = Classe(nom="Royauté",sous_classes=[prince,princesse,roi,reine])
villageois = Classe(nom="Villageois",sous_classes=[fermier,forgeron,boucher,pecheur])
magicien = Classe(nom="Magicien",sous_classes=[mage,sorcier,alchimiste,shaman])
armee = Classe(nom="Armée",sous_classes=[archer,cavalier,infanterie,mercenaire])

