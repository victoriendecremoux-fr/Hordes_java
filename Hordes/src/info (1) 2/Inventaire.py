public class Inventaire{

    private ObjetNomEtNombre listeInventaire[100];
    private int indice = 0;
    
    public void ajouter(int nb, int indice){
        if(this.indice >= indice)
            this.listeInventaire[indice].ajouter(nb);
        else
            throw IndiceOutOfIndexException;
    }

    public void ajouter(ObjetNomEtNombre objetNomEtNombre){
        this.listeInventaire[indice] = objetNomEtNombre;
        this.indice++;
    }

    
    public boolean memeType(Inventaire inventaire){
        if(this.getIndice() != inventaire.getIndice()){
            return False;
        }
        else{
            for(int i = 0, i < this.getIndice(), i++){
                String nomInventaire1 = this.getListeInventaire()[i].getNom();
                String nomInventaire2 = inventaire.getListeInventaire()[i].getNom();
                if(!nomInventaire1.equals(nomInventaire2))
                    return False;
            }
            return True;
        }
    }



    public void moins(Inventaire inventaire){
        if(this.memeType(inventaire)){
            for(int i = 0, i < this.indice, i++){
                this.ajouter(-inventaire.getListeInventaire().getNombre());
            }
        }
        else{
            throw ComparaisonImpossibleException;
        }
    }


    public ObjetNomEtNombre[] getListeInventaire(){
        return this.listeInventaire;
    }

    public int getIndice(){
        return this.indice;
    }

    public String toString(){
        String stringInventaire = "";
        for(int i = 0, i < indice, i++){
            stringInventaire += this.listeInventaire[i].toString();
            if(i != indice - 1)
                stringInventaire += "|";
        }
    }

    public void afficher(){
        for(int i = 0, i < indice, i++){
            System.out.println(this.listeInventaire[i].toString());
        }

}
