public static void main(String [ ] args){
    
    Ville ville = new Ville();

    while(ville.getJoueur().getEstVivant()){
        
        ville.arriveeBob();
        ville.decouvertePlanBatiment();
        ville.decouverteCompetence();
        ville.actionBatimentProduction();
        
        while(ville.getJoueur().getEstVivant() && ville.getJour().getEstEncourt()){
            
            ville.calculVitesses();
            ville.affichageActions();
            ville.selectionEtRealisationAction();
            ville.apparitionEventuelleTempete();
        }
        
        ville.actionBobs();
        ville.actionRonces();
        ville.estAttaquee();
    }
    
