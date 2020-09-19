**Sommaire**

[[_TOC_]]

# TD1 : Bibliothèque

_Remarque introductive_ : Les sujets de BE sont rédigés dans le format _Markdown_. Si ce format vous intéresse, vous trouverez des pointeurs vers des logiciels open source et des tutoriels sur le site du cours, sur https://pedagogie1.ec-lyon.fr/course/view.php?id=969.

> _Markdown est un langage de balisage léger créé en 2004 par John Gruber avec l'aide d'Aaron Swartz. Son but est d'offrir une syntaxe facile à lire et à écrire. Un document balisé par Markdown peut être lu en l'état sans donner l'impression d'avoir été balisé ou formaté par des instructions particulières. Il peut être converti en HTML, en PDF ou en d'autres formats._

## Objectif du sujet

Dans cet énoncé, nous abordons deux concepts de base de la programmation orientée objet, __l'encapsulation__ et la __composition__, qui ont été vus lors du premier cours. Nous nous exercerons également aux diagrammes de classe du langage graphique UML. Pour vos propres diagrammes, vous pouvez utiliser https://app.diagrams.net pour dessiner en ligne (et sauvegarder localement vos diagrammes sur votre machine).

Dans ce BE, il s'agit de concevoir et de réaliser un programme _simple_ de gestion d'une bibliothèque, intégrant des lecteurs, des livres et des emprunts.

_Remarque_ : Cet énoncé part d'un problème simple et connu qui permet d'en faire la conception et la réalisation dans le temps qui nous est imparti par les contraintes scolaires. Les choix de conception et de réalisation sont donc orientés par ces contraintes et par les objectifs pédagogiques, à savoir : apprendre la programmation orientée objet en Python. Il est clair que le même problème dans un cadre professionnel serait traité d’une autre manière et une solution basée sur des bases de données émergerait naturellement, solution que nous écartons a priori car en dehors du périmètre de ce cours.


## Cahier des charges

Le cahier des charges de notre application est décrit ci-dessous. Il est volontairement donné de manière informelle.

On doit pouvoir gérer le fond documentaire d'une bibliothèque identifiée par son nom. 

1. Pour simplifier, on considérera que tous les ouvrages sont des livres caractérisés par :

     - Le nom de l’auteur,
     - Le titre de l’ouvrage,
     - Un numéro de livre (attribué de manière unique par les bibliothécaires),
     - Le nombre d’exemplaires présents.

1. Notre application doit être capable de gérer également des lecteurs. Chacun d’eux est caractérisé par :

     - Son nom,
     - Son prénom,
     - Son adresse,
     - Un numéro (entier positif attribué de manière unique par les bibliothécaires).

1. On doit pouvoir ajouter un lecteur à tout moment et rechercher un lecteur (par son numéro de lecteur).   
On doit également pouvoir ajouter des ouvrages (acquisition de livres), et rechercher un ouvrage (par numéro).   
1. Tout lecteur peut emprunter des livres dans une ou plusieurs bibliothèques. Un lecteur peut emprunter plusieurs livres différents simultanément ou à des dates différentes et un même livre peut être emprunté par plusieurs lecteurs (s’il existe plusieurs exemplaires). Au moment de l’emprunt, il faut donc vérifier qu’un exemplaire de l'ouvrage est bien disponible et qu'il n'a pas été emprunté par le même lecteur. De manière symétrique, il faut également gérer le retour des livres.

1. On désire également pouvoir éditer des états détaillés :

    - Liste de tous les lecteurs d'une bibliothèque
    - Liste de tous les livres d'une bibliothèque
    - Liste de tous les emprunts d'une bibliothèque

1. Da manière facultative, on souhaite pouvoir retirer un lecteur s'il n'a plus d'emprunt en cours, et retirer un exemplaire non emprunté d'un livre (désherbage ou vol). Un livre qui n'aurait plus d’exemplaire ne doit plus apparaître dans la liste des livres à disposition de la bibliothèque. 

Cet énoncé a pour objectif de vous accompagner pour répondre au cahier des charges, __suivez le guide...__

_Remarque_ : Dans chaque titre de chapitre, vous verrez figurer un temps entre parenthèses : celui-ci correspond au temps approximatif à passer pour répondre aux questions du chapitre. Si vous prenez trop retard par rapport à ces _milestones_, demandez de l'aide à votre encadrant!

_Remarque_ : Même si ce n'est pas pas obligatoire, il vous est demandé de développer chaque classe dans un fichier python séparé (pensez à enregistrer tous les fichiers dans le même répertoire).

