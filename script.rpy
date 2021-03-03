# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define n = Character('Narrateur', color="#c8ffc8")
define m = Character('MisterADN', color="#F8BC26")

# Le jeu commence ici
label start:
    n "Nous voici donc sur la planète HERMITEON-1, plongeons maintenant retrouver nos amis les premiers organismes avec plusieurs cellules. Oh regarde en voilà un ! Il s’agit d’un « Initius Projectblocus ». Tu te rends compte ? Cet individu va être à l’origine de toute la vie pluricellulaire sur cette planète !"
    
    n "Pour le moment la planète ressemble à  un gigantesque océan où les conditions ont provoqué l’émergence d’organismes multicellulaires ressemblant à des plantes commencent  à sortir de l’eau et à peupler la planète HERMITEON-1."

    n "Retournons voir nos amis les Initius. Oh regarde ! Ils sont passés dans un courant marin  le temps que nous étions hors de l’eau et ont été dispersé un peu partout sur la planète. Restons avec ce petit groupe."

    n "Au cours du temps, ce petit groupe va se multiplier grâce à ce qu’on appelle la reproduction sexuée. Ainsi, des cellules qui viennent de deux Initius différents, le papa et la maman, et qui sont spécialisées dans la reproduction vont se joindre pour former un nouvel Initius. Incroyable non ?"

    n "Au cours du temps, de plus en plus d’Initius vont se reproduire et vont ainsi agrandir leur groupe."
##Montrer apparition de plein d’Initius sur l’image, puis n’en revenir que sur un

    n "Dans ces individus on en reconnait certains qui commencent à avoir une couleur différente sur leur dos. En effet je ne sais pas si tu as vu mais au lieu d’avoir le dos bleu, certains d’entre eux commencent à avoir de plus d’avoir le dos noir." 
##Montrer deux Initius : un avec un dos bleu et un avec dos noir

    n "Faisons un zoom sur les ordres Initius qui se sont dispersés un peu partout et qui ont prospéré et qui depuis le temps ont eux aussi eu des enfants."
##Initius avec des dos de toutes les couleurs

    n "Waouh ! C’est incroyable après un certain temps on dirait que des Initius avec des couleurs différentes se sont développées aux 4 coins de la planète ! Revenons à ceux qui ont un dos bleu et un dos noir."
##Augmenter luminosité de l’affichage si y a moyen

    n "Waouh quel endroit ensoleillé, le temps qu’on parte faire le tour de cette planète HERMITEON-1."
##NOM DE LA PLANEEEEETTTEEEEE

    n "Quelques millions d’années se sont écoulées, nos Initius ont encore eu des petits et se ont peut clairement voir deux populations dans notre espèce, une avec le dos noir et une avec le dos bleu."

    n "On dirait que certaine commence même à avoir un dos rouge… mais il semble que les dos noirs soient plus nombreux… Pfiou qu’il fait chaud, ça fait déjà un moment que le soleil est là…"

    menu:
        n "A ton avis jeune scientifique, quel Initius a le plus de chances de d’avoir de bébé sur cet océan ensoleillé ?"
        "Ceux qui ont un dos noir":
            jump dos_noir
        "Ceux qui ont un dos bleu ou rouge":
##Apparition de deux initius avec des yeux en croix et avec la langue qui pend pour bien faire comprendre qu’ils sont canés
            n "Aie Aie … on ne l’avait pas vu quand on était parti faire le tour du monde mais il semble que ceux avec un dos rouge et bleu étaient moins nombreux que ceux avec un dos noir. "

    n "Au cours du temps la chaleur et la température liés aux rayons du soleil n’ont pas aidé les pauvres initius à dos bleus et rouges à s’en sortir. Ils ont tous disparu ! Tous ? Non ahah ! Regarde les Initius avec un dos noir sont encore là !"

    n "Notre histoire va donc continuer avec eux ! Extinction des Initius à dos bleus et rouges."
