// const int NUM_SLIDERS = 1;
// const int analogInputs[NUM_SLIDERS] = {A0};
 
 const int NUM_SLIDERS = 2;
 const int analogInputs[NUM_SLIDERS] = {A0, A1};
 const int min_val = 20;
 const int mvc_apply[NUM_SLIDERS] = {1,1};

// const int NUM_SLIDERS = 2;
// const int analogInputs[NUM_SLIDERS] = {A0, A1};

// const int NUM_SLIDERS = 4;
// const int analogInputs[NUM_SLIDERS] = {A0, A1, A2, A3};


// const int NUM_SLIDERS = 12;
// const int analogInputs[NUM_SLIDERS] = {A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11};

int analogSliderValues[NUM_SLIDERS];

void setup() { 
  for (int i = 0; i < NUM_SLIDERS; i++) {
    pinMode(analogInputs[i], INPUT);
  }

  Serial.begin(9600);
}

void loop() {
  updateSliderValues();
  sendSliderValues(); // Actually send data (all the time)
  //printSliderValues(); // For debug
  //delay(10); // wait 10 ms
    //delay(5);
  delay(10);
}

void updateSliderValues() {
  for (int i = 0; i < NUM_SLIDERS; i++) {
    analogSliderValues[i] = analogRead(analogInputs[i]);
  }
}

void sendSliderValues() {
  String builtString = String("");

  for (int i = 0; i < NUM_SLIDERS; i++) {
    if(analogSliderValues[i] < mvc_apply[i] * min_val){
      analogSliderValues[i] = mvc_apply[i] * min_val;
    }
    builtString += String((int)analogSliderValues[i]);

    if (i < NUM_SLIDERS - 1) {
      builtString += String("|");
    }


  }
  
  Serial.println(builtString);
}

void printSliderValues() {
  for (int i = 0; i < NUM_SLIDERS; i++) {
    String printedString = String("Slider #") + String(i + 1) + String(": ") + String(analogSliderValues[i]) + String(" mV");
    Serial.write(printedString.c_str());

    if (i < NUM_SLIDERS - 1) {
      Serial.write(" | ");
    } else {
      Serial.write("\n");
    }
  }
}