# Question 1 :- Finding Data Type of Data in C#

int num1 = 5;
double num2 = 5.0;
bool bul = 5 > 1;
char character = '5';
int num3 = 5 * 2;
int num4 = '5' * 2;
int num5 = '5' * '2';
int num6 = '5' + '2';
int num7 = 5 / 2 ;
int num8 = 5 % 2;
int[] array = {5,2,1};
bool bul1 = 5==3;
double num9 = Math.PI;
Console.WriteLine("Data type of num1:" + num1.GetType());
Console.WriteLine("Data type of num2:" + num2.GetType());
Console.WriteLine("Data type of boolean:" + bul.GetType());
Console.WriteLine("Data type of character:" + character.GetType());
Console.WriteLine("Data type of num3:" + num3.GetType());
Console.WriteLine("Data type of num4:" + num4.GetType());
Console.WriteLine("Data type of num6:" + num6.GetType());
Console.WriteLine("Data type of num7:" + num7.GetType());
Console.WriteLine("Data type of num8:" + num8.GetType());
Console.WriteLine("Data type of array:" + array.GetType());
Console.WriteLine("Data type of boolean:" + bul1.GetType());
Console.WriteLine("Data type of num9:" + num9.GetType());

# Question 2 Write (and evaluate) C# expressions

string txt1 = "Supercalifragilisticexpialidocious";
string substringToFind = "ice";
bool containsSubstring = txt1.Contains(substringToFind);
string word2 = "Honorificabilitudinitatibus";
string word3 = "Bababadalgharaghtakamminarronnkonn";

        int maxLength = Math.Max(txt1.Length, Math.Max(word2.Length, word3.Length));

        if (txt1.Length == maxLength)
        {
            Console.WriteLine("The longest word is: Supercalifragilisticexpialidocious");
        }
        else if (word2.Length == maxLength)
        {
            Console.WriteLine("The longest word is: Honorificabilitudinitatibus");
        }
        else
        {
            Console.WriteLine("The longest word is: Bababadalgharaghtakamminarronnkonn");
        }
 if (containsSubstring)
        {
            Console.WriteLine("The word contains the substring 'ice'.");
        }
        else
        {
            Console.WriteLine("The word does not contain the substring 'ice'.");
        }
Console.WriteLine("Total number of letters in above string:" + txt1.Length);
string[] composers = { "Berlioz", "Borodin", "Brian", "Bartok", "Bellini", "Buxtehude", "Bernstein" };

        Array.Sort(composers); 

        Console.WriteLine("First composer: " + composers[0]);
        Console.WriteLine("Last composer: " + composers[composers.Length - 1]);




#Question 3 Implement function triangleArea(a,b,c) that takes as input the lengths of the 3 sides of a triangle and returns the area of the triangle. By Heron's formula, 
the area of a triangle with side lengths a, b, and c is 

double a = 2.0;
double b = 2.0;
double c = 2.0;
double s = (a + b + c) / 2.0;
double area = Math.Sqrt(s * (s - a) * (s - b) * (s - c));
Console.WriteLine("The area of triangle is: " + area);


#Question 4 : Write a program in C# Sharp to separate odd and even integers in separate arrays.
#https://stackoverflow.com/questions/69717370/array-of-total-even-numbers

int[] test_data = {25, 47, 42, 56, 32};
int[] evenarr;
int[] oddarr;

evenarr = new int[test_data.Length]; 
oddarr = new int[test_data.Length]; 
int evenCount = 0;
int oddCount = 0;

for (int i = 0; i < test_data.Length; i++)
{
    if (test_data[i] % 2 == 0)
    {
        evenarr[evenCount] = test_data[i];
        evenCount++;
    }
    else
    {
        oddarr[oddCount] = test_data[i];
        oddCount++;
    }
}


Array.Resize(ref evenarr, evenCount);
Array.Resize(ref oddarr, oddCount);

Console.WriteLine("Even elements are:");
foreach (int even in evenarr)
{
    Console.WriteLine(even);
}

Console.WriteLine("Odd elements are:");
foreach (int odd in oddarr)
{
    Console.WriteLine(odd);
}









#Question 5 Write a function inside(x,y,x1,y1,x2,y2) that returns True or False depending on whether the point (x,y) 
lies in the rectangle with lower left corner (x1,y1)
and upper right corner (x2,y2).


public static bool Inside(int x, int y, int x1, int y1, int x2, int y2)
{
    return x1 <= x && x <= x2 && y1 <= y && y <= y2;
}


Inside(1,1,0,0,2,3)

Inside(-1,-1,0,0,2,3)


bool inside(double x, double y, double x1, double y1, double x2, double y2)
{
   
    if (x < x1 || x > x2)
    {
        return false;
    }
    
    if (y < y1 || y > y2)
    {
        return false;
    }
    // If both checks pass, the point is inside the rectangle
    return true;
}
// Test if the point (1,1) lies in both rectangles
bool pointInBothRectangles = inside(1, 1, 0.3, 0.5, 1.1, 0.7) && inside(1, 1, 0.5, 0.2, 1.1, 2);
// Display the result
Console.WriteLine(pointInBothRectangles);

inside(1,1,0,0,2,3)

inside(-1,-1,0,0,2,3)


