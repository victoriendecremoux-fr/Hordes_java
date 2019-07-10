public class FonctionsUtiles{
    
    public static String[] egaliser(String[] listeNoms, int nbEspaces){
        String listeNomsEgalises[listeNoms.length];
        int longueurMax = longueurMax(listeNoms);
        for(int i = 0, i < listeNoms.length, i++){
            listeNomsEgalises[i] = listeNoms[i] + multiplier(" ", nbEspaces +(longueurMax - listeNoms[i].length));
        }    
        return listeNomsEgalises;
    }

    public static String multiplier(String str, int nb){
        //verifier que nb > 1
        
        String stringMultipliee = str;
        for(int i = 1, i < nb, i++){
            stringMultipliee = stringMultipliee + str;
        }
        return stringMultipliee;
    }



    public static int longueurMax(String[] listeNoms){
        //verifier qu il y a au moins un element
        
        int longeurMax = listeNoms[0].length;
        for(String nom : listeNoms){
            if(nom.length > longueurMax)
                longueurMax = nom.length;
        }
        return longueurMax;
    }

    
    public static int longueurMax(double[] listeNombres){
        return longueurMax(nombreEnString(listeNombres));

    }


    public static String[] nombreEnString(double[] listeNombres){
        String listeString[listeNombres.length];
        for(int i = 0, i < listeNombres.length, i++){
            listeString[i] = Double.toString(listeNombres[i]);
        }
        return listeString;
    }


    public static String minEnHeure(int nbMinutes){ // 373 minutes -> 6:13
        heures = nbMinutes / 60;
        minutes = nbMinutes - heures*60;
        if(minutes < 10)
            return heures + ":0" + minutes;
        else
            return heures + ":" + minutes;                                              
    }

    public static double defenseReelle(int defenseBase, Ville ville){
        return defenseReelle;
    }

    public static int tempsReel(int tempsMinutesBase, Ville ville){
        return tempsMinutesReel;
    }
        
        
