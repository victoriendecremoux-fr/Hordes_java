public class Batiment{
    
    private String nom;
    private int lvlMax;
    
    private int lvl;
    private int defense;
    private int tempsConstructionMinutes;
    private Inventaire ressourcesRequises;

    public Batiment(String nom, int lvl, int lvlMax, int defense, double tempsConstructionMinutes, Inventaire RessourcesRequises){
        this.nom = nom;
        this.lvl = lvl;
        this.lvlMax = lvlMax;
        this.defense = defense;
        this.tempsConstructionMinutes = tempsConstructionMinutes;
        this.ressourcesRequises = ressourcesRequises;
    }

    public int getDefense(){
        return this.defense;
    }

    public int getTempsConstructionMinutes(){
        return this.tempsConstructionMinutes;
    }

    public int getLvl(){
        return this.lvl;
    }

    public int getLvlMax(){
        return this.lvlMax;
    }


    public Inventaire getRessourcesRequises(){
        return this.ressourcesRequises; //return new Inventaire(ressourcesRequises);
    }

    public void lvlUp(){
        if(this.lvl==this.lvlMax){
            throw BatimentDejaLvlMaxException;
        }
        else{
            this.lvl++;
        }
    }

    public void lvlDown(){
        if(this.lvl==0){
            throw BatimentLvlZeroException;
        }
        else{
            this.lvl--;
        }
    }

    
