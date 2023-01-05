                                                              7. Reverse Integer 
 Link:https://leetcode.com/problems/reverse-integer/

long long reverse(long long x){
    long long rev=0,num,rem;
    if(x%10==0){
        num=x/10;
        while(num!=0){
            rem=num%10;
            rev=rev*10+rem;
            num/=10;
        }
        
    }
    if(x%10!=0){
        num=x;
        while(num!=0){
            rem=num%10;
            rev=rev*10+rem;
            num/=10;      
        }
        
    }
    if(rev>2147483648 || rev<-2147483648){
        return 0;
    }
    else{
         return rev;
    }
   
}
