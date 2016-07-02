class Complex{
  float r;
  float t;
  PVector v = new PVector(0,0);
  Complex(float r, float t){
    this.r = r;
    this.t = t;
    this.v.x = r*cos(t);
    this.v.y = r*sin(t);
  }
  Complex(PVector v){
    this.v = v;
    this.r = sqrt(pow(v.x,2)+pow(v.y,2));
    this.t = atan2(v.y,v.x);
  }
  Complex raise(int n){
    return new Complex(new PVector(pow(r,n)*cos(t*n),pow(r,n)*sin(t*n)));
  }
  Complex add(Complex a){
    return new Complex(new PVector(v.x+a.v.x,v.y+a.v.y));
  }
  Complex transpose(float a){
    return new Complex(new PVector(v.x,v.y*a));
  }
  Complex e(){
    float ex = exp(this.v.x);
    return new Complex(ex*cos(this.v.y),ex*sin(this.v.y));
  }
}