## MISTER ADN DANS LA PLACE (voix de MELISSA/SORELLE ON SAIT PAS TROP)
    m "Sais-tu pourquoi certains individus disposaient d’un dos noir et d’autres couleurs encore ? Et bien comme toi, ces initius viennent de deux parents, ces deux parents peuvent avoir plusieurs enfants qui seront frères et sœurs."

    m "Comme toi, si tu as un frère ou une sœur, tu as remarqué que vous n’avez pas exactement le même visage ni les mêmes mains, … Et bien c’est qu’on appelle une variation. Une variation fait que chaque personne est unique et à son apparence propre."

    m "Et c’est pareil chez nos Initius et pour toutes les bestioles avec lesquels nous évolueront durant cette histoire ! Certaines variations vont arriver au hasard et modifier très légèrement l’apparence de ton Initius comme par exemple lui donner un dos noir ou rouge et encore plein d’autres choses !"

    m "Mais maintenant, sais-tu ce qu’il s’est passé pour que nos petits amis au dos noir et rouge disparaissent ? C’est dû à un phénomène qui fait que certaines variations sont plus favorables que d’autres. Ainsi dans ce milieu ensoleillé le fait d’avoir un dos bleu ou un dos rouge n’aide pas tes Initius."

    m "Du coup, un phénomène qu’on appelle la sélection naturelle va faire en sorte que seulement ceux qui disposent de la meilleure variation puissent survivre pour que la suite de ta population puisse prospérer en étant la mieux adaptée à son environnement."

    m "Néanmoins, il est peut-être intéressant de donner un rapide coup d’œil aux autres Initius dispersés un peu partout sur la planète."
##Image avec des Initius à dos rouge, bleu, vert et noir se trouvant sur la surface du globe.
    m "Comme tu peux le voir les Initus à dos noir ne sont pas forcément présents partout, certains Initius ayant eu d’autres variations ont su mieux s’adapter à leur environnement propre."

    m "Certaines variations vont donc être plus avantageuses que d’autres alors que dans d’autres environnement celles qui auraient pu lui être défavorable lui confère un avantage !"

    m "D’autres en revanche, ne modifieront rien du tout et seront appelées variations neutres. Bien passons à la suite de ta lignée !"

label vertebre:
    n "On se retrouve quelques millions d’années plus tard, notre population d’Initius a eu beaucoup d’enfants qui eux-mêmes ont eu beaucoup d’enfants qui ont eu beaucoup d’enfants, et ainsi de suite."

    n "Chacun d’entre eux ont eu beaucoup de variations différentes, visibles ou non. Certaines d’entre elles ont été avantageuses et d’autres non selon l’environnement dans lequel ils vivaient."

    n "Pour celles qui ont été avantageuses, elles ont permis à certains d’entre eux de survivre face à leur environnement et de mieux s’adapter" 
    
    n "Ces variations se sont accumulées et ont permis l’apparition de plein d’enfants qui ne ressemblent plus du tout à leurs arrières arrières arrières… grands-parents Initus, c’est tellement lointain que je n’arrive pas à compter." 
    
    n "Dans tous les cas, ces descendants ont, au cours du temps, formé ce qu’on appelle des lignées."
##MISTER ADN SUR LE DANCE FLOOR
    m "Imagine une source d’où jaillit de l’eau qui forme au bout d’un moment un cours d’eau, celui-ci s’écoule alors le long d’un chemin."

    m "Puis, un gros rocher vient séparer ce cours d’eau en deux parties séparée qui ensuite ne se rejoindront plus car de la terre les en empêchent. Maintenant imagine que ce phénomène se répète plusieurs fois."

    m "Ainsi, chaque fois que tu te trouves entre des séparations, tu peux considérer cette portion du chemin comme une espèce. Ensuite, lorsque tu rencontres un rocher qui sépare le cours d’eau, tu vas, après cette séparation, avoir de nouvelles espèces qui sont la descendance de la précédente."

    m "Donc, lorsque tu décides de suivre un seul chemin à partir de la source, c’est ce qu’on appelle une lignée où plusieurs espèces, la prochaine étant une descendante de la précédente, se succèderont au fil du temps. Pour rappel, la source dans cette exemple correspond à LUCA."

    m "Bref ! Retournons dans l’eau observer quelques lointains descendants de nos Initius. On se retrouve tout de suite dans un milieu aquatique dans lequel la diversité du vivant a augmenté de façon importante et dans laquelle plusieurs espèces sont apparues."

    m "Prenons donc deux lignées descendantes aléatoires des Initius, par le hasard des variations, dans une de ces espèces, au fil des générations, une structure ressemblant à un squelette a commencé à apparaître, cette espèce s’appelle les Durus Chordus."

