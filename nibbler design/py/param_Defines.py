import math
# // DECLARE CONSTANTS
NIBBLER_P_NBITS         = 16                                 #// Bit width of datapath
NIBBLER_C_LOG_NBITS     = int( math.log(NIBBLER_P_NBITS,2) ) #// # of bits needed to index into subword
NIBBLER_C_LOG_NBITS_STR = str(NIBBLER_C_LOG_NBITS)
NIBBLER_C_N_OFF         = 32/NIBBLER_P_NBITS                 #// Number of total n-bit chunks per word. 
NIBBLER_C_OFFBITS       = int( math.log(NIBBLER_C_N_OFF,2) ) #// # of bits needed to index the n-bit chunks.
NIBBLER_C_OFFBITS_STR   = str(NIBBLER_C_OFFBITS)
NIBBLER_N_CTRL_SIGNALS  = 54
