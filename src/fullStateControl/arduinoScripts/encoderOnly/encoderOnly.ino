#if defined(ARDUINO) && ARDUINO >= 100
  #include "Arduino.h"
#else
  #include <WProgram.h>
#endif

#include <SPI.h>
#include "Encoder.h"

// define some variables for the encoders
float motorEncData = 0;
float motorEncPos = 0;
float armEncData = 0;
float armEncPos = 0;
float calibArmEnc = 0;

// previous enc values
float motorEncPosOld = 0;
float armEncPosOld = 0;

// enc velocities
float motorEncVel = 0;
float armEncVel = 0;

void setup()
{  
  Serial.begin(9600);

  // initialize encoders
  initEncoders();
  clearEncoderCount();

  // do first read from encoders to zero them out
  motorEncData = readEncoder(1);
  motorEncPos = motorEncData * 360/(64 * 26.9 * 4);
  
  delay(1);

  armEncData = readAS5147P(2);
  armEncData = armEncData * 360 / 16383;
  calibArmEnc = armEncData; //we need to subtract this off every time to zero out arm enc
  armEncPos = (armEncData - calibArmEnc) * (-1);
}

long encVal = 0;
int armVal = 0;
void loop()
{
  encVal = readEncoder(1);
  Serial.print("enc1: ");
  Serial.print(encVal);
  armVal = readAS5147P(2);
  Serial.print(" enc2: ");
  Serial.println(armVal);
}

//void readEncoders()
//{
//  // read in from encoders and assign to x
//  // motor position
//  motorEncData = readEncoder(1);
//  motorEncPos = motorEncData * 360 / (64 * 26.9 * 4);
//
////  // arm position
////  armEncData = readAS5147P(2);
////  armEncPos = armEncData * 360 / 16383;
////  armEncPos = (armEncPos - calibArmEnc) * (-1); //SEA 1
//
//  //motor velocity
//  motorEncVel = (motorEncData - motorEncPosOld); /// dt;
//
////  //arm velocity
////  armEncVel = (armEncData - armEncPosOld); /// dt;
//
//  // set encoder positions to old
//  motorEncPosOld = motorEncData;
////  armEncPosOld = armEncData;
//
//  //publish values
//  Serial.println(motorEncPos);
//}
