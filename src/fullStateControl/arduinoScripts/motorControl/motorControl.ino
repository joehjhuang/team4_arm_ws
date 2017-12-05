//define pin names
#define dir_1 3
#define pwm_1 5

int pwm_value=0; //Goes from 0-255

void setup() {
  // put your setup code here, to run once:
  pinMode(pwm_1,OUTPUT);
  pinMode(dir_1,OUTPUT);
  pwm_value = 25;
  Serial.begin(9600);
}

void loop() {
  //controls the direction the motor
  digitalWrite(dir_1,HIGH);
  
  //controls the speed of the motor
  analogWrite(pwm_1,pwm_value);
  
  Serial.println(pwm_value); //Display the value of PWM
  delay(750);
  digitalWrite(dir_1,LOW);
  
  delay(750);

}
