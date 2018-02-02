#!/bin/bash

ssh -N -f -L localhost:8888:localhost:8080 dc@192.168.0.11

