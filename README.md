Readme


CS 210 Assignment 1: Converter and Pixel System

This program completed does the following tasks:
- Ascii to Decimal Converter
- Number base converter supporting: Decimal, Binary, Octal, and Hexadecimal
- Program that reads and prints the images pixel values
- program that consumes the pixel values and creates an image
- Program testing boundary cases of the number base converter including the largest unsigned values, zero, and one negative two's complement value

This code requires Python and the pillow library.

Ascii to Decimal Converter

This converter works by taking a string and processing each character invidually to convert it to a decimal value. It does this by using the ord() function to find the decimal ascii value for each character and prints them in order.

Number Base Converter

This number base converter depicts numbers in binary,decimal,octal, and hexadecimals. It works by converting values to decimal using the value and position of each digit. It works by repeatedly dividing the number by the target base and uses the remainders to construct the result.

Image to Pixel Program

The image to pixel program opens an image and reads the values of each individual pixel. Each pixel is represented by its color value on the red green and blue scale. After, it prints the images data.

Pixel to Image Program

The pixel to image program does the reverse process of the image to pixel program by taking pixel values and using them to create an image. It places a pixel at the location and saves the result as a new file.

Boundary Case Testing

The boundary tests verify that the number converter with the various 32 bit values. These include zero, the largest unsigned value of 4.2 billion and a negative value using the 32 bit twos complement. 
