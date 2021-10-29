function start(){
    //valores constantes del dado
    const max = 6;
    const min = 0;
    //variable donde se guarda la información de la casilla
    var casilla=0;

    console.log("Comienza el juego");
    //ciclo que se realiza mientras el jugador no llegué a la casilla final.
    while(casilla<25){
        // variable donde se guarda el valor random que lanzara el dado
        var dado = Math.ceil(Math.random()*(max-min)+min);
        console.log("El dado ha arrojado " + dado);
        //variable donde se guarda la información de la casilla
        casilla= casilla+dado;
        //condiciones para validar las casillas donde se asciende
        if(casilla==3){ 
            casilla=11;
            console.log("usted esta en la casilla 3 sube por la escalera a la casilla " + 11);
        }else if(casilla==6){
            console.log("usted se encuentra en la casilla " + casilla); 
            casilla=17;
            console.log("usted esta en la casilla 6 sube por la escalera a la casilla " + 17);
        }else if(casilla==9){
            console.log("usted se encuentra en la casilla " + casilla); 
            casilla=18;
            console.log("usted esta en la casilla 9 sube por la escalera a la casilla " + 18);
        }else if(casilla==10){
            console.log("usted se encuentra en la casilla " + casilla); 
            casilla = 12;
            console.log("usted esta en la casilla 10 sube por la escalera a la casilla " + 12);
        //condiciones para validar las casillas por donde se desciende
        }else if(casilla==14){
            console.log("usted se encuentra en la casilla " + casilla); 
            casilla = 4;
            console.log("usted esta en la casilla 14 baja por la serpiente a la casilla " + 4);
        }else if(casilla==19){
            console.log("usted se encuentra en la casilla " + casilla); 
            casilla = 8;
            console.log("usted esta en la casilla 19 baja por la serpiente a la casilla " + 8);
        }else if(casilla==22){
            console.log("usted se encuentra en la casilla " + casilla); 
            casilla = 20;
            console.log("usted esta en la casilla 22 baja por la serpiente a la casilla " + 20);
        }else if(casilla==24){
            console.log("usted se encuentra en la casilla " + casilla); 
            casilla = 16;
            console.log("usted esta en la casilla 24 baja por la serpiente a la casilla " + 16);
        //condiciones para saber si el jugador esta en o supero la casilla 25
        }else if(casilla>25){
            console.log("usted esta en la casilla " + 25); 
            console.log("el juego termino");
        }else if(casilla>=25){
            console.log("usted ha superado la casilla " + 25); 
            console.log("el juego termino");
        }else{
        //impresión donde se retroalimenta al usuario, sobre la casilla donde esta ubicado
            console.log("usted se encuentra en la casilla " + casilla); 
        }
        
    
    }


};