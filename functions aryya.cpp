#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <cmath>
#include "functions.h"

using namespace std;

Pixel** createImage(int width, int height) {
  cout << "Start createImage... " << endl;
  
  // Create a one dimensional array on the heap of pointers to Pixels 
  //    that has width elements (i.e. the number of columns)
  Pixel** image = new Pixel*[width];
  
  bool fail = false;
  
  for (int i=0; i < width; ++i) { // loop through each column
    // assign that column to a one dimensional array on the heap of Pixels
    //  that has height elements (i.e. the number of rows)
    image[i] = new Pixel[height];
    
    if (image[i] == nullptr) { // failed to allocate
      fail = true;
    }
  }
  
  if (fail) { // if any allocation fails, clean up and avoid memory leak
    // deallocate any arrays created in for loop
    for (int i=0; i < width; ++i) {
      delete [] image[i]; // deleting nullptr is not a problem
    }
    delete [] image; // dlete array of pointers
    return nullptr;
  }
  
  // initialize cells
  //cout << "Initializing cells..." << endl;
  for (int row=0; row<height; ++row) {
    for (int col=0; col<width; ++col) {
      //cout << "(" << col << ", " << row << ")" << endl;
      image[col][row] = { 0, 0, 0 };
    }
  }
  cout << "End createImage... " << endl;
  return image;
}

void deleteImage(Pixel** image, int width) {
  cout << "Start deleteImage..." << endl;
  // avoid memory leak by deleting the array
  for (int i=0; i<width; ++i) {
    delete [] image[i]; // delete each individual array placed on the heap
  }
  delete [] image;
  image = nullptr;
}

// implement for part 1

int* createSeam(int length) 
{

  int* seam = new int[length];

  for(int i=0;i<length;i++)
  {
    seam[i]=0;
  }


  return seam;
}

void deleteSeam(int* seam) 
{

  delete [] seam;

}

bool loadImage(string filename, Pixel** image, int width, int height)
{

  int colorvalue=0;
  ifstream ifs(filename);
  if(!ifs.is_open())
  {
    cout << "Error: failed to open input file - " << filename << endl;
    return false;

  }
  char type[3];
  ifs >> type;
  if ((toupper(type[0]) != 'P') || (type[1] != '3')) 
  {
    cout << "Error: type is " << type << " instead of P3" << endl;
    return false;
  }


  int w_check=0;
  int h_check=0;

  ifs >> w_check;

  if(ifs.fail())
  { 
    
    cout << "Error: read non-integer value" << endl;
    return false;

  }

  if(w_check!=width)
  {
    cout << "Error: input width ("<< width <<") does not match value in file ("<<w_check << ")" << endl;
    return false;
  }

  ifs >> h_check;

  if(ifs.fail())
  { 
    
    cout << "Error: read non-integer value" << endl;
    return false;

  }

  if(h_check!=height)
  {
    cout << "Error: input height ("<< height <<") does not match value in file ("<<h_check << ")" << endl;
    return false;
  }

  ifs >> colorvalue;
  if(ifs.fail())
  {
    cout << "Error: read non-integer value" << endl;
  }
  if((colorvalue>255)||(colorvalue<0))
  {
    cout << "Error: invalid color value " << colorvalue << endl;
  }

  for(int i = 0; i <height; i++)
{
  for(int j = 0; j <width; j++)
  {

    ifs >> image[j][i].r;

    if(ifs.fail())
    {
      if(ifs.eof())
      {
        cout << "Error: not enough color values" << endl;
        return false;
      }
    }

    if(ifs.fail())
    {

      cout << "Error: read non-integer value" << endl;
      return false;

    }

    if(image[j][i].r <0 || image[j][i].r >255)
    {

      cout << "Error: invalid color value " << image[j][i].r << endl;
      return false;

    } 

    ifs >> image[j][i].g;

    if(ifs.fail())
    {
      if(ifs.eof())
      {
        cout << "Error: not enough color values" << endl;
        return false;
      }
    }

    if(ifs.fail())
    {

      cout << "Error: read non-integer value" << endl;
      return false;

    }

    if(image[j][i].g <0 || image[j][i].g >255)
    {

      cout << "Error: invalid color value " << image[j][i].g << endl;
      return false;

    }

    ifs >> image[j][i].b;

    if(ifs.fail())
    {
      if(ifs.eof())
      {
        cout << "Error: not enough color values" << endl;
        return false;
      }
    }

    if(ifs.fail())
    {

      cout << "Error: read non-integer value" << endl;
      return false;

    }

    if(image[j][i].b <0 || image[j][i].b >255)
    {

      cout << "Error: invalid color value " << image[j][i].b << endl;
      return false;
    }
  }
}
  
  int value=0;
  
  if(ifs >> value)
  {
    cout << "Error: too many color values" << endl;
    return false;

  }

  return true;
}





