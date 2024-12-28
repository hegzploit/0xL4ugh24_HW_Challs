#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main() {
  // Specify the environment variable you want to print
  const char *env_var_name = "FLAG";

  // Retrieve the value of the environment variable
  char *env_var_value = getenv(env_var_name);

  char correct_pass[] = "562951413";
  char inp[10] = {0};

  puts("Please enter the pin:");
  if (scanf("%s", inp) != 1) { // Check scanf return value
    puts("Error: Invalid input");
    return 1;
  }

  // Check if the input length exceeds the correct password length
  if (strlen(inp) > strlen(correct_pass)) {
    puts("Error: Input is longer than the allowed password length.");
    return 1;
  }
  // Check if the input is numeric
  for (size_t i = 0; i < strlen(inp); i++) {
    if (!isdigit((unsigned char)inp[i])) {
      puts("Error: Only numeric inputs are allowed.");
      return 1;
    }
  }
  size_t pass_len = strlen(correct_pass);
  for (size_t i = 0; i < pass_len; i++) {
    if (inp[i] != correct_pass[i]) {
      break;
    }
    usleep(100000);
  }

  if (strcmp(inp, correct_pass) == 0) {
    puts("Congratulations! You entered the correct password.");
    printf("The flag is: %s\n", env_var_value);
  }

  puts("Analyzing...");
  return 0;
}
