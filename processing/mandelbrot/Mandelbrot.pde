boolean julia = true;
boolean tricorn = true;
float increment = 0.05;
int n = 2;
float k = 2;
int max = 50;
Complex v = new Complex(new PVector(0, 0));
Complex t = new Complex(new PVector(0, 0));
float ji = 0;
float ti = 0;
float con = 0;
int resolution = 1;
int p = 3;
float depth = 5;

PImage img;
String path;
float state = 1;
PVector offset = new PVector(0, 0);
void setup() {
  size(400, 400);
  colorMode(HSB, 1);
}
void draw() {
  img = createImage(width*resolution,height*resolution, RGB);
  v.t += ji;
  if (v.t >= TWO_PI-ji &&  v.t <= TWO_PI+ji) {
    v.r += ji;
  }
  v = new Complex(v.r, v.t);
  t.v.x += ti;
  t.v.y += con;
  t = new Complex(t.v);
  background(255);
  img.loadPixels();
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
        c = new Complex(v.r, v.t);
      }
      c = c.transpose(-cos(t.v.y));
      int iters = 0;
      while (iters < max) {
        if (tricorn) {
          z = z.transpose(-cos(t.v.x)).raise(n).add(c);
        } else {
          z = z.transpose(cos(t.v.x)).raise(n).add(c);
        }
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
  image(img,width,height);
  println(frameRate);
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
    if (tricorn) {
      fractal +=" Tricorn";
    }
    path = fractal+" Set for z^"+n+" @ "+round(5.0/depth, p)+"x";
    if (julia) {
      path += " C["+round(v.v.x, p)+','+round(v.v.y, p)+']';
    }
    if (t.r < 0) {
      path += " T["+round(t.v.x, p)+','+round(t.v.y, p)+']';
    }
    path += " O["+round(offset.x, p)+','+round(offset.y, p)+']';
    saveFrame("fractals/"+path+".png");
  }
}

float round(float f, int p) {
  return round(pow(10, p)*f)/pow(10, p);
}