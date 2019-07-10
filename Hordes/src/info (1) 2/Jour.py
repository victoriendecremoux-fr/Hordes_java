public class Jour{
    private double heureEnMinute = 360;
    private int nbJour = 1;

    public void ajouterXMinutes(double nbMinutes){
        this.heureEnMinute += nbMinutes;
    }

    public boolean getEstEnCourt(){
        return this.heureEnMinute < 22*60;
    }

    public void suivant(){
        this.heureEnMinute = 360;
        this.nbJour++;
    }

    public String getHeureEnH(){ //a tester: attention aux operations entre differents types
        int h = (int)this.heureEnMinute / 60;
        int minutes = this.heureEnMinute - h*60;
        return h + "h" + this.heureEnMinute;
    }


}
