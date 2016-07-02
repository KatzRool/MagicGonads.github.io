class Ball{
  int tail;
  float time;
  float radius;
  float resistance;
  float speedX;
  float speedY;
  float positionX;
  float positionY;
  float speedG;
  float colour;
  float[] ppositionX = {};
  float[] ppositionY = {};
  Ball(float tpX,float tpY, float tvX, float tvY, float tr, float tr2,int tt){
    radius = tr;
    resistance = tr2;
    positionX = tpX;
    positionY = tpY;
    speedX = tvX;
    speedY = tvY;
    tail = tt;
    ppositionX = expand(ppositionX,tail);
    ppositionY = expand(ppositionY,tail);
    for(int i=0;i<tail;i++){
      ppositionX[i] = -radius*2;
      ppositionY[i] = -radius*2;
    }
  }
  void render(){
    time++;
    colour++;
    if(colour==256){
      colour=1;
    }
    positionX += speedX;
    positionY += speedG+speedY;
    positionX = constrain(positionX,radius,width-radius);
    positionY = constrain(positionY,radius,height-radius);
    for(int i = 0; i < tail-1; i += 1){
      ppositionX[i] = ppositionX[i+1];
      ppositionY[i] = ppositionY[i+1];
    }
    ppositionX[tail-1] = positionX;
    ppositionY[tail-1] = positionY;
    for(int i = 0; i < tail; i += 1){
      if(tailMode){
        fill(radius*resistance,255,255-255*(time/(frameRate*life)),(i+1)*(255/tail));
        stroke(radius*resistance,255,255-255*(time/(frameRate*life)),(i+1)*(255/tail));
        ellipse(ppositionX[i],ppositionY[i],meters*radius*2*(i+1)/tail,meters*radius*2*(i+1)/tail);
      }
    }
    fill(radius*resistance,255,255-255*(time/(frameRate*life)));
    stroke(radius*resistance,255,255-255*(time/(frameRate*life)));
    ellipse(ppositionX[ppositionX.length-1],ppositionY[ppositionY.length-1],meters*radius*2,meters*radius*2);
    speedG += gravity*meters/frameRate;
  }
  void bounce(){
    if(positionX <= radius || positionX >= width-radius){
      speedX = -speedX*resistance;
      speedY = speedY*resistance;
    }
    if(positionY <= radius || positionY >= height-radius){
      speedY = -(speedY+speedG)*resistance;
      speedG = 0;
      speedX = speedX*resistance;
    }
  }
  boolean check(){
    if(time >= frameRate*life){
      return true;
    }
    else{
      return false;
    }
  }
}