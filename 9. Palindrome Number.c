                                                                9. Palindrome Number          
  Link:https://leetcode.com/problems/palindrome-number/
      
 bool isPalindrome(long long x){
    long long rev=0;
    long long num=x;
    if(x<0){
        return false;
    }
    while(x!=0){
        long rem=x% 10;
        rev=rev*10+rem;
        x=x/10;
    }
    return rev==num;
}
