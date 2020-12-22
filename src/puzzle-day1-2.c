#include <stdio.h>
#include <stdlib.h>

int main()
{
	FILE *input = fopen("numbers.txt", "r");
	if (input == NULL) {
		fprintf(stderr, "Can't open input file!\n");
		exit(EXIT_FAILURE);
	}

	unsigned long numbers[4096];
	size_t number_count = 0;
	unsigned long sum = 0;
	unsigned long remainder = 0;
	unsigned long multiplication = 0;
	do {
		int ret = fscanf(input, "%lu", &numbers[number_count]);
		if (ret != 1 || ret == EOF) {
			break;
		}
		number_count++;
	} while (1);

	fprintf(stdout, "I've read %zu numbers!\n", number_count);
	for (size_t i = 0; i < number_count - 2; ++i) {
		for (size_t j = i + 1; j < number_count -1; ++j) {
			for (size_t k = j + 1; k < number_count; k++) {
				if (numbers[i] + numbers[j] + numbers[k] == 2020) {
					multiplication = numbers[i] * numbers[j] * numbers[k];
					break;
				}
			}
		}
	}

	fprintf(stdout, "multiplication: %lu\n", multiplication);

	return 0;
}
	
