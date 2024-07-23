#export LENSTOOL_DIR=/home/joseph/Software/lenstool
export LENSTOOL_JA_DIR=/home/joseph/Software/Lenstool_JA
export LD_LIBRARY_PATH=$LENSTOOL_JA_DIR/lib:$LD_LIBRARY_PATH
export PYTHONPATH="${PYTHONPATH}:${LENSTOOL_JA_DIR}"

#export CODESDIR=/home/joseph/Work/Codes
#export PYTHONPATH="${PYTHONPATH}:${CODESDIR}"

export CFITSIO_PATH=/home/joseph/Software/cfitsio
export PATH=$PATH:$CFITSIO_PATH:
export LD_LIBRARY_PATH=$CFITSIO_PATH/lib/:$LD_LIBRARY_PATH
export INCLUDE=$CFITSIO_PATH/include/:$INCLUDE
