//Codigo en el lenguaje de apex.
    integer max = 6;
    integer min = 0;
    integer casilla=0;

    System.debug('Comienza el juego');
    while(casilla<25){
        integer dado =Integer.valueof((Math.random() *(max-min)+min));
        System.debug('El dado ha arrojado ' + dado);
        casilla= casilla+dado;
        if(casilla==3){ 
            casilla=11;
            System.debug('usted esta en la casilla 3 sube por la escalera a la casilla ' + 11);
        }else if(casilla==6){
            System.debug('usted se encuentra en la casilla ' + casilla); 
            casilla=17;
            System.debug('usted esta en la casilla 6 sube por la escalera a la casilla ' + 17);
        }else if(casilla==9){
            System.debug('usted se encuentra en la casilla ' + casilla); 
            casilla=18;
            System.debug('usted esta en la casilla 9 sube por la escalera a la casilla ' + 18);
        }else if(casilla==10){
            System.debug('usted se encuentra en la casilla ' + casilla); 
            casilla = 12;
            System.debug('usted esta en la casilla 10 sube por la escalera a la casilla ' + 12);
        }else if(casilla==14){
            System.debug('usted se encuentra en la casilla ' + casilla); 
            casilla = 4;
            System.debug('usted esta en la casilla 14 baja por la serpiente a la casilla ' + 4);
        }else if(casilla==19){
            System.debug('usted se encuentra en la casilla ' + casilla); 
            casilla = 8;
            System.debug('usted esta en la casilla 19 baja por la serpiente a la casilla ' + 8);
        }else if(casilla==22){
            System.debug('usted se encuentra en la casilla ' + casilla); 
            casilla = 20;
            System.debug('usted esta en la casilla 22 baja por la serpiente a la casilla ' + 20);
        }else if(casilla==24){
            System.debug('usted se encuentra en la casilla ' + casilla); 
            casilla = 16;
            System.debug('usted esta en la casilla 24 baja por la serpiente a la casilla ' + 16);
        }else if(casilla>25){
            System.debug('el juego termino');
            System.debug('usted se encuentra en la casilla ' + casilla); 
        }else{
            System.debug('usted se encuentra en la casilla ' + casilla); 
        }
        
    
    }
