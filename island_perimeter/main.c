#include <stdio.h>
#include "island_perimeter.h"

/**
 * main - Builds a grid and prints the perimeter of its island
 *
 * Return: Always 0
 */
int main(void)
{
	int row0[] = {0, 0, 0, 0, 0, 0};
	int row1[] = {0, 1, 0, 0, 0, 0};
	int row2[] = {0, 1, 0, 0, 0, 0};
	int row3[] = {0, 1, 1, 1, 0, 0};
	int row4[] = {0, 0, 0, 0, 0, 0};
	int *grid[5];

	grid[0] = row0;
	grid[1] = row1;
	grid[2] = row2;
	grid[3] = row3;
	grid[4] = row4;
	printf("%d\n", island_perimeter(grid, 5, 6));
	return (0);
}
