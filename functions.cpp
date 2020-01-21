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
    delete [] image; // delete array of pointers
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
  for (int i=0; i < width; ++i) {
    delete [] image[i]; // delete each individual array placed on the heap
  }
  delete [] image;
  image = nullptr;
}

// implement for part 1

int* createSeam(int length) {
    int* seam = new int[length];
    for(int i = 0; i < length; ++i){
        seam[i] = 0;
    }
    return seam;
}

void deleteSeam(int* seam) {
    delete[] seam;
}

bool loadImage(string filename, Pixel** image, int width, int height) {
    ifstream infile{filename};
    if(!infile.is_open()){
        cout << "Error: failed to open input file - " << filename << endl;
        return false;
    }
    string type{};
    infile >> type;
    if(!(type == "P3" || type == "p3")){
        cout << "Error: type is " << type << " instead of P3" << endl;
        return false;
    }
    int w;
    int h;
    infile >> w >> h;
    if(infile.fail()){
        cout << "Error: read non-integer value" << endl;
        return false;
    }
    if(w != width){
        cout << "Error: input width (" << width << ") does not match value in file (" << w << ")" << endl;
        return false;
    }
    if(h != height){
        cout << "Error: input height (" << height << ") does not match value in file (" << h << ")" << endl;
        return false;
    }
    int p;
    infile >> p;
    int r, g, b;
    for(int i = 0; i < height; ++i){
        for(int j = 0; j < width; ++j){
            infile >> r;
            if(infile.eof()){
                cout << "Error: not enough color values" << endl;
                return false;
            }
            if(infile.fail()){
                cout << "Error: read non-integer value" << endl;
                return false;
            }
            if(r > 255 || r < 0){
                cout << "Error: invalid color value " << r << endl;
                return false;
            }
            image[j][i].r = r;
            infile >> g;
            if(infile.eof()){
                cout << "Error: not enough color values" << endl;
                return false;
            }
            if(infile.fail()){
                cout << "Error: read non-integer value" << endl;
                return false;
            }
            if(g > 255 || g < 0){
                cout << "Error: invalid color value " << g << endl;
                return false;
            }
            image[j][i].g = g;
            infile >> b;
            if(infile.eof()){
                cout << "Error: not enough color values" << endl;
                return false;
            }
            if(infile.fail()){
                cout << "Error: read non-integer value" << endl;
                return false;
            }
            if(b > 255 || b < 0){
                cout << "Error: invalid color value " << b << endl;
                return false;
            }
            image[j][i].b = b;
        }
    }
    int temp;
    infile >> temp;
    if(!infile.fail()){
        cout << "Error: too many color values" << endl;
        return false;
    }
    infile.close();
    return true;
}

bool outputImage(string filename, Pixel** image, int width, int height) {
    ofstream outFile;
    outFile.open(filename);
    if(!outFile.is_open()){
        cout << "Error: failed to open output file - " << filename << endl;
        return false;
    }
    outFile << "P3" << endl;
    outFile << width << " " << height << endl;
    outFile << 255 << endl;
    for(int i = 0; i < height; ++i){
        for(int j = 0; j < width; ++j){
            outFile << image[j][i].r << " " << image[j][i].g << " " << image[j][i].b << " ";
        }
    }
    outFile.close();
    return true;
}

int energy(Pixel** image, int x, int y, int width, int height) { 
    int tot_energy = 0;
    int grad_x = 0;
    if(x == 0){
        grad_x += pow((image[1][y].r - image[width - 1][y].r), 2) + pow((image[1][y].g - image[width - 1][y].g), 2) + pow((image[1][y].b - image[width - 1][y].b), 2);
    }
    else if(x == width - 1){
        grad_x += pow(image[0][y].r - image[x - 1][y].r, 2) + pow(image[0][y].g - image[x - 1][y].g, 2) + pow(image[0][y].b - image[x - 1][y].b, 2);
    }
    else{
        grad_x += pow(image[x + 1][y].r - image[x - 1][y].r, 2) + pow(image[x + 1][y].g - image[x - 1][y].g, 2) + pow(image[x + 1][y].b - image[x - 1][y].b, 2); 
    }
    int grad_y = 0;
    if(y == 0){
        grad_y += pow(image[x][1].r - image[x][height - 1].r, 2) + pow(image[x][1].g - image[x][height - 1].g, 2) + pow(image[x][1].b - image[x][height - 1].b, 2);
    }
    else if(y == height - 1){
        grad_y += pow(image[x][0].r - image[x][y - 1].r, 2) + pow(image[x][0].g - image[x][y - 1].g, 2) + pow(image[x][0].b - image[x][y - 1].b, 2);
    }
    else{
        grad_y += pow(image[x][y + 1].r - image[x][y - 1].r, 2) + pow(image[x][y + 1].g - image[x][y - 1].g, 2) + pow(image[x][y + 1].b - image[x][y - 1].b, 2);
    }
    tot_energy = grad_x + grad_y;
    return tot_energy;
}

// implement for part 2

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

int* findMinVerticalSeam(Pixel** image, int width, int height) {
    int* minimum_seam = new int[height];
    int minimum_energy = loadVerticalSeam(image, 0, width, height, minimum_seam);
    int curr_energy;
    for(int i = 1; i < width; ++i)
    {
        int* seam = new int[height];
        curr_energy = loadVerticalSeam(image, i, width, height, seam);
        
        if(curr_energy < minimum_energy)
        {
            minimum_energy = curr_energy;
            for(int i = 0; i < height; ++i)
            {
                minimum_seam[i] = seam[i];
            }
        }
        delete[] seam;
    }
    return minimum_seam;
}

int* findMinHorizontalSeam(Pixel** image, int width, int height) {
    int* minimum_seam = new int[width];
    int minimum_energy = loadHorizontalSeam(image, 0, width, height, minimum_seam);
    int curr_energy;
    for(int i = 1; i < height; ++i)
    {
        int* seam = new int[width];
        curr_energy = loadHorizontalSeam(image, i, width, height, seam);
        
        if(curr_energy < minimum_energy)
        {
            minimum_energy = curr_energy;
            for(int i = 0; i < width; ++i)
            {
                minimum_seam[i] = seam[i];
            }
        }

        delete[] seam;
    }
    return minimum_seam;
}

void removeVerticalSeam(Pixel** image, int width, int height, int* verticalSeam) {
    for(int i = 0; i < height; ++i)
    {
        int col = verticalSeam[i];

        for(int j = col; j < width - 1; ++j)
        {
            image[j][i] = image[j + 1][i];
        }
    }
}

void removeHorizontalSeam(Pixel** image, int width, int height, int* horizontalSeam) {
    for(int i = 0; i < width; ++i)
    {
        int row = horizontalSeam[i];
        for(int j = row; j < height - 1; ++j)
        {
            image[i][j] = image[i][j + 1];
        }
    }
}
