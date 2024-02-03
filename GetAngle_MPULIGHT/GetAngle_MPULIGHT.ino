/* Get tilt angles on X and Y, and rotation angle on Z
 * Angles are given in degrees
 * 
 * License: MIT
 */

#include "Wire.h"
#include <MPU6050_light.h>

String p1=";";
MPU6050 mpu(Wire);
unsigned long timer = 0;

int LED_BUILTIN = 2;

void setup() {
  Serial.begin(57600);
  pinMode (LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, HIGH);
  Wire.begin();
  
  byte status = mpu.begin();
  Serial.print(F("MPU6050 status: "));
  Serial.println(status);
  while(status!=0){ } // stop everything if could not connect to MPU6050
  
  Serial.println(F("Calculating offsets, do not move MPU6050"));
  delay(1000);
  // mpu.upsideDownMounting = true; // uncomment this line if the MPU6050 is mounted upside-down
  mpu.calcOffsets(); // gyro and accelero
  Serial.println("Done!\n");
}

void loop() {
  mpu.update();
  
  if((millis()-timer) > 100){ // print data every 50ms
    // Serial.print("Angle_Roll[°]:");
    // Serial.print(mpu.getAngleX());
    // Serial.print(",");
    // // Serial.print("Angle_Pitch[°]:");
    // Serial.print(mpu.getAngleY());
    // Serial.print(",");
    //Serial.print("Angle_Yaw[°]:");
    Serial.println(mpu.getAngleX() + p1 + mpu.getAngleY() + p1 + mpu.getAngleZ());
    //Serial.println(mpu.getAngleX(), mpu.getAngleY());
    timer = millis();  
  }

}