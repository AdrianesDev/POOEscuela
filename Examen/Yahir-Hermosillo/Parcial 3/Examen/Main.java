public class Main {
    public static void main(String[] args) {
        // Probando Ejercicio 1
        Mario mario = new Mario();
        mario.acelerar();
        
        Bowser bowser = new Bowser();
        bowser.acelerar();
        
        // Probando Ejercicio 2
        Toad toad = new Toad();
        toad.lanzarPlatano();
        toad.lanzarPlatano();
        toad.lanzarPlatano();
        toad.lanzarPlatano(); 
        toad.recargarPlatanos();
        
        // Probando Ejercicio 3
        Kart kart = new Kart();
        Moto moto = new Moto();
        
        kart.descripcion();
        moto.descripcion();
        
        // Probando Ejercicio 4
        Luigi luigi = new Luigi();
        Yoshi yoshi = new Yoshi();
        
        luigi.saludar();
        yoshi.saludar();
    }
}
