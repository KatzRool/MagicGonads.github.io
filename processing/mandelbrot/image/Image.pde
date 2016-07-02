boolean julia = false;                              // is julia set (true/false)
int n = 2;                                          // exponent of the fractal
float k = 2;                                        // logarithmic color power
int max = 50;                                       // maximum iterations
float zoom = 1;                                     // zoom magnitude
Complex constant = new Complex(new PVector(0, 0));  // constant for julia set
Complex transpose = new Complex(new PVector(0, 0)); // transpose for both numbers
PVector offset = new PVector(0, 0);                 // offset for the graph
int resolution = 1;                                 // resolution multiplier
int p = 3;                                          // decimal places for file name

// DO NOT TOUCH FROM HERE ON ---------------------------------------------------------

String path;
float state = 1;
float depth = 5/zoom;
void setup() {
  size(800, 450);
  colorMode(HSB, 1);
  PImage img = createImage(int(width*sqrt(resolution)), int(height*sqrt(resolution)), RGB);
  img.loadPixels();
  background(255);
  PVector[] range = {new PVector(-depth/2, -depth/2/img.width*img.height).add(offset), new PVector(depth/2, depth/2/width*height).add(offset)};
  float[] res = {(range[1].x - range[0].x)/img.width, (range[1].y - range[0].y)/img.height};
  float y = range[0].y;
  for (int j = 0; j < img.height; j++) {
    float x = range[0].x;
    for (int i = 0; i < img.width; i++) {
      Complex z = new Complex(new PVector(0, 0));
      Complex c = new Complex(new PVector(x, y));
      if (julia) {
        z = new Complex(new PVector(x, y));
        c = new Complex(constant.r, constant.t);
      }
      c = c.transpose(-cos(transpose.v.y));
      int iters = 0;
      while (iters < max) {
        z = z.transpose(cos(transpose.v.x)).raise(n).add(c);
        if (pow(z.v.x, n) + pow(z.v.y, n) > pow(4.0, n)) {
          break;
        }
        iters++;
      }
      if (iters == max) {
        img.pixels[i+j*img.width] = color(0);
      } else {
        img.pixels[i+j*img.width] = color(1-pow((float(iters) / max), pow(k, -1)), 1-pow((float(iters) / max), pow(k, -1)), pow((float(iters) / max), pow(k, -1)));
      }
      x += res[0];
    }
    y += res[1];
  }
  img.updatePixels();
  img.save("Fractals/"+nameImage()+".png");
  println(nameImage());
}

String nameImage() {
  String fractal = "Mandelbrot";
  if (julia) {
    fractal = "Julia";
  }
  path = fractal+" Set for z^"+n+" @ "+round(5.0/depth, p)+"x";
  if (julia) {
    path += " C["+round(constant.v.x, p)+','+round(constant.v.y, p)+']';
  }
  if (transpose.r < 0) {
    path += " T["+round(transpose.v.x, p)+','+round(transpose.v.y, p)+']';
  }
  path += " O["+round(offset.x, p)+','+round(offset.y, p)+']';
  return path;
}


float round(float f, int p) {
  return round(pow(10, p)*f)/pow(10, p);
}