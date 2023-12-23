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

bool is_valid(int row, int col, Direction direction)
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

    char prev = input[row][col];
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

    input[row][col] = prev;
}

int main()
{
    int rows = 0, cols = 0;
    std::string line;

    while (getline(std::cin, line))
    {
        for (int i = 0; i < line.size(); i++)
        {
            input[rows][i] = line[i];

            cols = i + 1;
        }
        rows++;
    }

    start_x = 0;
    start_y = 1;
    end_x = rows - 1;
    end_y = cols - 2;

    input[start_x][start_y] = '#';

    // this way we don't have to check for going out of bounds
    find_longest_path(start_x + 1, start_y, 1);
    std::cout << longest_path << '\n';

    for (size_t i = 0; i < rows; i++)
    {
        for (size_t j = 0; j < cols; j++)
        {
            if (input[i][j] != '#')
            {
                input[i][j] = '.';
            }
        }
    }

    find_longest_path(start_x + 1, start_y, 1);
    std::cout << longest_path << '\n';
}
