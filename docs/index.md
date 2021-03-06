Bonjour; Vous venez d'entrer dans un monde où seul la loi du plus fort compte. Un monde où le prédateur est sans pitié envers sa proie. Un monde où seul la survie de l'espèce compte. Le seul dieu de ce monde est le modèle Lotka-Volterra, régissant l'évolution des populations de ce monde grâce à des équations modélisant la prédation. Alors oui, ce n'est qu'une modélisation ne pouvant en aucun cas representer la complexité de la réalité. Mais on peut se réduire à des modèles réalistes tirés de la vraie vie, par exemple en se limitant à 3 espèces : un proie, un prédateur et un prédateur du prédateur, on peut se rapprocher de vrai écosystèmes existants. Avec nous vous allez pouvoir visiter des versions parallèles de cet endroit impitoyable. En variant "les conditions initiales" exemple les populations de départ de chacun des acteurs. On va plonger de plus en plus profond dans l'abysse de cet univers en complexifiant notre modélisation : ajouter des paramètres et des conditions liées à ces paramètres : exemples, la "faim" une proie ne peut se reproduire que lorsque sa jauge de faim est suffisante, un individu d'une espèce peut mourir de famine. Où encore ajouter le paramètre "âge": un individu peut mourir de vieillesse, où ne plus se reproduire à partir d'un certain âge. Après cette brève introduction il ne me reste qu'à vous souhaiter un bon voyage. Je vous laisse une dernière recommendation, lors de votre visite posez-vous la question : Suis-je le prédateur où la proie ?

Day 1 : Utilisation du terminal pour ajouter des fichiers depuis des fichers locaux + Début algorithme

Day 2 : Algorithme de base d'une chaine alimentaire selon les equations de lotka-volterra + création du terrain: 

Après avoir realisé une version basique de l'évolution de population sur une génération, aujourd'hui nous avons codé un algorithme plus general qui concerne les chaines alimentaires constituées d'un nombre de populations distinctes n > 2, le long de N generations. Pour cela nous avons pris la moyenne des effet qu'on la proie et le predateur sur une espèce située dans la chaine (sauf aux extrémités). Cette fonction nous retourne la resultante des equations a chaque generation que l'on pourra ensuite représenter sur des graphes.
\Nous avons aussi codé le terrain et l'avons représenté, ainsi celui-ci est différent à chaque fois qu'on en utilise un nouveau et dépend de sa position (plaine, foret ou montagne). Sur le terrain, on peut voir les emplacements de la végétation.

Day 3 : Aujourd'hui nous nous sommes focalisés surtout sur l'interface graphique. Nous avons représenté les populations sous formes de matrices carrées. Chaque élément de la matrice était soit occupé (Animal ou vegetation, signifié par sa signature) ou vacant (0). On commence par créer la matrice nulle de dimentions souhaitées, et on utilise "random" pour parcourir aléatoirement la matrice et ajouter la signature de chaque éspèce à la place des 0. On a ensuite transformé la matrice en tableau de couleur.
On va la prochaine fois se focaliser sur le dynamisme de la matrice selon les equations de lotka volterra et de la position des individus.
\Nous avons aussi codé la vision des animaux, ceux-ci ont seulement un périmètre dépendant de l'espèce. Ainsi nous avons pu coder les déplacements des animaux en fonction de la position de leur cible (soit proie soit autre animal pour la reproduction). Nous avons crée un dictionnaire des plantes, chaque plante étant représenté par une clé, et ayant une "jauge de vie".

Day 4 : Modification de la fonction déplacement à l'aide lde la fonction pop

On a commencé a écrire l'algorithme qui nous permet de mettre à jour la matrice en fonction de l'évolution du nombre de population de chaque éspèce et des paramétres de chaque individu. La difficulté principale sera de fusionner ces deux modèles en restant coherent.
En effet, le modèle de prédation décrit l'évolution de la population comme un tout; alors que notre modèle se concentre sur chaque individu. La solution à ce problème serait d'utiliste le modèle de lotka volterra afin de changer le nombre de population dans notre matrice alors que notre modèle (dictionnaire {éspèce : [age, fin]}) nous permettera de mettre a jour la disposition spaciale des populations.



Day 5 : Conception d'une map n'utilisant pas les formules de Lokta Volterra au cas ou la map avec les formules ne fonctionnerait pas. 
Mise en forme et fusion de toutes les algorithmes avec ajustement des fonctions. Correction de quelques erreurs dans les fonctions faites préalablement en observant les problèmes de déplacement sur les terrains. Première visualisation des déplacements sur un terrain de taille 16x16 avec 3 especes de chaque individus.
Nous avons presque finis avec l'algorithme de base; à part quelques bugs à règler. Il faudra maintenant implémanter cet algorithme dans un interface graphique. 


Day 6 : Animation de l'évolution du terrain, cette animation nous permet de voir les mois défilés les uns après les autres. Recherche pour faire une interface graphique prenant en compte toutes les variables. Nous avons deux modèles différents, l'un prenant en compte les formules du modèle Lokta Volterra et l'autre basé sur la réalité. L'objectif sera de comparer ces deux modèles lors de l'oral.
Recherche de plusieurs especes ainsi que leur caractéristique pouvant être représenter par nos modèles.
