// Global Variables
boolean tailMode = true; // if the tail is visible
float tailWidth = 0.75; // the width of the lines
float meters = 0.75; // m = px
float force = 2.5; // Throw Speed
float life = 15; // ball lifetime
int tail = 20; // ball tail length
float gravity = 9.78; // ag in meter/s^2
// 9.78 (earth)
// 1.62 (moon)
// 3.78 (mercury)
// 8.8 (venus)
// 3.72 (mars)
// 23.1 (jupiter)
// 9.05; (saturn)
// 8.69; (uranus)
// 11.0; (neptune)
// 0.6; (pluto)
// 274; (sol)

// Inital
int oY;
int oX;
float aimX;
float aimY;
boolean spawn = false;
boolean aim = false;
int ballCount;
Ball[] balls = {};

void setup(){
//  fullScreen();
  frameRate(60);
  size(800,450);
  colorMode(HSB);
}

void draw(){
  background(0);
  if(spawn){
    ballCount++;
    balls = (Ball[]) expand(balls,ballCount);
    float radius = round(random(1,5))*5;
    float resistance = 1/(pow(radius,0.085));
    balls[balls.length-1] = new Ball(aimX,aimY,(mouseX-aimX)*meters*force/frameRate,(mouseY-aimY)*meters*force/frameRate+1,radius,resistance,tail);
    spawn = false;
  }
  for(int i=0;i<balls.length;i++){
    Ball ball = balls[i];
    if(ball.check()){
      balls = (Ball[]) reverse(balls);
      balls = (Ball[]) shorten(balls);
      balls = (Ball[]) reverse(balls);
      ballCount = balls.length;
    }
    ball.render();
    ball.bounce();
  }
}

void mousePressed(){
  aim = true;
  aimX = mouseX;
  aimY = mouseY;
}

void mouseReleased(){
  aim = false;
  spawn = true;
}