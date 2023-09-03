#include <stdio.h>
#include <locale.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <stdbool.h>

char linha[100],linha2[10],palavra_usuario[10];
int cont,sorteio,verificador,tam1, tentativas = 0,z;
double time_spent = 0.0;

int sorteio_palavra(FILE*arquivo){
    cont = 0;
    verificador = 1;
    
	srand(time(NULL));

    arquivo = fopen("dicionario.txt","r");


    while(NULL != fgets(linha,100,arquivo)){
        cont++;
    }
    fclose(arquivo);

    sorteio = rand() % cont;
   	arquivo = fopen("dicionario.txt", "r");
    while(verificador-1!=sorteio){
    	NULL != fgets(linha2,100,arquivo);
    	verificador++;
	}
	fclose(arquivo);
	tam1 = strlen(linha2);
    return tam1;
}

void palavra(FILE*arquivo){
	while(true){
		sorteio_palavra(arquivo);
		if(tam1 == 6){
			break;
		}	
	}
}

int dic(char palavra[], FILE*arquivo) {
	char aux[10];
	int c;
	for(c = 0; c <= cont; c++){
    	fgets(aux,10,arquivo);
    	if(strncmp(palavra, aux, 5) == 0) {
    		return 1;
    		break;
		}
	}
	return 0;
	
}

void scores(char palavra[],int tentativas, double tempo){
    char nome[50];

    FILE *arquivo;
    arquivo = fopen("scores.txt", "a+");


    printf("\nDigite seu nome: \n");
    scanf("%s", nome);
    fprintf(arquivo,"Nome: %s\n", nome);
    fprintf(arquivo,"Palavra: %s", palavra);
    fprintf(arquivo,"Tentativas: %d\n", tentativas);
    fprintf(arquivo,"Tempo: %g segundos\n", tempo);
    fprintf(arquivo, "------------------------------\n");

    fclose(arquivo);
    printf("Arquivo criado com sucesso!\n");
}

int game(char palavra[]){
	int i, j, n, z ;
	char teste[6] = "^^^^^"; 
	FILE*arquivo;
	
	while(tentativas < 6) {
		arquivo = fopen("dicionario.txt","r");
		char amostra[6] = "xxxxx";
		int positivo = 0;
		
		printf("\nDigite seu palpite:\n");
		gets(palavra);
		z = dic(palavra, arquivo);
		fclose(arquivo);
		
		if(z) {
			for(i=0;i<5;i++){
				for(j=0;j<5;j++){
					if(palavra[i] == linha2[j]){
						if(i == j){
							amostra[i] = '^';
						}else {
							if(amostra[i] == '^'){
								continue;
							}else {
								amostra[i] = '!';
							}
					
						}
					}
			
				}
			}
		
			tentativas++;
			n = strcmp(amostra, teste);
	
			if(n == 0) {
				printf("\nParabéns vc acertou em %d tentativas\n", tentativas);
				return 1;
			}
	
			printf("%s", amostra);
		
			if (tentativas == 6) {
				printf("\nSuas tentativas acabaram! A palavra certa era: %s", linha2);
				return 0;
			}
		}else {
			printf("Essa palavra não existe no dicionário");
		}	
	}
}

int main(){
    setlocale(LC_ALL, "Portuguese");

    FILE*arquivo;
    
    printf("----------------------------------------\n");
    printf("MACK-TERMOO: Jogo de advinhação!\n");
    printf("(Jogo feito por Antônio, Henrique e Joaquim.)\n");
    printf("----------------------------------------\n");

	palavra(arquivo);
	
	clock_t begin = clock();
	z = game(palavra_usuario);
	clock_t end = clock();
	
	time_spent += (double)(end - begin) / CLOCKS_PER_SEC;
	
	if(z) {
		scores(linha2, tentativas, time_spent);
	}
	
    fclose(arquivo);
    
    
	
	
    return 0;
}
