#!/bin/bash

sudo apt install lm-sensors fancontrol
sudo sensors-detect
/etc/init.d/kmod start
sudo pwmconfig
sudo service fancontrol start
