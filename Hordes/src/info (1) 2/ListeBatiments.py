public class ListeBatiments{
    private Batiment listeBatiments[1000];
    private int indice = 0;

    public void ajouter(Batiment batiment){
        this.listeBatiments[indice] = batiment;
        this.indice += 1;
    }

    public void enlever(int indice, ListeBatiment listeBatiments){
        
        listeBatiments.ajouter(this.listeBatiments[indice];
        for(int i = indice, i < this.indice, i++){
            this.listeBatiments[i] = this.listeBatiments[i+1];
        }
        this.indice -= 1;
    }

    public void afficher(){
        String listeNoms[this.indice + 1];
        String listeDefense[this.indice + 1];
        String listeTempsConstruction[this.indice + 1];
        String listeLvl[this.indice + 1];
        String listeLvlMax[this.indice + 1];
        String listeRessources[this.indice + 1];

        listeNoms[0] = "Buildings";
        listeDefense[0] = "Defense";
        listeTempsConstruction[0] = "Time Required";
        listeLvl[0] = "Lvl";
        listeLvlMax[0] = "Lvl Max";
        listeRessources[0] = "Ressources";
        
        //construction des listes
        for(int i = 1, i < this.indice + 1, i++){
            
            listeNoms[i]                = this.listeBatiments[i-1].getNom();
            listeDefense[i]             = Double.toString(defenseReelle(this.listeBatiments[i-1].getDefense()));
            listeTempsConstruction[i]   = minEnHeure(tempsReel(this.listeBatiments[i-1].getTempsConstructionMinutes()));
            listeLvl[i]                 = Integer.toString(this.listeBatiments[i-1].getLvl());
            listeLvlMax[i]              = Integer.toString(this.listeBatiments[i-1].getLvlMax());
            listeRessources[i]          = this.listeBatiments[i-1].getRessourcesRequises().toString();
        }

        egaliser(listeNoms,5);
        egaliser(listeDefense,5);
        egaliser(listeTempsConstruction,5);
        egaliser(listeLvl,5);
        egaliser(listeLvlMax,5);
        egaliser(listeRessources,5);

        //affichage
        for(int i = 0, i < this.indice, i++){
            System.out.print(listeNoms[i] + listeDefense[i] + listeTempsConstruction[i] + listeLvl[i] + listeLvlMax[i] + listeRessources[i]);
            if(i == 1)
                System.out.println()
        }
