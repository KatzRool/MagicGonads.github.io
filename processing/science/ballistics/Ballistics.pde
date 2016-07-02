// Variables
float m = 0.75; // m = px
int h = 15; // Ball Diameter
float r = 0.8; // Coefficient of Restitution
float f = 1.5; // Throw Speed

// Gravity
float g = 9.78; // ag in meter/s^2
// g = 9.78 (earth)
// g = 1.62 (moon)
// g = 3.78 (mercury)
// g = 8.8 (venus)
// g = 3.72 (mars)
// g = 23.1 (jupiter)
// g = 9.05; (saturn)
// g = 8.69; (uranus)
// g = 11.0; (neptune)
// g = 0.6; (pluto)
// g = 274; (sol)

// Inital
int y;
int x;
int guide = 0;
int sim = 0;
float speedX = 0;
float speedY = 0;
float posX;
float posY;
float fall = 0;
float drop = 0;
float far = 0;
float c = 0;
float[] pposX = {-h,-h,-h,-h,-h,-h,-h,-h,-h,-h,-h,-h,-h,-h,-h,-h,-h,-h,-h,-h};
float[] pposY = {-h,-h,-h,-h,-h,-h,-h,-h,-h,-h,-h,-h,-h,-h,-h,-h,-h,-h,-h,-h};

void setup(){
//  fullScreen();
  frameRate(60);
  size(1000,400);
  colorMode(HSB);
  fill(0);
}

void draw(){
  if(c == 255){
    c = 0;
  }
  else{
    c += 1;
  }
  fill(255-c,255,255);
  stroke(c,255,255);
  background(0);
  if(guide == 1){
    line(x,y,mouseX,mouseY);
  }
  else if(sim == 0){
    x = mouseX;
    y = mouseY; 
    posX = x;
    posY = y;
  }
  if(sim == 1){
    posX += speedX;
    posY += fall+speedY;
    posX = constrain(posX,0,width);
    posY = constrain(posY,0,height);
    for(int i = 0; i < 19; i += 1){
      pposX[i] = pposX[i+1];
      pposY[i] = pposY[i+1];
    }
    pposX[19] = posX;
    pposY[19] = posY;
    for(int i = 0; i < 20; i += 1){
      fill(255-c,(i+1)*10 +55,(i+1)*10.5);
      stroke(c,(i+1)*10 +55,(i+1)*10.5);
      ellipse(pposX[i],pposY[i],m*h,m*h);
    }
    fill(255-c,255,255);
    stroke(c,255,255);
    ellipse(posX,posY,m*h,m*h);
    fall += g*m/frameRate;
    if(posX <= 0 || posX >= width){
      speedX = -speedX*r;
      speedY = speedY*r;
    }
    if(posY <= 0 || posY >= height){
      speedY = -(speedY+fall)*r;
      fall = 0;
      speedX = speedX*r;
    }
  }
}

void mousePressed(){
  if(sim == 0){
    guide = 1;
  }
}

void mouseReleased(){
  if(sim == 0){
    guide = 0;
    sim = 1;
    speedX = f*(mouseX-x)*m/frameRate;
    speedY = f*(mouseY-y)*m/frameRate;
  }
  else{
    sim = 0;
    far = 0;
    fall = 0;
    drop = 0;
    for(int i=0;i<20;i+=1){
      pposX[i] = -h;
      pposY[i] = -h;
  }
  }
}