package lfpc;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;


public class Main {

    public static void main(String[] args) throws FileNotFoundException {
        String Sn,St , T;
        HashMap<String , HashMap<String, String>> way = new HashMap<String , HashMap<String, String >>();

        String path = "D:/lfpc/lab2/src/lfpc/in.txt";
        File file = new File(path);
        Scanner input = new Scanner(file);

        Sn = input.nextLine();
        Sn = input.nextLine();
        T = input.nextLine();
        String S1=" ",S2=" ",S3=" ";

        while (input.hasNext()){
            S1=input.next();
            if (S1.charAt(0)>96){
                while(true){
                    S2= input.next();
                    if (S2.charAt(0)>96)
                        break;
                }
                while(true) {
                    S3 = input.next();
                    if (S3.charAt(0) > 96)
                        break;
                }
                if (way.containsKey(S1)){
                    if (way.get(S1).containsKey(S2)){
                        String add, el;
                        el=way.get(S1).get(S2);
                        if (el.charAt(1)>S3.charAt(1)){
                            add=S3+el;
                        }
                        else{
                            add=el+S3;
                        }
                        way.get(S1).put(S2,add);
                    }
                    else {
                        way.get(S1).put(S2,S3);
                    }
                }
                else {
                    HashMap<String , String > sp = new HashMap<String ,String>();
                    sp.put(S2,S3);
                    way.put(S1,sp);
                }
            }
        }
        Compute c = new Compute(way);
        c.find();
        c.print();
    }
}
