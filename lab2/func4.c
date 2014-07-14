#include <stdio.h>

int func4(int x) {
  return x > 1 ? func4(x - 1) + func4(x - 2) : x;
}

int main(int argc, char *argv[]) {
  printf("%i\n", func4(9));

  return 0;
}

