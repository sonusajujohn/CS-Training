#include<stdio.h>
int main()
{
     int a[]={10,7,8,8,10,3,2};
     int size=7;
     for(int i=0;i<size-1;i++)
     {
         for(int j=i+1;j<size;j++)
         {
             if(a[i]==a[j])
             {
                 for(int k=j;k<size;k++)
                       {     a[k]=a[k+1];
                               
                       }
                       size--;
                               j--;
                  }
         }
     }
     for (int l=0;l<size;l++)
     {
         printf("%d\t",a[l]);
     }
}     