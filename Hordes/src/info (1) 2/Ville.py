public class Ville{
    private double defense;

    private ListeBobs listeBobs;
    
    private ListeBatiments listeBatimentsConstruits;
    private ListeBatiments listePlansDecouverts;
    private ListeBatiments listePlansADecouvrir;
    
    private Inventaire inventaire;

    private Jour jour;

    public void conctruction(int indice, booleen estDanslistePlansDecouverts){
        if(estDanslistePlansDecouverts){
            this.listePlansDecouverts[indice].lvlUp();
            this.jour.ajouterXMinutes(this.listePlansDecouverts[indice].getTempsConstructionMinutes())
            this.inventaire.soustraction(this.listePlansDecouverts[indice].getRessourcesRequises())
            this.defense += this.listePlansDecouverts[indice].getDefense()
            
            this.listePlansDecouverts.enlever(indice, listeBatimentsConstruits);
            }
    }
