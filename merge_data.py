# inport des librairies 
import os
#import shutil
# import touch

# acceder au dossier parent
cheminParent = "/home/mickael/darknet/data/data_pcb/"
savingFolder = "/home/mickael/darknet/data/data_pcb/merge_3size/"
dirs = os.listdir(cheminParent)
# acceder au dossier fils 
for subfold in dirs:
	if subfold == "pcb_split_512" or subfold == "pcb_split_640" or subfold == "pcb_split_768":
		name_subfold = subfold
		nouveau_chemin = cheminParent + name_subfold
		subDir = os.listdir(nouveau_chemin)
		for elt in subDir:
			if elt == "train":
				# faire le changement du nom de l'element contenu dans le dossier
				trainPath = nouveau_chemin + "/train/"
				trainDir = os.listdir(trainPath)
				for img in trainDir: # ici j'accede deja au dossier train
					# ici je vais modifier le nom de chaque elts et ajouter le nom du parent
					# peut etre il me faut ajouter l'extension de chaque elt ici? pour que ca lise
					# reflechir plutot a l'alternative de renome le fichier (chemin complet de depart de fichier 
					# chemin complet de destination avec modification de nom
					if img.endswith(".jpg"):
						nameImg = img[:-4]
						newEltName = subfold + "_" + nameImg+".jpg"
						# changer le nom de fichier a renomer
						newFile = trainPath + nameImg+".jpg" # ceci est la source
						destFile = savingFolder+"train/"+subfold+"_"+ nameImg+".jpg"
						os.rename(newFile, newFile) # ecriture repertoire courant 
						os.rename(newFile, destFile) # ecriture repertoire merge
					# maintenant je veux pouvoir sauvegarder tous ses elements dans un dossier 
					#print(newEltName)
					#touch.touch(savingFolder+newEltName)
						# completeName = os.path.join(savingFolder+"train/", newEltName)
						# # dest = shutil.copyfile(completeName, savingFolder) # (source, destination)
						# file1 = open(completeName, "w")
					# print(completeName)
					else:
						nameImg = img[:-4]
						newEltName = subfold + "_" + nameImg+".txt"
						# f = open(newEltName, "r") # je voulais tester l'ouverture du fichier texte en lecture
						# print(f.read())
						newFile = trainPath + nameImg+".txt" # ceci est la source
						destFile = savingFolder+"train/"+subfold+"_"+ nameImg+".txt"
						os.rename(newFile, newFile) # ecriture repertoire courant 
						os.rename(newFile, destFile) # ecriture repertoire merge

						# completeName = os.path.join(savingFolder+"train/", newEltName)
						# # os.rename(source, destination)
						# file1 = open(completeName, "w") # premiere option qui a marche mais de poids 0kb

			elif elt == "val":
				# faire le changement du nom de l'element contenu dans le dossier
				valPath = nouveau_chemin + "/val/"
				valDir = os.listdir(valPath)
				for img in valDir: # ici j'accede deja au dossier train
					# ici je vais modifier le nom de chaque elts et ajouter le nom du parent
					# newEltName = subfold + "_" + img
					# completeName = os.path.join(savingFolder+"val/", newEltName)
					# file1 = open(completeName, "w")

					if img.endswith(".jpg"):
						nameImg = img[:-4]
						newEltName = subfold + "_" + nameImg+".jpg"
						# changer le nom de fichier a renomer
						newFile = valPath + nameImg+".jpg" # ceci est la source
						destFile = savingFolder+"val/"+subfold+"_"+ nameImg+".jpg"
						os.rename(newFile, newFile) # constat: rename deplace le fichier si source # destination
						os.rename(newFile, destFile) # ecriture repertoire merge


					else:
						nameImg = img[:-4]
						newEltName = subfold + "_" + nameImg+".txt"
						# f = open(newEltName, "r") # je voulais tester l'ouverture du fichier texte en lecture
						# print(f.read())
						newFile = valPath + nameImg+".txt" # ceci est la source
						destFile = savingFolder+"val/"+subfold+"_"+ nameImg+".txt"
						os.rename(newFile, newFile) # ecriture repertoire courant 
						os.rename(newFile, destFile) # ecriture repertoire merge
					#print(completeName)
# parcourir chaque dossier fils et extraire les differents 
# element puis leur ajouter le nom de leur dossier parent

