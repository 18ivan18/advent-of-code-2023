#include <iostream>

enum Direction
{
    UP,
    DOWN,
    RIGHT,
    LEFT
};

char input[150][150];
int start_x, start_y;
int end_x, end_y;

int longest_path = 0;

bool is_valid(int row, int col, int direction)
{
    switch (input[row][col])
    {
    case '>':
        return direction == RIGHT;
    case '<':
        return direction == LEFT;
    case '^':
        return direction == UP;
    case 'v':
        return direction == DOWN;
    case '#':
        return false;
    case '.':
        return true;
    }
    return false;
}

void find_longest_path(int row, int col, int len)
{

    if (row == end_x && col == end_y)
    {
        if (len > longest_path)
        {
            longest_path = len;
        }
        return;
    }

    input[row][col] = '#';

    if (is_valid(row - 1, col, UP))
    {
        find_longest_path(row - 1, col, len + 1);
    }

    if (is_valid(row + 1, col, DOWN))
    {
        find_longest_path(row + 1, col, len + 1);
    }

    if (is_valid(row, col + 1, RIGHT))
    {
        find_longest_path(row, col + 1, len + 1);
    }

    if (is_valid(row, col - 1, LEFT))
    {
        find_longest_path(row, col - 1, len + 1);
    }

    input[row][col] = '.';
}

int main()
{
    int rows = 0, cols = 0;
    std::string line;

    while (getline(std::cin, line))
    {
        for (int i = 0; i < line.size(); i++)
        {
            if (line[i] == '#')
            {
                input[rows][i] = line[i];
            }
            else
            {
                input[rows][i] = '.';
            }

            cols = i + 1;
        }
        rows++;
    }

    start_x = 0;
    start_y = 1;
    end_x = rows - 1;
    end_y = cols - 2;

    printf("start: %d %d %c\n", start_x, start_y, input[start_x][start_y]);
    printf("end: %d %d %c\n", end_x, end_y, input[end_x][end_y]);
    input[start_x][start_y] = '#';

    // this way we don't have to check for going out of bounds
    find_longest_path(start_x + 1, start_y, 1);

    printf("%d\n", longest_path);
}
