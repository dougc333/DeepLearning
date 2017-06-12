#!/bin/bash

echo "starting ssh command point browser to localhost:8888"

ssh -N -f -L localhost:8888:localhost:8889 dc@hadoop.is-very-good.org

