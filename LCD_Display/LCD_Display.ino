#include <LiquidCrystal.h>

// Initialize the library with the numbers of the interface pins
// Format: LiquidCrystal lcd(rs, enable, d4, d5, d6, d7)
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

void setup() {
  // Set up the LCD’s number of columns and rows
  lcd.begin(16, 2);

  // Print a message to the LCD
  lcd.print("Hello, World!");
}

void loop() {
  // Nothing needed here for a simple "Hello World" display
}
