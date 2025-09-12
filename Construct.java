public class Construct
{
       Construct()
       {
            System.out.println("constructor is created");
       }
       Construct(int a,int b)
       {
           System.out.println(a+b);
       }
       public static void main(String args[])
       {
              Construct exe1=new Construct();
              Construct exe2=new Construct(10,20);
              
       }
}