Voici une démo des principales commandes de git, à utiliser depuis un terminal. Pour **Windows**, utilisez le terminal appelé ``Git Bash``, qui a été installé en même temps que **git**). 

**Configuration de git** (à faire une fois pour toute)
```bash
>> git config --global color.ui true
>> git config --global user.name "votre_pseudo"
>> git config --global user.email moi@email.com
>> git config --global core.editor geany                                       #(for Linux if installed)
>> git config --global core.editor "/App.../Sublime\ Text.app/.../bin/subl -w" #(for Mac if installed)
>> git config --global core.autocrlf true                                      #(for Windows)
>> git config --list
>> cat ~/.gitconfig
```

**git clone / status / log**
```bash
>> git clone https://gitlab.ec-lyon.fr/sderrode/helloworld.git
>> cd helloworld
>> git status
>> git log
```
Il s'agit ici du clonage d'un projet existant sur votre espace **gitlab**.

**Modification d'un fichier existant**
```bash
>> subl readme.md                               #(modification du fichier)
>> git status
>> git commit -a -m "modification de readme.md"
>> git status
>> git log
```

**Création d'un fichier et ajout à git**
```bash
>> touch prog.py                          #(création d''un nouveau fichier vide)
>> subl prog.py                           #(écriture d''un programme dans le fichier)
>> python prog.py
>> git status
>> git add prog.py                        #(suivi du fichier par git)
>> git add -A                             #(suivi de tous les nouveaux fichiers )
>> git commit -a -m "ajout d'un fichier"
>> git status
>> git log
```
On peut utiliser ce procédé pour ajouter un fichier ``.gitignore`` sur la racine du projet.


**Différence entre 2 commit**
```bash
>> git diff HEAD^ HEAD README.md  #(entre l''avant dernier et le dernier commit)
```
On peut remplacer ``HEAD^`` et ``HEAD`` par deux numéros de commit.

**Revenir en arrière**
```bash
>> git reset --hard 82f5     #(attention suppression des commit les plus récents!)
>> git checkout 1ce87820b4b1 #(bref saut dans un commit précédent)
>> git log
>> ls
>> git checkout master (on revient dans l''état initial)
>> git log
>> ls
```

**Publication vers gitlab et mise à jour depuis gitlab**
```bash
>> git status
>> git push    #(publication vers gitlab de tous les nouveaux commit)
>> git pull    #(récupération des changements publiés par d'autres)
```

Si un collègue du projet à mis à jour le dépôt **gitlab**, alors il faut fusionner ces modifications avec vos propres travaux, localement sur votre machine. Avant de lancer la commande, pensez à commiter vos propres changements. Si la fusion pose problèmes (vous avez travaillé sur le même bout de code et vos corrections ne sont pas fusionable de manière automatique), alors git vos informe de la procédure manuelle à suivre.

**Création d'une branche**
Les branches sont essentiellement utilisées pour tester une idée sans perturber le projet. Si vous validez cette idée, alors il devient possible de fusionner la branche avec la branche principale:
```bash
>> git branch essai                                #(on créé une nouvelle branche essai
>> git branch
>> git checkout essai                              #(on bascule vers cette branche)
>> touch ALIRE.tx
>> subl ALIRE.tx
>> git add ALIRE.tx
>> git commit -a -m "add file ALIRE.tx"
>> ls
>> git log
>> git checkout master
>> ls
>> git merge essai -m "merge de la branche essai"  #(vous pouvez préciser un message qui explique le merge)
>> ls
>> git branch -d essai                             #(destruction de la branche après merge)
```
On peut très bien merger une branche et continuer son développement pour faire un second merge plus tard. On peut aussi publier la branche sur **gitlab** (pour l'instant elle ne reste que locale).

**Tagger une version**
```bash
>> git tag -a v0.1 HEAD -m "my version 0.1"
>> git tag                                  #(liste les tags)
>> git push --tags                          #(envoi des tag sur le dépôt gitlab)
```

**Archiver une version**
```bash
>> git archive --format=tgz --prefix=git-0.1/ HEAD >git-0.1.tgz
>> ls
```
