/* VernierTutorialLinearCalibration (v2017)
 *  
 * This sketch reads the raw count from a Vernier Analog (BTA) 
 * sensor once every half second, and uses its algebraic slope 
 * and intercept to convert it to standard units.
 * 
 * Plug the sensor into the Analog 2 port on the Vernier Arduino 
 * Interface Shield or into an Analog Protoboard Adapter wired 
 * to Arduino pin A2.
 */

float rawCount; //create global variable for reading from A/D converter (0-1023)
float voltage; //create global variable for voltage (0-5V)
float phValue; //create global variable for sensor value
float slope = -3.90345; //create global variable for slope for a pH Sensor 0-14 range
float intercept = 13.72; //create global variable for intercept for a Dual-Range Force Sensor 0-14 range
 
void setup() {
  Serial.begin(9600); //setup communication to display
}

void loop() {
  
  rawCount=analogRead(A0); //read one data value (0-1023)
  voltage=rawCount/1023*5; //convert raw count to voltage (0-5V)
  phValue=slope*voltage+intercept; //convert to sensor value with linear calibration equation
  //Serial.println(voltage);  //prints sensor voltage to serial monitor for calibration 
  Serial.println(phValue); //print sensor value 
  delay(500); //wait half second
}
