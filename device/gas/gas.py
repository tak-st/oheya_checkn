import wiringpi as wp

SPI_CH = 0
PIN_BASE=64
wp.mcp3002Setup(PIN_BASE, SPI_CH)

def get_gas():
    
    gasval = {"gas": wp.analogRead(PIN_BASE)}
    
    return gasval