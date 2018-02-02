1) install history
installed NVIDIA cuda 9.0 
commented out install-gpu.sh cuda repo
AFTER errors in gpu-install.sh add conda create -n myenv python=3.4
AFTER errors in gpu-install.sh removed pip install theeano from gpu-install.sh; added conda install theano

commented out cuda.list dep repo under /etc/apt/sources.list.d; ran sudo apt update to make sure there is no cuda repo
bad: apt cache search cuda reveals older versions of nvidia cuda 7.5 and 8.0 polluting namespace. If you do apt-get install cuda you are in big trouble 
This creates confusing errors when installing from deb. Cause it leads to many errors. 
Cuda installation is not idempotent. Once you install cuda 9.1 you can't just uninstall it and install an older version assuming this is the
same as a clean kernel install. 


collabrative filter contrast with: https://github.com/NVIDIA/DeepRecommender
https://www.kaggle.com/abhishek/approaching-almost-any-nlp-problem-on-kaggle
http://ruder.io/word-embeddings-1/index.html
https://medium.com/@yaroslavvb/optimizing-deeper-networks-with-kfac-in-pytorch-4004adcba1b0
http://ruder.io/deep-learning-nlp-best-practices/index.html#layerconnections

https://github.com/maciejkula/netrex