##Apparition de Durus Chordus de couleurs et tailles différentes

    m "Il s’agit de petits animaux se nourrissant principalement de plantes et d’une sorte de planctons vivant sur cette planète. Ils se déplacent comme des serpents de mers mais ils ne vont pas très vite."

    m "Une caractéristique de ce type de déplacement est qu’il leur permet d’aller de la surface la mer comme sur le sol marin, peu profond, dans lequel ils évoluent. Regardons une autre espèce descendante des Initius aléatoire."

    m "En voilà une autre ! Il semble que cette espèce contrairement aux Durus Chordus dispose d’une forme un peu sphérique et d’un aspect mou. Nous les appellerons les Nouillus Asichinus."

##Apparition de Nouillus Asichinus de couleurs et tailles différentes

    m "Encore une fois, ces Nouillus Asichinus sont des petits animaux mais à l’instar des Durus, ils semblent se déplacer par roulement uniquement sur le sol marin. Ils se nourrissent principalement des Durus Chordus et d’autres animaux qui se trouvent trop près du sol."

##Mettre un Durus Chordus et un Nouillus Asichinus l’un à côté de l’autre

    n "Maintenant jeune scientifique, nous te proposons de poursuivre ton aventure évolutive."

    n "En fonction du choix que tu feras, tu suivras les aventures des descendants, et donc de la lignée évolutive, d’une de ces deux espèces." 
    
    menu:
        "Alors qui choisis tu ?"

        "Descendance des Durus Chordus":
            jump durus_chordus
        "Descendance des Nouillus Asichinus":
##MISTER ADN DANS LE GAME
            m "Ahahah ! Je vois que tu as décidé de suivre ton aventure avec l’espèce des Nouillus Asichinus ! Je ne sais pas si tu as remarqué mais encore une fois, parmis ces animaux, des variants existent, ils n’ont pas forcément tous la même couleur et la même taille."

    m "Cependant, te souviens-tu de leur manière de se déplacer ?"

    m "Eh bien, l’origine de leurs mouvements est dû au fait qu’au cours des générations, les ancêtres de ces animaux ont subi une sélection les menant à la formation d’une ébauche d’épines leurs donnant une adaptation leurs conférant une meilleure adhérence et accélération lorsqu’ils roulent."

    m "Et ce qui est intéressant dans notre situation c’est de voir que parmi les populations de Nouillus Asichinus les individus qui mangent principalement les Durus Chordus, ce sont ceux dont les ébauches d’épines sont les plus résistantes leurs permettant ainsi de plus facilement attraper les Durus Chordus."

    m "Ainsi, au cours du temps, on va avoir une sélection naturelle tellement forte que les individus disposant de pseudoépines assez compétentes pour leur permettre de chasser plus vite et efficacement vont être favorisés."

    m "C’est ainsi que des millions d’années plus tard, les descendants de la population Nouillus Asichinus vivant parmi les Durus Chordus vont donner le groupe des Asichinus de ce monde. C’est-à-dire des animaux disposant d’un corps mou mais disposant d’appendices divers !"

    m "Voyons voir un des descendants justement de ces Nouillus Asichinus."

    m "Je tiens tout de même à te rappeler que d’autres Nouillus Asichinus vivant à d’autres endroits avec des proies différentes que Durus Chordus et des conditions environnementales différentes ont pu se développer vers une autre voie évolutive que nous ne verrons pas ici."

    m "Repartons de nouveau faire un voyage dans le temps !"

label habitat:
##vidéo d'un archipel pris sur pixabay
    n "Nous sommes dans la mer d’un archipel où vivent différentes espèces qui commencent tout doucement à se diversifier."

##Image de l'archipel avec l'aquarius (espèce en jeu ici)
    n "Nous avons quitté les Asichinus depuis plusieurs millions d’années et en ce moment les Aquarius dominent l’archipel grâce à leur silhouette élancée tout aussi légère que fiable pour leur assuré une vitesse très utile pour se nourrir ou fuir."

    n "L’eau est transparente et avec une unique sorte d’algue dans le fond qui remontent si haut qu'elles recouvrent la surface de l’eau. Avec un climat tempéré et un beau soleil qui brille de mille feux, nos aqua-rius asichinus sont épanouis dans ce monde qui est le leur."

    n "Notre population d’Aquarius Asichinus endémique à cette région vit de façon prospère depuis 1000 ans sans subir de réelle mutation majeur, toutefois parmi l’espèce subsiste une dérive de couleur spécifique séparant notre Aquarius, des individus vert et rouge vivant ensemble sur un même pied d’égalité."

