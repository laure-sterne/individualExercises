`En français`

# Multi-threading

Tâches en parallèle via le multithreading

## Objectifs 
- Multi-threading
- Synchronization des accès

## Enoncé

Cette exercice a pour objectif de compresser les images d'un répertoire en faisant le traitement de chaque image dans un thread afin de minimiser le temps d'exécution et maximiser l'utilisation des cores. (le répertoire ne contient que 4 images, donc on aura au plus 4 threads simultanement !). 

Ce traitement sera aussi l'occasion de mesurer les tailles des fichiers avant/aprés compression pour, en fin de traitement, afficher un taux de compression pour l'ensemble des fichiers (ce chiffre pourrait être le rapport des tailles de fichiers aprés / avant traitement).

Les fichiers sont disponibles dans un répertoire `IMAGES` (voir l'archive *IMAGES.tar* à downloader puis uploader vers le notebook). Les fichiers compressés seront mis dans un répertoire `COMPRESSED_IMAGES`, à créer s'il n'existe pas, par un des threads de traitement d'image.
Penser à synchroniser les sections critiques (création du répertoire de destination, cumul des tailles de fichiers).

Exemple de résultat d'exécution du code

https://indico.in2p3.fr/event/16733/attachments/46220/57699/enonce-ex4.pdf

Quand l'exercise sera (quasi) fini, vous pourriez essayer de faire le traitement des fichiers en mode séquentiel i.e. sans utiliser les threads pour se persuader de ce qu'apporte le multithreading en terme de gain de temps d'exécution sur cette exemple là.

## Indications
### Numéro 1
Faire une programmation en orienté objet et en utilisant le logging comme dans l'exercice précedent (un logger par classe et avec affichage de la classe mais aussi du `thread via %(threadName)12s` dans le pattern de formattage).

On aura une classe `CompressOneImage`, dont le but est de compresser une image, et ceci dans un thread (cette classe dérivera donc de Thread).
On aura une classe `ProcessImages`, dont le but est de scanner le répertoire IMAGES/ et de lancer un thread par image à traiter.

Et enfin un code d'utilisation de cette classe.

### Numéro 2
Le scan du répertoire IMAGES/ peut se faire comme ceci

```
# filenames will be a list of all files found in directory
    for (dirpath, dirnames, filenames) in walk(CompressImage.IMAGES_DIRNAME):
        pass
```

Comme dit dans le commentaire, filenames contiendra tous les fichiers du répertoire.
Il faudrait donc filter les noms selon leur extension pour ne retenir que ceux suffixés ‘.jpg’ (l'occasion
d'utiliser les "listes comprehensions" !).

### Numéro 3

Le traitement d'images sera fait avec module **Image** du package **PIL**.
La lecture d'une image, l'obtention de la taille du fichier, et la sauvegarde de l'image compressée seront fait selon ces indications.

```
# opening and getting image
picture = Image.open(image_filepath)
...

# get image filesize (in B)
image_filesize = os.stat(image_filepath).st_size
...

# compress image
compressed_image_filepath = "..."
picture.save(compressed_image_filepath, "JPEG", optimize=True, quality=30)
... 
```
### Numéro 4

La création du répertoire *COMPRESSED_IMAGES*, sera faite selon ces instructions. 

(Penser à synchroniser les accès concurrents si cette étape est faite dans un thread comme cela est
demandé)

```
if not os.path.exists(compressed_image_directory):
    os.makedirs(compressed_image_directory)
```

### Numéro 5

Les calculs et cumul des tailles des fichiers seront fait dans les threads, et stockés dans des variables
globales.

Penser à synchroniser les accès concurrents.

### Numéro 6

Pour démarrer, un aperçu de la classe **CompressOneImage**

```
import logging

import threading
from threading import Thread

import sys
import os
from os import walk
from PIL import Image # available with 'pip install pillow'

import time # for time.time() which gives time in seconds since the epoch

class CompressOneImage(Thread):
    # When specifying datefmt, (see below), ms are lost unless you add then with
 %(msecs) pattern
    MY_FORMAT = "%(asctime)s.%(msecs)03d %(name)16s %(threadName)12s %(levelname
)-6s %(message)s"
    logging.basicConfig(format=MY_FORMAT, datefmt='%H:%M:%S', level=logging.INFO
)

    IMAGES_DIRNAME = "IMAGES"
    COMPRESSED_IMAGES_DIRNAME = "COMPRESSED_IMAGES"
    # will hold the cumulative sizes of processed files
    IMAGES_FILESIZE = 0
    COMPRESSED_IMAGES_FILESIZE = 0
...
```


`In english`

# Multithreading

Parallel tasks via multithreading

## Goals
- Multi-threading
- Access synchronization

## States

This exercise aims to compress the images of a directory by processing each image in a thread in order to minimize the execution time and maximize the use of cores. (the directory only contains 4 images, so we will have at most 4 threads simultaneously!).

This processing will also be an opportunity to measure the sizes of the files before/after compression in order, at the end of the processing, to display a compression rate for all the files (this figure could be the ratio of the file sizes after/before processing).

The files are available in an `IMAGES` directory (see the *IMAGES.tar* archive to download then upload to the notebook). 

The compressed files will be put in a `COMPRESSED_IMAGES` directory, to be created if it does not exist, by one of the image processing threads.

Remember to synchronize the critical sections (creation of the destination directory, accumulation of file sizes).

Example of code execution result

https://indico.in2p3.fr/event/16733/attachments/46220/57699/enonce-ex4.pdf

When the exercise is (almost) finished, you could try processing the files in mode sequential i.e. without using threads to convince oneself of what multithreading brings in terms of saving execution time on this example.

## Directions

### Number 1
Do object-oriented programming and use logging as in the previous exercise (one logger per class and with display of the class but also of the `thread via %(threadName)12s` in the formatting pattern).

We will have a `CompressOneImage` class, whose purpose is to compress an image, and this in a thread (this class will therefore derive from Thread).

We will have a `ProcessImages` class, the purpose of which is to scan the IMAGES/ directory and launch one thread per image to be processed.

And finally a code for using this class.

### Number 2

The scan of the IMAGES/ directory can be done like this
```
# filenames will be a list of all files found in directory
    for (dirpath, dirnames, filenames) in walk(CompressImage.IMAGES_DIRNAME):
        pass
```

As said in the comment, filenames will contain all files in the directory.
It would therefore be necessary to filter the names according to their extension to retain only those suffixed '.jpg' (the occasion
to use "list comprehensions"!).

### Number 3

Image processing will be done with the **Image** module of the **PIL** package.

Reading an image, getting the file size, and saving the compressed image will be done according to these guidelines.

```
# opening and getting image
picture = Image.open(image_filepath)
...

# get image filesize (in B)
image_filesize = os.stat(image_filepath).st_size
...

# compress image
compressed_image_filepath = "..."
picture.save(compressed_image_filepath, "JPEG", optimize=True, quality=30)
... 
```

### Number 4

The creation of the COMPRESSED_IMAGES directory will be done according to these instructions. (Think about synchronizing concurrent accesses if this step is done in a thread as is
demand).

```
if not os.path.exists(compressed_image_directory):
    os.makedirs(compressed_image_directory)
```

### Number 5

Calculations and accumulation of file sizes will be done in threads, and stored in variables
global.

Think about synchronizing concurrent accesses.

### Number 6

To start, an overview of the **CompressOneImage** class


```
import logging

import threading
from threading import Thread

import sys
import os
from os import walk
from PIL import Image # available with 'pip install pillow'

import time # for time.time() which gives time in seconds since the epoch

class CompressOneImage(Thread):
    # When specifying datefmt, (see below), ms are lost unless you add then with
 %(msecs) pattern
    MY_FORMAT = "%(asctime)s.%(msecs)03d %(name)16s %(threadName)12s %(levelname
)-6s %(message)s"
    logging.basicConfig(format=MY_FORMAT, datefmt='%H:%M:%S', level=logging.INFO
)

    IMAGES_DIRNAME = "IMAGES"
    COMPRESSED_IMAGES_DIRNAME = "COMPRESSED_IMAGES"
    # will hold the cumulative sizes of processed files
    IMAGES_FILESIZE = 0
    COMPRESSED_IMAGES_FILESIZE = 0
...
```