---

## Classe Lecteur et classe Livre (75 minutes)

**Point 1. du cahier des charges**

1. Dessinez la boîte UML de la classe __Lecteur__, en respectant le cahier des charges ci-dessus et les conventions syntaxiques présentées en cours.

    * Quels attributs devront être publiques, lesquels devront être privés? Pour rappel: selon les principes de l'encapsulation, un attribut devra être privé si on veut/peut exercer un contrôle dessus.      
    * Prévoyez une méthode qui affiche l'état d'un lecteur (pour rappel: l'état d'un objet est l'ensemble des valeurs de ses attributs à un instant donné).

1. Dans un fichier appelé _Lecteur.py_, implémentez votre classe progressivement, et développez simultanément le programme principal qui permet de vérifier le comportement attendu de votre classe (vu en cours: un programme principal commence par la commande `if __name__ == '__main__')`. Pour être plus précis:

    * Écrivez en premier lieu le constructeur de votre classe et créez un ou deux lecteurs dans votre programme principal. L'exécution du programme ne produit aucun résultat visible mais elle permet de vérifier que le programme est syntaxiquement correct. Ne passez pas à la méthode suivante tant que l'exécution produit des erreurs.   
    * Passez ensuite au codage de la méthode d'affichage (méthode dont le nom est `__str__`). Testez cette méthode en modifiant votre programme principal pour qu'il affiche les deux lecteurs précédemment créés. L'exécution du programme vous donne-t-elle satisfaction ?

1. Continuez ainsi pour les méthodes que vous avez prévues. Il est fort probable que nous soyons amenés à revenir sur cette classe par la suite, pour la compléter avec de nouvelles méthodes.    
Un programme principal typique aura l'allure suivante:

    ```python
    if __name__ == '__main__':

        # Des lecteurs
        L1 = Lecteur('Mzai',     'Ahmed',  'rue de la Paix',1)
        L2 = Lecteur('Dupond',   'John',   'rue de la Gare',2)
        L3 = Lecteur('Levgueni', 'Dimitri','rue La Fayette',3)
        L4 = Lecteur('Rodriguez','Alfonso','rue du Stade',  4)

        print('L1 -->', L1)
        print('L2 -->', L2)
        print('L3 -->', L3)
        print('L4 -->', L4)
    ```

**Point 2. du cahier des charges**

4. Réalisez la même démarche pour la classe __Livre__, que vous coderez dans le fichier _Livre.py_. Un programme principal typique aura l'allure suivante:

    ```python
    if __name__ == '__main__':

        # Des livres
        B1 = Livre('Le Père Goriot',  'Honoré de Balzac',        2,101)
        B2 = Livre("Léon l'Africain", 'Amin Maalouf',            2,102)
        B3 = Livre('Le Petit Prince', 'Antoine de Saint-Éxupery',2,103)
        B4 = Livre("L'Étranger",      'Albert Camus',            2,104)

        print('B1 -->', B1)
        print('B2 -->', B2)
        print('B3 -->', B3)
        print('B4 -->', B4)
    ```


## Classe Bibliothèque (75 minutes)

**Points 3. et 5. du cahier des charges**

1. Un bibliothèque gère une collection de livres et un répertoire de lecteurs (et des emprunts, mais nous verrons cela plus tard). Quels liens entre les classes __Bibliotheque__ et __Livre__ d'une part, et __Bibliotheque__ et __Lecteur__ vous semblent les plus adaptés pour exprimer ces relations ? *Tip* Si un Livre appartient à une bibliothèque, un lecteur peut s'inscrire dans plusieurs bibliothèques (vous voyez la différence?)! Dessinez alors le schéma UML entre ces 3 classes. N'oubliez pas d'ajouter les cardinalités de part et d'autre des liens.  
Dessinez ensuite le détail de la boîte UML de la classe __Bibliothèque__, de manière à répondre au point 3. du cahier des charges.

1. Dans un nouveau fichier appelé _Bibliotheque.py_, commencez par coder le constructeur de la classe __Bibliotheque__, en choisissant la structure de données adéquate pour gérer les lecteurs et les livres. Créez un programme principal, dans lequel vous créerez une bibliothèque (de nom _Michel Serre_ ?). Codez ensuite la méthode `__str__` qui affiche simplement le nom de la bibliothèque. Testez dans votre programme principal. 

1. On se concentre sur les lecteurs. Codez successivement l'implémentation des méthodes permettant   
    * d'ajouter un lecteur (on fera l'hypothèse qu'on n'essaye pas d'ajouter un lecteur déjà présent),    
    * d'afficher la liste des lecteurs de la bibliothèque,    
    * de chercher un lecteur par son numéro,    
    * de chercher un lecteur par son nom,

    N'oubliez pas de tester chacune des méthodes avant de passer à la suivante! N'hésitez pas à compléter la classe __Lecteur__ s'il vous manque des méthodes...  

1. Faites de même avec les livres. On ne vérifiera pas si le livre est déjà présent dans la collection avant de l'ajouter.


## Les emprunts (90 minutes)

**Points 4. et 5. du cahier des charges**

Un emprunt sera modélisé par un objet qui associe un lecteur (connu par son identifiant) avec un livre (connu par son identifiant) à une date donnée.    

1. Dessinez la boite UML de la classe __Emprunt__. Celle-ci doit permettre de créer un nouvel emprunt, et d'afficher son état. Prévoyez des getter pour les attributs privés. Comment modéliser en UML les relations de la classe __Emprunt__ avec les classes __Lecteur__ et __Livre__?   

1. Implémentez votre classe dans un fichier appelé _Emprunt.py_. Complétez, en parallèle de l'implémentation des méthodes, un programme principal qui pourra finalement avoir l'allure suivante:   
    
    ```python
    if __name__ == '__main__':

        # Creation d'une Emprunt
        E1 = Emprunt(1, 2)
        print('E1 --> ', E1)
        print("Num lecteur de l'emprunt E1: ", E1.get_numero_lecteur())
    ```    
    Résultat:
    
    ```console
        E1 -->  Emprunt - Numero lecteur : 1, Numero livre: 2, Date : 2020-08-23
        Num lecteur de l'emprunt E1:  1
    ```

    _Remarque_ : Pour la date, on pourra utiliser l’instruction `date.isoformat(date.today())`, en ayant pris soin d'importer la librairie, à l'aide de la commande `from datetime import date` (à positionner tout en haut de la classe).

1. À ce stade du développement, les emprunts sont indépendants de la bibliothèque. Compléter votre schéma UML précédent pour modéliser le fait que c'est la bibliothèque qui gère tous les emprunts. Quel nouvel attribut de la classe __Bibliotheque__ prévoyez-vous pour stocker la collection des emprunts ?     

1. Codez la méthode `emprunt_livre(...)` dans la classe __Bibliotheque__. Cette méthode est sensée    
    
    1. rechercher le lecteur à partir de son numéro,    
    1. rechercher le livre à partir de son numéro et vérifier qu'il reste au moins un exemplaire à emprunter, et    
    1. créer un nouvel objet `emprunt` que l'on stockera dans la liste des emprunts.

    _Tip_ : Pensez à

    1. modifier la classe __Lecteur__ de manière à lui ajouter un compteur de livres empruntés (à sa création, un lecteur n'a pas d'emprunt). Prévoyez une méthode publique appelée `incremente_nb_emprunts()`.    
    1. modifier la classe __Livre__ de manière à lui ajouter un compteur qui tient à jour le nombre d'exemplaires disponibles (à sa création, un livre à autant d'exemplaires disponibles qu'il a de nombre d'exemplaires). Prévoyez une méthode publique appelée `decremente__dispo()` qui décrémentera le nombre d'exemplaires disponibles et renverra `True` s'il reste au moins un exemplaire, sinon `False`.    

    Pensez à modifier les méthodes `__str__` des 2 classes pour y inclure l'affichage de leur nouvel attribut.

    Vous ajouterez également une méthode `affiche_emprunts()` pour visualiser la liste des emprunts et testerez vos nouvelles méthodes avant de passer à la suite. Pour tester votre méthode, ajouter ces quelques lignes à votre programme principal:

    ```python
    if __name__ == '__main__':
    
        ...
    
        # Quelques emprunts
        print('\n--- Quelques emprunts :')
        b.emprunt_livre(1,101)
        b.emprunt_livre(1,104)
        b.emprunt_livre(2,101)
        b.emprunt_livre(3,101)
        print(b.chercher_livre_numero(101))
        
        # Affichage des emprunts, des lecteurs et des livres
        print('\n--- Liste des emprunts :')
        b.affiche_emprunts()
    ```   
    et vérifiez que vous obtenez un affichage similaire à celui-ci

    ```console
        --- Quelques emprunts :
          ->Livre 101  - Emprunt impossible
        Livre - Nom auteur: Honoré de Balzac, Titre ouvrage: Le Père Goriot, \
        Nb examplaires: 2, Numero: 101, Nb dispo: 0.
        
        --- Liste des emprunts :
        Emprunt - Numero lecteur : 1, Numero livre: 101, Date : 2020-08-23
        Emprunt - Numero lecteur : 1, Numero livre: 104, Date : 2020-08-23
        Emprunt - Numero lecteur : 2, Numero livre: 101, Date : 2020-08-23
    ```
    
1. Pour simuler le rendu d'un livre par un lecteur à la bibliothèque, implémentez une méthode _retour\_livre(self, numero_lecteur, numero_livre)_. Pour cela, on pourra faire appel à une __méthode privée__ appelée _\_\_chercher_emprunt(self, numero_lecteur, numero_livre)_ qui renverra l'instance de l'emprunt s'il fait partie de la liste des emprunts, ou _None_ dans le cas contraire. La méthode _retour\_livre_ affichera un message d'erreur si l'emprunt n'existe pas. Dans le cas contraire, détruisez l'emprunt et pensez à mettre à jour le nombre d’exemplaires du livre ainsi que le nombre d’emprunts du lecteur.

    Tester le retour dans votre programme principal grâce au code suivant :

    ``` python
    if __name__ == '__main__':
    
        ...
        
        # Quelques retours de livres
        print('\n--- Quelques retours de livres :')
        b.retour_livre(1,101)
        b.retour_livre(1,102)
        b.retour_livre(10,108)
    ```
    qui devra afficher quelque chose de similaire à :

    ```console
        --- Quelques retours de livres :
        Aucun emprunt ne correspond a ces informations :  1 102
        Aucun emprunt ne correspond a ces informations :  10 108
    ```



## Questions ouvertes supplémentaires

**Point 6. (facultatif) du cahier des charges**

1. Implémentez une méthode permettant de supprimer un livre (si tous les exemplaires sont rendus).   

    ```python
    def retrait_livre(self,numero):
        # On cherche le livre
        livre = self.chercher_livre_numero(numero)
        if livre == None:
            return False
        # On verifie que le livre n'est pas en cours d'emprunt
        for e in self.__emprunts:
            if e.get_numero_livre()==numero:
                return False
        # On peut ici retirer le livre de la liste
        self.__livres.remove(livre)
        return True
    ```   
    Les commandes
    
    ```python
    if __name__ == '__main__':
        ...

        # Suppression de quelques livres
        print('\n--- Suppression de quelques livres :')
        rep = b.retrait_livre(101)
        if not rep:
            print('Retrait du livre impossible')
        else:
            print('Retrait du livre effectue')
    
        b.retour_livre(2,101)
    
        rep = b.retrait_livre(101)
        if not rep:
            print('Retrait du livre impossible')
        else:
            print('Retrait du livre effectue')
    ```   
    donnent

    ```console
        --- Suppression de quelques livres :
        Retrait du livre impossible
        Retrait du livre effectue
    ```

1. Implémentez une méthode permettant de supprimer un lecteur (si il n'est redevable d'aucun emprunt).

    ```python
    def retrait_lecteur(self,numero):
        # On cherche le lecteur
        lecteur = self.chercher_lecteur_numero(numero)
        if lecteur == None:
            return False
        # On verifie qu'il n'a pas d'emprunt en cours
        for e in self.__emprunts:
            if e.get_numero_lecteur()==numero:
                return False
        # On peut ici retirer le lecteur de la liste
        self.__lecteurs.remove(lecteur)
        return True 
    ```   
    Les commandes

    ```python
    if __name__ == '__main__':
        ...
        
        # Suppression de quelques lecteurs
        print('\n--- Suppression de quelques lecteurs :')
        rep = b.retrait_lecteur(1)
        if not rep:
            print('Retrait du lecteur impossible')
        else:
            print('Retrait du lecteur effectue')
    
        b.retour_livre(1,104)
    
        rep = b.retrait_lecteur(1)
        if not rep:
            print('Retrait du lecteur impossible')
        else:
            print('Retrait du lecteur effectue')
    ```    
    donnent

    ``` console
        --- Suppression de quelques lecteurs :
        Retrait du lecteur impossible
        Retrait du lecteur effectue
    ```

1. Un livre qui n'aurait plus d’exemplaire ne doit plus apparaître dans la liste des livres à disposition de la bibliothèque. 

1. Comment implémenter un mécanisme de vérification de l'unicité de l'identifiant d'un lecteur et de celui d'un livre ?