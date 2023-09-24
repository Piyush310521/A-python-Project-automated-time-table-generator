package test ;

public class Multi implements Runnable {

	public void run()
	{
		for(int i =1; i<=10;i++)
		{
			System.out.println("Value of i is "+i);
		    try
		    {
		    	Thread.sleep(1000);
		    }
		    catch(Exception e)
		    {}
		}
	}
	public static void main(String[] args) {
         Multi t = new Multi();
         Thread thr = new Thread(t);
         thr.start();
	}

}
