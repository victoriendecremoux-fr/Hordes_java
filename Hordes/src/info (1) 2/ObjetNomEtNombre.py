public class ObjetNomEtNombre{
    private String nom;
    private int nombre;

    public ObjetNomEtNombre(String nom, int nombre){
        this.nom = nom;
        this.nombre = nombre;
    }

    public String getNom(){
        return this.nom;
    }

    public String getNombre(){
        return this.nombre;
    }

    public void ajouter(int nb){
        if(this.nombre + nb >= 0)
            this.nombre += nb;
        else
            throw PasAssezDeRessourcesARetirerException;
    }

    public String toString(){
        return this.nombre + " " + this.nom;
    }


    
