package lfpc;

import java.util.HashMap;

public class Compute {
    HashMap<String , HashMap<String, String>> way = new HashMap<String , HashMap<String, String >>();
    Compute(HashMap<String , HashMap<String, String>> in){
        way=in;
    }
    void find(){
        boolean restart=false;
        for ( String key : way.keySet()){
            restart=false;
            for( String key1 : way.get(key).keySet()){
                if (way.get(key).get(key1).length()>2){
                    boolean check ;
                    check=true;
                    for (String key2 : way.keySet()){
                        if (way.get(key).get(key1).equals(key2)){
                            check=false;
                            break;
                        }
                    }
                    if(check){
                        splitting(way.get(key).get(key1));
                        restart=true;
                    }
                }
            }
            if(restart)break;
        }
        if (restart)find();
    }

    void splitting(String a){
        for (int i=0;i<a.length();i+=2){
            search(a.substring(i,i+2) , a);
        }
    }

    void search(String a,String sp){
        boolean restart=false;
        for ( String key : way.keySet()){
            restart=false;
            if (key.equals(a)){
                for ( String key1 : way.get(key).keySet()){
                    adding(sp , key1 , way.get(key).get(key1));
                    restart=true;
                }
            }
            if (restart)break;
        }
    }

    void adding(String key1 , String key2 , String last  ){
        if (way.containsKey(key1)){
            if (way.get(key1).containsKey(key2)){
                String add, el;
                el=way.get(key1).get(key2);
                if (el.charAt(1)>last.charAt(1)){
                    add=last+el;
                }
                else{
                    add=el+last;
                }
                way.get(key1).put(key2,add);
            }
            else {
                way.get(key1).put(key2,last);
            }
        }
        else {
            HashMap<String , String > sp = new HashMap<String ,String>();
            sp.put(key2,last);
            way.put(key1,sp);
        }
    }
    void print (){
        matrix print = new matrix(way);
        print.computeMatrix();
    }
}