bool outputImage(string filename, Pixel** image, int width, int height) 
{

  fstream ifs(filename);
  if(!ifs.is_open())
  {
    cout << "failed to open output file " << filename << endl;
    return false;
  }

  ifs << "P3" << endl;
  ifs << width << " " << height << endl;
  ifs << 255 << endl;

  for(int i = 0; i <height; i++)
  {
    for(int j = 0; j <width; j++)
    {
        ifs << image[j][i].r << " " << image[j][i].g << " " << image[j][i].b << endl;
    }
  }

  return true;
}

int energy(Pixel** image, int x, int y, int width, int height) 
{ 
  int delta_rx = 0;
  int delta_gx=0;
  int delta_bx=0;
  int totalx = 0;
  int delta_ry = 0;
  int delta_gy=0;
  int delta_by = 0;
  int totaly = 0;
  int energy=0;

  if(x==0)
  {

    delta_rx = image[x+1][y].r - image[width-1][y].r;
    delta_gx = image[x+1][y].g - image[width-1][y].g;
    delta_bx = image[x+1][y].b - image[width-1][y].b;

  }
  else if(x == width -1)
  {

    delta_rx = image[0][y].r - image[x-1][y].r;
    delta_gx = image[0][y].g - image[x-1][y].g;
    delta_bx = image[0][y].b - image[x-1][y].b;

  }
  else
  {

    delta_rx = image[x+1][y].r - image[x-1][y].r;
    delta_gx = image[x+1][y].g - image[x-1][y].g;
    delta_bx = image[x+1][y].b - image[x-1][y].b;

  }

  totalx = (delta_rx*delta_rx) + (delta_gx*delta_gx) + (delta_bx*delta_bx);

  if(y==0)
  {

    delta_ry = image[x][y+1].r - image[x][height - 1].r;
    delta_gy = image[x][y+1].g - image[x][height - 1].g;
    delta_by = image[x][y+1].b - image[x][height - 1].b; 

  }
  else if(y == height-1)
  {

    delta_ry = image[x][0].r - image[x][y-1].r;
    delta_gy = image[x][0].g - image[x][y-1].g;
    delta_by = image[x][0].b - image[x][y-1].b; 

  }
  else
  {

    delta_ry = image[x][y+1].r - image[x][y-1].r;
    delta_gy = image[x][y+1].g - image[x][y-1].g;
    delta_by = image[x][y+1].b - image[x][y-1].b; 

  } 

  totaly = (delta_ry*delta_ry) + (delta_gy*delta_gy) + (delta_by*delta_by);

  energy = totalx + totaly; 

  return energy;

}
 
int loadVerticalSeam(Pixel** image, int start_col, int width, int height, int* seam) {
    int col = start_col;
    int middle;
    int left;
    int right;
    int energy_sum= 0;
    seam[0] = col;
    energy_sum += energy(image, col, 0, width, height);
    for(int i = 1; i < height; ++i){
        if(col == 0)
        {
            middle = energy(image, col, i, width, height);
            right = energy(image, col + 1, i, width, height);
            if(middle <= right)
            {
                energy_sum += middle;
                seam[i] = col;
            } 
            else
            {
                energy_sum += right;
                seam[i] = col + 1;
                ++col;
            }
        } 
        else if(col == width - 1)
        {
            middle = energy(image, col, i, width, height);
            left = energy(image, col - 1, i, width, height);
            if(middle <= left)
            {
                energy_sum += middle;
                seam[i] = col;
            } else
            {
                energy_sum += left;
                seam[i] = col - 1;
                --col;
            }
        } 
        else
        {
            middle = energy(image, col, i, width, height);
            left = energy(image, col - 1, i, width, height);
            right = energy(image, col + 1, i, width, height);
            if(middle < right && middle < left)
            {
                energy_sum += middle;
                seam[i] = col;
            } 
            else if(right < middle && right < left)
            {
                energy_sum += right;
                seam[i] = col + 1;
                ++col;
            } 
            else if(left < middle && left < middle)
            {
                energy_sum += left;
                seam[i] = col - 1;
                --col;
            } 
            else
            {
                if(middle == left&& middle == right)
                {
                    energy_sum += middle;
                    seam[i] = col;
                } 
                else if(middle == left && middle != right)
                {
                    energy_sum += middle;
                    seam[i] = col;
                } 
                else if(middle == right && middle != left)
                {
                    energy_sum += middle;
                    seam[i] = col;
                } 
                else if(left == right && left != middle)
                {
                    energy_sum += right;
                    seam[i] = col + 1;
                    ++col;
                }
            }
        }
    }
    return energy_sum;
}