##MISTER ADN IS BACK
    m "Il n’est pas si rare de voir au sein d’une même espèce des variations de couleurs, ce phénomène s’appelle la variation génétique et cela existe aussi sur notre planète."

##Retour image précédente
    n "Leur environnement semblait avoir trouvé une certaine stabilité, quand soudain un évènement va venir troubler la quiétude de leur lieu de vie."

##Vidéo volcan
    n "Cette événement va venir perturber notre population d’aquarius asichinus, en effet plusieurs volcans océaniques vont entrer en éruption cela aura pour effet de chauffer d’avantage l'eau et lui donner une couleur verte à cause des cendres riches en particules de cuivre"

##Image précédente mais teintée en vert
    n "Notre Aquarius Asichinus dont l’espèce est composée d’individus vert et rouge va devoir s’adapter à un nouvel environnement."

    n "La population verte, favorisée par la nouvelle teinte de l’eau aura plus facile à chasser alors que les rouges, handicapés par leur couleur, ne peuvent plus concurrencer leurs congénères."

    n "Notre invertébré a un style de chasse très singulier, il fonce sur tous types de proie, que ce soit des petits unicellulaires ou même d’autres Aquarius plus petits."

##Bien montrer une image ou un petit Aquarius se fait courser par un grand

    n "Ils misent tout sur leur vitesse et la surprise de ce fait les rouges qui sont visibles au loin à cause de la nouvelle teinte de l’eau sont fort impactés par ce changement comparé aux verts."

    n "Au cours des générations la population de rouge ayant de meilleurs chances de survie en périphérie des lieux d’éruptions va voir son nombre augmenter dans les zones peu profondes et proches des côtes."

    n "Les aquarius rouges situés au large et proches des volcans vont mourir car ils ne sont pas adaptés à cet environnement ce qui va faire qu’au cours du temps nous n’allons plus retrouver un rouge dans ses zones."
##Image d’un Aquarius asichinus rouge sur une plage

    n "Certains rouges présentent des caractéristiques particulières comme le stockage d’oxygène sous leur peau ou alors l’apparition d’écailles ventrales qui leur confère une adhésion parfaite sur le sol et bien d’autres petites mutations parfois inutile ou handicapante."

    n "Les générations d’individus les mieux adaptées vont continuer de perfectionner ces caractères pour faciliter leurs nouvelles interactions avec la surface."

##MISTER ADN AUX PLATINES

    m "L’évolution n’est pas dirigiste, c’est une succession d’événements qui provoquent des mutation positif ou négatif. Ce phénomène ne peut pas être contrôlé."

    m "A force de faire des va-et-vient entre la plage et l’eau, après plusieurs centaines de millions d’années certains vont être capable de rester plus longtemps sur le sable et ainsi de suite jusqu’à ce qu’il soit capable de s’établir définitivement sur la côte."

    m "Ce processus a pris un temps considérable et ceux qui sont resté dans les eaux profondes sont morts de faim et du sida des profondeurs."

    m "En moins de cent ans nous allons observer une disparition des rouges au large, une espèce qui n’est plus adaptées à son environnement va s’éteindre plus vite qu’elle n’est apparue et une augmentation de leur population sur la côte car ils pullulent dans ce nouvelle environnement qu’ils se sont durement approprié."

    menu:
        "Qui voulez-vous suivre ?"

        "Les individus verts qui vont continuer leur vie dans la mer":
            jump aquarius_vert
        "Suivre les rouges à la conquête des plages de l’archipel":
##MISTER ADN CE GRAND FOU
            m "Tu vas continuer ton aventure avec la population d’individus rouges."
    
    m "Comme t’as pu le comprendre nos Aquarius rouges ne se retrouvent plus qu’aux extrémités des côtes et sur le sable."

    m "En effet les individus au loin n’ont pas su s’adapter mais pour ceux près de la plage après un long temps d’adaptation, ils vont pouvoir s’épanouir et peut-être conquérir la terre ferme grâce à de nouveaux atouts acquis et perfectionné au cours de nombreuse générations et de mutations."

    return
   
