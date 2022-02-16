package lfpc;

import java.util.HashMap;

public class matrix {
    HashMap<String , HashMap<String, String>> way = new HashMap<String , HashMap<String, String >>();
    matrix(HashMap<String , HashMap<String, String>> a ){
        way=a;
    }
    void computeMatrix(){
        int l1=0,l2=0;
        for (String key : way.keySet()){
            l1++;
        }
        String Ts="";
        for (String key : way.keySet()){
            int max;
            max=0;
            for(String key1 : way.get(key).keySet()){
                max++;
            }
            if (max>l2){
                l2=max;
                for(String key1 : way.get(key).keySet()){
                    Ts+=key1;
                }
            }
        }
        String[][] matrix=new String[l1+1][l2+2];
        System.out.println(l1+" "+l2);
        int i=1;
        for ( String key : way.keySet()){
            matrix[i][0]=key;
            i++;
        }
        for ( i=1;i<Ts.length()+1;i++){
            matrix[0][i]=Character.toString(Ts.charAt(i-1));
        }
        for (i=1;i<l1+1;i++){
            for (int j=1;j<l2+1;j++){
                if (way.get(matrix[i][0]).get(matrix[0][j])!=null){
                    matrix[i][j]=way.get(matrix[i][0]).get(matrix[0][j]);
                }
            }
        }
        printMatrix(matrix , l1, l2);
    }
    void printMatrix(String[][] matrix,int l1,int l2){
        for(int i=0;i<l1+1;i++){
            for (int j=0;j<l2+1;j++){
                if (matrix[i][j]!=null){
                    System.out.format("%10s", matrix[i][j]);
                }
                else{
                    System.out.format("%10s", "_");
                }
            }
            System.out.println();
        }
    }
}
