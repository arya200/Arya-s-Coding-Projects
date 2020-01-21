int amax(const double* x, const unsigned int len);
double asum(const double* x, const unsigned int len);
void axpy(const double a, const double* x, double* y, const unsigned int len);
void copy(const double* src, double* dest, const unsigned int len);
double dot(const double* x, const double* y, const unsigned int len);
double norm2(const double* x, const unsigned int len);
void scale(const double a, double* x, const unsigned int len);
void swap(double* x, double* y, const unsigned int len);