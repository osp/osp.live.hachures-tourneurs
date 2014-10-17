import oscP5.*;
import netP5.*;

import geomerative.*;
import processing.opengl.*;
//import processing.xml.*;

OscP5 oscP5;
NetAddress myRemoteLocation;

// global variables
RShape grp;
String svgFile;
ArrayList ve;
int nve = 1;
int colo;
int record = 1;

// global params
float pl = 4.0; // maximum segments length


void setup() {
  // Initilaize the sketch
  size(1024, 768);
  frameRate(220);
  ve= new ArrayList();

  // start oscP5, telling it to listen for incoming messages at port 5001 */
  oscP5 = new OscP5(this, 5001);

  // set the remote location to be the localhost on port 5001
  myRemoteLocation = new NetAddress("127.0.0.1", 5001);

  // Choice of colors
  background(255);
  fill(255, 102, 0);
  stroke(100);
  strokeWeight(1);

  // VERY IMPORTANT: Allways initialize the library in the setup
  RG.init(this);

  //svgFile = selectInput();
  svgFile = "image.svg";
  grp = RG.loadShape(svgFile);
  smooth();

  exVert(grp);
  println("tot points: " + ve.size());
  println(grp.getTopLeft().x);
  //grp.draw();
}

void draw() {
  if (nve < ve.size()) {
    strokeWeight(map(mouseY, 0, height, 1, 20));
    stroke(255, 0, 0);
    if (((Point) ve.get(nve)).z != -10.0) {
      line(((Point) ve.get(nve-1)).x, ((Point) ve.get(nve-1)).y, ((Point) ve.get(nve)).x, ((Point) ve.get(nve)).y);
      float okx = (((Point) ve.get(nve)).x);
      float oky = (((Point) ve.get(nve)).y);

      /* create an osc bundle */
      OscBundle myBundle = new OscBundle();

      OscMessage start = new OscMessage("/start");
      start.add(record);

      OscMessage myMessagex = new OscMessage("/x");
      myMessagex.add(okx); // add a string to the osc message

      OscMessage myMessagey = new OscMessage("/y");
      myMessagey.add(oky); // add a string to the osc message

      myBundle.add(myMessagex);
      myBundle.add(myMessagey);
      myBundle.add(start);

      // send the message
      oscP5.send(myBundle, myRemoteLocation);
    }
    nve++;
  } else { // restart drawing

    /* stop recording */
    int record = 0;

    OscBundle myBundle = new OscBundle();

    OscMessage start = new OscMessage("/start");
    start.add(record);

    myBundle.add(start);

    // send the message
    oscP5.send(myBundle, myRemoteLocation);


    delay(3000);
    background(255);
    nve = 1;
  }
}

// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
// recursively find RShape children and "flattens", by putting vertices inside an array
//
void exVert(RShape s) {
  RShape[] ch; // children
  int n, i, j;
  RPoint[][] pa;

  n = s.countChildren();
  if (n > 0) {
    ch = s.children;
    for (i = 0; i < n; i++) {
      exVert(ch[i]);
    }
  } else { // no children -> work on vertex
    pa = s.getPointsInPaths();
    n = pa.length;
    for (i=0; i<n; i++) {
      for (j=0; j<pa[i].length; j++) {
        //ellipse(pa[i][j].x, pa[i][j].y, 2,2);
        if (j==0)
          ve.add(new Point(pa[i][j].x, pa[i][j].y, -10.0));
        else
          ve.add(new Point(pa[i][j].x, pa[i][j].y, 0.0));
      }
    }
    //println("#paths: " + pa.length);
  }
}

// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
// Class for a 3D point
//
class Point {
  float x, y, z;
  Point(float x, float y, float z) {
    this.x = x;
    this.y = y;
    this.z = z;
  }

  void set(float x, float y, float z) {
    this.x = x;
    this.y = y;
    this.z = z;
  }
}

