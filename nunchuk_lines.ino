
/*
 * nunchuk_lines sketch
 * sends data to Processing to draw line that follows nunchuk movement
 */
 
#include <Wire.h> // initialize wire
 
const int vccPin = A3; // +v (power) provided by pin 17
const int gndPin = A2; // gnd provided by pin 16
 
const int dataLength = 6;        // number of bytes to request
static byte rawData[dataLength]; // array to store nunchuk data
 
enum nunchukItems{
  joyX,
  joyY,
  accelX,
  accelY,
  accelZ,
  btnZ,
  btnC
};
 
void setup(){
  pinMode(gndPin, OUTPUT); // set power pins to correct state
  pinMode(vccPin, OUTPUT);
  digitalWrite(gndPin, LOW);
  digitalWrite(vccPin, HIGH);
  delay(100); // wait for things to stabilize
  
  Serial.begin(9600);
  nunchukInit();
}

void loop(){
  
  nunchukRead();
  
  Serial.print("H,"); // header
  for(int i = 0; i < 7; i++){
    Serial.print(getValue(joyX+ i), DEC);
    Serial.write(',');
  }
  
  Serial.println();
  delay(27); //The time in ms between redraws

  
}

/*
 * Establishes I2C communication w/ nunchuk
 */
void nunchukInit(){
  
  Wire.begin(0x52);                 // join I2C bus as master
  Wire.beginTransmission(0x52); // transmit to device 0x52
  
  Wire.write((byte)0x40);       // sends memory address
  Wire.write((byte)0x00);       // sends one byte
  
  Wire.endTransmission();       // stop transmitting
  
}

/* 
 * Send a request for data to the nunchuk
 */
static void nunchukRequest(){
  
  Wire.beginTransmission(0x52); // transmit data to device 0x52
  Wire.write((byte)0x00);       // sends one byte
  Wire.endTransmission();       // stop transmitting

}


/*
 * Receive data back from the nunchuk,
 * returns true if read successful, else false
 */
boolean nunchukRead(){
  
  int count = 0;
  Wire.requestFrom(0x52, dataLength); // request data from nunchuk
  
  // works like Serial.available (indicates how many bytes have been received)
  while(Wire.available()){
    // store data in rawData buffer
    rawData[count] = nunchukDecode(Wire.read());
    count++;
  }
  
  nunchukRequest(); // send request for next data payload
  
  if(count >= dataLength){
    return true;     // success if all 6 bytes received
  }else{
    return false;    // failure
  }
  
}

/*
 * Encode data to format that most wiimote drivers accept
 */
static char nunchukDecode(byte x){
  return (x ^ 0x17) + 0x17;
}

int getValue(int item){
  if(item <= accelZ){
    return (int)rawData[item];
  }else if(item == btnZ){
    return bitRead(rawData[5], 0) ? 0 : 1;
  }else if(item == btnC){
    return bitRead(rawData[5], 1) ? 0 : 1;
  }
}
