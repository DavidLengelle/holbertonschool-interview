#include "island_perimeter.h"

/**
 * island_perimeter - Computes the perimeter of the island described in grid
 * @grid: 2D array where 0 is water and 1 is land
 * @height: number of rows of the grid
 * @width: number of columns of the grid
 *
 * Return: The perimeter of the island
 */
int island_perimeter(int **grid, int height, int width)
{
	int r, c, perimeter;

	perimeter = 0;
	for (r = 0; r < height; r++)
	{
		for (c = 0; c < width; c++)
		{
			if (grid[r][c] == 1)
			{
				if (r == 0 || grid[r - 1][c] == 0)
					perimeter++;
				if (r == height - 1 || grid[r + 1][c] == 0)
					perimeter++;
				if (c == 0 || grid[r][c - 1] == 0)
					perimeter++;
				if (c == width - 1 || grid[r][c + 1] == 0)
					perimeter++;
			}
		}
	}
	return (perimeter);
}
