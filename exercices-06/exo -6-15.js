// exo 6.15
// Trouvez la chaîne de caractères la plus longue dans une liste.
// Affichez son index, sa valeur et sa longueur.
//
// ATTENTION: ne pas utiliser la fonction list.index()
// ATTENTION: cet exercice nécessite l'utilisation d'une boucle`for`

let my_list = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit']

// réponse 6.15

// pour avoir la longeur d'une liste c'est my_list.length

console.log("foo.length")

// my_list.length 
// my_list[0].length (affiche la longeur de la chaine de caractére)

let index = null;
let valeur = "";
let longeur = 0;

if (my_list[i] > length > longeur) {
   // mise à jour
   // ou stockage de la plus grande longeur rencontrée jusque maintenant
   longeur = my_list.length;
   index = i;
   valeur = my_list[i]
}


console.log(index);
console.log(valeur);
console.log(longeur);

// boucle for each qui permet de recuperer mes valeurs mais pas l'index
let i = 0;
valeur = "";
longeur = 0;


for (let word of my_list) {
   
   // console.log(i, word,lword.length)
   if (my_list[i] > length > longeur) {
      // mise à jour
      // ou stockage de la plus grande longeur rencontrée jusque maintenant
      longeur = my_list.length;
      index = i;
      valeur = my_list[i]
   }
   // increment de l'index
   i++;
   //c

}

console.log(index);
console.log(valeur);
console.log(longeur);

