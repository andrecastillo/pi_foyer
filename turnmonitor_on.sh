#!/bin/bash

// Turn on the monitor

sudo tvservice -p


// Im not 100% sure I know why this is needed but it solved a problem I was
// having where the montior would turn back on, but nothing would display, so
// here it is

sudo chvt 9 && sudo chvt 7
