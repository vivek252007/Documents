/*#include <stdio.h>

main() {
  FILE *fp;

  fp = fopen("temp.txt", "w+");
  fprintf(fp, "This is testing for fprintf...\n");
  fputs("This is testing for fputs...\n", fp);
  fclose(fp);
}*/

/*#include <stdio.h>

int scmp( char *s1, char *s2 ) {
    while(*s1 != '\0' && *s1 == *s2) {s1++; s2++;}
    return(*s1 - *s2);
}
main() {

   FILE *fvec, *fvocab;
   char buff_vec[600],buff_vocab[50];
   int i,c;
	
   fvec = fopen("vector.txt", "r");
   fvocab = fopen("vocab.txt","r");

	if (fvocab) {
	   while ((c = getc(fvocab)) != EOF){
	       fscanf(fvocab, "%s", buff_vocab);
	       fgets(buff_vocab, 600, (FILE*)fvocab);
	       printf("Vocab : %s \n", buff_vocab );
	}
	   fclose(fvocab);
	}

   fscanf(fvec, "%s", buff_vec);
   printf("Vector : %s \n", buff_vec );
   fscanf(fvec, "%s", buff_vec);
   printf("Vector : %s \n", buff_vec );
   fscanf(fvocab, "%s", buff_vocab);
   printf("Vocab : %s \n", buff_vocab );
   if (!(scmp(buff_vec,buff_vocab))){
   ifgets(buff_vec, 600, (FILE*)fvec);
   }
   
   fclose(fvec);

}
*/
#include <stdio.h>
 
int main()
{
  FILE *fvocab = fopen("vocab.txt", "r");
  int ch = '0';
  char buff_vec[600],buff_vocab[50];
  while (ch != EOF) 
  {
    /* display contents of file on screen */
/*    putchar(ch); 
*/	fgets(buff_vocab, 600, (FILE*)fvocab);
	printf("Vocab : %s \n", buff_vocab );
 
    ch = fgetc(fvocab);
  }
   
  if (feof(fvocab))
     printf("\n End of file reached.");
  else
     printf("\n Something went wrong.");
  fclose(fvocab);
     
  getchar();
  return 0;
}