int loadHorizontalSeam(Pixel** image, int start_row, int width, int height, int* seam)
 {
    int row = start_row;
    int middle;
    int top;
    int bottom;
    int energy_sum = 0;
    seam[0] = row;
    energy_sum += energy(image, 0, row, width, height);
    for(int i = 1; i < width; ++i)
    {
        if(row == 0)
        {
            middle = energy(image, i, row, width, height);
            bottom = energy(image, i, row + 1, width, height);
            if(middle <= bottom)
            {
                seam[i] = row;
                energy_sum += middle;
            } 
            else
            {
                seam[i] = row + 1;
                ++row;
                energy_sum += bottom;
            }
        } 
        else if(row == height - 1)
        {
            top = energy(image, i, row - 1, width, height);
            middle = energy(image, i, row, width, height);
            if(middle <= top)
            {
                seam[i] = row;
                energy_sum += middle;
            } 
            else
            {
                seam[i] = row - 1;
                --row;
                energy_sum += top;
            }
        } 
        else
        {
            middle = energy(image, i, row, width, height);
            bottom = energy(image, i, row + 1, width, height);
            top = energy(image, i, row - 1, width, height);
            if(middle < top && middle < bottom)
            {
                energy_sum += middle;
                seam[i] = row;
            } 
            else if(top < middle && top < bottom)
            {
                energy_sum += top;
                seam[i] = row - 1;
                --row;
            } 
            else if(bottom < middle && bottom< top)
            {
                energy_sum += bottom;
                seam[i] = row + 1;
                ++row;
            } 
            else
            {
                if(middle == bottom && middle == top)
                {
                    energy_sum += middle;
                    seam[i] = row;
                } 
                else if(middle == bottom && middle != top)
                {
                    energy_sum += middle;
                    seam[i] = row;
                } 
                else if(middle == top && middle != bottom)
                {
                    energy_sum += middle;
                    seam[i] = row;
                } 
                else if(top == bottom && top != bottom)
                {
                    energy_sum += top;
                    seam[i] = row - 1;
                    --row;
                }
            }
        }
    }
    return energy_sum;
}


int* findMinVerticalSeam(Pixel** image, int width, int height) 
{
  
  int* min_value_seam = new int [height];
  int min_energy = loadVerticalSeam(image, 0, width, height, min_value_seam);
  int temp_energy;

    for(int col=1; col<width; col++)
    {
      int* seam = new int[height];
      temp_energy = loadVerticalSeam(image, col, width, height, seam);
      if(temp_energy < min_energy)
      {
        min_energy = temp_energy;
        min_value_seam = seam;
        for(int i=0; i<height; i++)
        {
          min_value_seam[i] = seam[i];
        }
      }
      delete [] seam;
    }

   
 return min_value_seam;
}

int* findMinHorizontalSeam(Pixel** image, int width, int height) 
{
  int* min_value_seam = new int [width];
  int min_energy = loadVerticalSeam(image, 0, width, height, min_value_seam);
  int temp_energy;

    for(int row=1; row<height; col++)
    {
      int* seam = new int[width];
      temp_energy = loadVerticalSeam(image, row, width, height, seam);
      if(temp_energy < min_energy)
      {
        min_energy = temp_energy;
        min_value_seam = seam;
        for(int i=0; i<width; i++)
        {
          min_value_seam[i] = seam[i];
        }
      }
      delete [] seam;
    }

   
 return min_value_seam;
}


void removeVerticalSeam(Pixel** image, int width, int height, int* verticalSeam) 
{

  for(int i = 0; i< height;i++)
  {
    for(int j=verticalSeam[i];j<width-1;j++)
    {
      image[j][i] = image[j+1][i];
    }
  }


}


void removeHorizontalSeam(Pixel** image, int width, int height, int* horizontalSeam) 
{

  for(int i=0; i<width; i++)
  {
    for(int j=horizontalSeam[i]; j<height-1;j++)
    {
      image[i][j] = image[i][j+1];
    }
  }



}
