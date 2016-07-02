boolean julia = false;                              // is julia set (true/false)
int n = 2;                                          // exponent of the fractal
float k = 2;                                        // logarithmic color power
int max = 50;                                       // maximum iterations
float zoom = 1;                                     // zoom magnitude
Complex constant = new Complex(new PVector(0, 0));  // constant for julia set
Complex transpose = new Complex(new PVector(0, 0)); // transpose for both numbers
PVector offset = new PVector(0, 0);                 // offset for the graph
int p = 3;                                          // decimal places for file name            
float ji = 0;                                       // incrementation for constant
float ti = 0;                                       // incrementation for transpose 1
float con = 0;                                      // incrementation for transpose 2
float increment = 0.05;                             // incrementation for zoom

// DO NOT TOUCH FROM HERE ON ---------------------------------------------------------

String path;
float state = 1;
float depth = 5/zoom;
void setup() {
  size(800, 450);
  colorMode(HSB, 1);
}
void draw() {
  constant.t += ji;
  if (constant.t >= TWO_PI-ji &&  constant.t <= TWO_PI+ji) {
    constant.r += ji;
  }
  constant = new Complex(constant.r, constant.t);
  transpose.v.x += ti;
  transpose.v.y += con;
  transpose = new Complex(transpose.v);
  background(255);
  loadPixels();
  PVector[] range = {new PVector(-depth/2, -depth/2/width*height).add(offset), new PVector(depth/2, depth/2/width*height).add(offset)};
  float[] res = {(range[1].x - range[0].x)/width, (range[1].y - range[0].y)/height};
  float y = range[0].y;
  for (int j = 0; j < height; j++) {
    float x = range[0].x;
    for (int i = 0; i < width; i++) {
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
        pixels[i+j*width] = color(0);
      } else {
        pixels[i+j*width] = color(1-pow((float(iters) / max), pow(k, -1)), 1-pow((float(iters) / max), pow(k, -1)), pow((float(iters) / max), pow(k, -1)));
      }
      x += res[0];
    }
    y += res[1];
  }
  updatePixels();
}
void mousePressed() {
  state += increment;
  depth /= state;
  offset.x += (mouseX - width/2 ) / float(width);
  offset.y += (mouseY - height/2 ) / float(height);
}

void keyPressed() {
  if (key == ' ') {
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
    saveFrame("Image/Fractals/"+path+".png");
    println(path);
  }
}

float round(float f, int p) {
  return round(pow(10, p)*f)/pow(10, p);
}