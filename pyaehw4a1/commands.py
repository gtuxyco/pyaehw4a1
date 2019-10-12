from enum import Enum

class ReadCommand(Enum):
    status = bytes([0xF4, 0xF5, 0x00, 0x40, 0x0C, 0x00, 0x00, 0x01, 0x01, 0xFE, 0x01, 0x00, 0x00, 0x66, 0x00, 0x00, 0x00, 0x01, 0xB3, 0xF4, 0xFB])

class UpdateCommand(Enum):
    on = bytes([0xF4, 0xF5, 0x00, 0x40, 0x29, 0x00, 0x00, 0x01, 0x01, 0xFE, 0x01, 0x00, 0x00, 0x65, 0x00, 0x00, 0x00, 0x00, 0x0C, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0xDF, 0xF4, 0xFB])
    off	= bytes([0xF4, 0xF5, 0x00, 0x40, 0x29, 0x00, 0x00, 0x01, 0x01, 0xFE, 0x01, 0x00, 0x00, 0x65, 0x00, 0x00, 0x00, 0x01, 0x04, 0x00, 0x00, 0x00, 0x00, 0x04, 0x01, 0x00, 0x00, 0x00, 00, 0x01, 0x00, 0x00, 0x01, 0x55, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0x31, 0xF4, 0xFB])
    mode_cool = bytes([0xF4, 0xF5, 0x00, 0x40, 0x29, 0x00, 0x00, 0x01, 0x01, 0xFE, 0x01, 0x00, 0x00, 0x65, 0x00, 0x00, 0x01, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 00, 0x00, 0x00, 0x00, 0x00, 0x54, 0x00, 0x10, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0x39, 0xF4, 0xFB])
    mode_heat = bytes([0xF4, 0xF5, 0x00, 0x40, 0x29, 0x00, 0x00, 0x01, 0x01, 0xFE, 0x01, 0x00, 0x00, 0x65, 0x00, 0x00, 0x01, 0x01, 0x30, 0x2F, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 00, 0x00, 0x00, 0x10, 0x01, 0x04, 0x00, 0x10, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0x59, 0xF4, 0xFB])
    mode_fan = bytes([0xF4, 0xF5, 0x00, 0x40, 0x29, 0x00, 0x00, 0x01, 0x01, 0xFE, 0x01, 0x00, 0x00, 0x65, 0x00, 0x00, 0x07, 0x01, 0x10, 0x33, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 00, 0x00, 0x00, 0x10, 0x01, 0x04, 0x00, 0x10, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0x43, 0xF4, 0xFB])
    mode_dry = bytes([0xF4, 0xF5, 0x00, 0x40, 0x29, 0x00, 0x00, 0x01, 0x01, 0xFE, 0x01, 0x00, 0x00, 0x65, 0x00, 0x00, 0x01, 0x01, 0x70, 0x33, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 00, 0x00, 0x00, 0x10, 0x01, 0x04, 0x00, 0x10, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0x9D, 0xF4, 0xFB])
    speed_mute = bytes([0xF4, 0xF5, 0x00, 0x40, 0x29, 0x00, 0x00, 0x01, 0x01, 0xFE, 0x01, 0x00, 0x00, 0x65, 0x00, 0x00, 0x03, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x30, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0x0B, 0xF4, 0xFB])
    speed_low = bytes([0xF4, 0xF5, 0x00, 0x40, 0x29, 0x00, 0x00, 0x01, 0x01, 0xFE, 0x01, 0x00, 0x00, 0x65, 0x00, 0x00, 0x05, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x10, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0xED, 0xF4, 0xFB])
    speed_med = bytes([0xF4, 0xF5, 0x00, 0x40, 0x29, 0x00, 0x00, 0x01, 0x01, 0xFE, 0x01, 0x00, 0x00, 0x65, 0x00, 0x00, 0x07, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x10, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0xEF, 0xF4, 0xFB])
    speed_max = bytes([0xF4, 0xF5, 0x00, 0x40, 0x29, 0x00, 0x00, 0x01, 0x01, 0xFE, 0x01, 0x00, 0x00, 0x65, 0x00, 0x00, 0x09, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x10, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0xF1, 0xF4, 0xFB])
    speed_auto = bytes([0xF4, 0xF5, 0x00, 0x40, 0x29, 0x00, 0x00, 0x01, 0x01, 0xFE, 0x01, 0x00, 0x00, 0x65, 0x00, 0x00, 0x01, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x10, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0xE9, 0xF4, 0xFB])
    temp_16_C = bytes([0xF4, 0xF5, 0x00, 0x40, 0x29, 0x00, 0x00, 0x01, 0x01, 0xFE, 0x01, 0x00, 0x00, 0x65, 0x00, 0x00, 0x00, 0x00, 0x00, 0x21, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0xF4, 0xF4, 0xF4, 0xFB])
    temp_17_C = bytes([0xF4, 0xF5, 0x00, 0x40, 0x29, 0x00, 0x00, 0x01, 0x01, 0xFE, 0x01, 0x00, 0x00, 0x65, 0x00, 0x00, 0x00, 0x00, 0x00, 0x23, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0xF6, 0xF4, 0xFB])
    temp_18_C = bytes([0xF4, 0xF5, 0x00, 0x40, 0x29, 0x00, 0x00, 0x01, 0x01, 0xFE, 0x01, 0x00, 0x00, 0x65, 0x00, 0x00, 0x00, 0x00, 0x00, 0x25, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0xF8, 0xF4, 0xFB])
    temp_19_C = bytes([0xF4, 0xF5, 0x00, 0x40, 0x29, 0x00, 0x00, 0x01, 0x01, 0xFE, 0x01, 0x00, 0x00, 0x65, 0x00, 0x00, 0x00, 0x00, 0x00, 0x27, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0xFA, 0xF4, 0xFB])
    temp_20_C = bytes([0xF4, 0xF5, 0x00, 0x40, 0x29, 0x00, 0x00, 0x01, 0x01, 0xFE, 0x01, 0x00, 0x00, 0x65, 0x00, 0x00, 0x00, 0x00, 0x00, 0x29, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0xFC, 0xF4, 0xFB])
    temp_21_C = bytes([0xF4, 0xF5, 0x00, 0x40, 0x29, 0x00, 0x00, 0x01, 0x01, 0xFE, 0x01, 0x00, 0x00, 0x65, 0x00, 0x00, 0x00, 0x00, 0x00, 0x2B, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0xFE, 0xF4, 0xFB])
    temp_22_C = bytes([0xF4, 0xF5, 0x00, 0x40, 0x29, 0x00, 0x00, 0x01, 0x01, 0xFE, 0x01, 0x00, 0x00, 0x65, 0x00, 0x00, 0x00, 0x00, 0x00, 0x2D, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0x00, 0xF4, 0xFB])
    temp_23_C = bytes([0xF4, 0xF5, 0x00, 0x40, 0x29, 0x00, 0x00, 0x01, 0x01, 0xFE, 0x01, 0x00, 0x00, 0x65, 0x00, 0x00, 0x00, 0x00, 0x00, 0x2F, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0x02, 0xF4, 0xFB])
    temp_24_C = bytes([0xF4, 0xF5, 0x00, 0x40, 0x29, 0x00, 0x00, 0x01, 0x01, 0xFE, 0x01, 0x00, 0x00, 0x65, 0x00, 0x00, 0x00, 0x00, 0x00, 0x31, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0x04, 0xF4, 0xFB])
    temp_25_C = bytes([0xF4, 0xF5, 0x00, 0x40, 0x29, 0x00, 0x00, 0x01, 0x01, 0xFE, 0x01, 0x00, 0x00, 0x65, 0x00, 0x00, 0x00, 0x00, 0x00, 0x33, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0x06, 0xF4, 0xFB])
    temp_26_C = bytes([0xF4, 0xF5, 0x00, 0x40, 0x29, 0x00, 0x00, 0x01, 0x01, 0xFE, 0x01, 0x00, 0x00, 0x65, 0x00, 0x00, 0x00, 0x00, 0x00, 0x35, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0x08, 0xF4, 0xFB])
    temp_27_C = bytes([0xF4, 0xF5, 0x00, 0x40, 0x29, 0x00, 0x00, 0x01, 0x01, 0xFE, 0x01, 0x00, 0x00, 0x65, 0x00, 0x00, 0x00, 0x00, 0x00, 0x37, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0x0A, 0xF4, 0xFB])
    temp_28_C = bytes([0xF4, 0xF5, 0x00, 0x40, 0x29, 0x00, 0x00, 0x01, 0x01, 0xFE, 0x01, 0x00, 0x00, 0x65, 0x00, 0x00, 0x00, 0x00, 0x00, 0x39, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0x0C, 0xF4, 0xFB])
    temp_29_C = bytes([0xF4, 0xF5, 0x00, 0x40, 0x29, 0x00, 0x00, 0x01, 0x01, 0xFE, 0x01, 0x00, 0x00, 0x65, 0x00, 0x00, 0x00, 0x00, 0x00, 0x3B, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0x0E, 0xF4, 0xFB])
    temp_30_C = bytes([0xF4, 0xF5, 0x00, 0x40, 0x29, 0x00, 0x00, 0x01, 0x01, 0xFE, 0x01, 0x00, 0x00, 0x65, 0x00, 0x00, 0x00, 0x00, 0x00, 0x3D, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0x10, 0xF4, 0xFB])
    temp_31_C = bytes([0xF4, 0xF5, 0x00, 0x40, 0x29, 0x00, 0x00, 0x01, 0x01, 0xFE, 0x01, 0x00, 0x00, 0x65, 0x00, 0x00, 0x00, 0x00, 0x00, 0x3F, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0x12, 0xF4, 0xFB])
    temp_32_C = bytes([0xF4, 0xF5, 0x00, 0x40, 0x29, 0x00, 0x00, 0x01, 0x01, 0xFE, 0x01, 0x00, 0x00, 0x65, 0x00, 0x00, 0x00, 0x00, 0x00, 0x41, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0x14, 0xF4, 0xFB])
    turbo_on = bytes([0xF4, 0xF5, 0x00, 0x40, 0x29, 0x00, 0x00, 0x01, 0x01, 0xFE, 0x01, 0x00, 0x00, 0x65, 0x00, 0x00, 0x01, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 00, 0x00, 0x00, 0x00, 0x00, 0x5C, 0x00, 0x10, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0x41, 0xF4, 0xFB])
    turbo_off = bytes([0xF4, 0xF5, 0x00, 0x40, 0x29, 0x00, 0x00, 0x01, 0x01, 0xFE, 0x01, 0x00, 0x00, 0x65, 0x00, 0x00, 0x01, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 00, 0x00, 0x00, 0x00, 0x00, 0x54, 0x00, 0x10, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0x39, 0xF4, 0xFB])
    energysave_on = bytes([0xF4, 0xF5, 0x00, 0x40, 0x29, 0x00, 0x00, 0x01, 0x01, 0xFE, 0x01, 0x00, 0x00, 0x65, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 00, 0x00, 0x00, 0x00, 0x00, 0x34, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0x07, 0xF4, 0xFB])
    energysave_off = bytes([0xF4, 0xF5, 0x00, 0x40, 0x29, 0x00, 0x00, 0x01, 0x01, 0xFE, 0x01, 0x00, 0x00, 0x65, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 00, 0x00, 0x00, 0x00, 0x00, 0x14, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0xE7, 0xF4, 0xFB])
    display_on = bytes([0xF4, 0xF5, 0x00, 0x40, 0x29, 0x00, 0x00, 0x01, 0x01, 0xFE, 0x01, 0x00, 0x00, 0x65, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xC0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0x93, 0xF4, 0xFB])
    display_off = bytes([0xF4, 0xF5, 0x00, 0x40, 0x29, 0x00, 0x00, 0x01, 0x01, 0xFE, 0x01, 0x00, 0x00, 0x65, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x40, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0x13, 0xF4, 0xFB])
    sleep_1 = bytes([0xF4, 0xF5, 0x00, 0x40, 0x29, 0x00, 0x00, 0x01, 0x01, 0xFE, 0x01, 0x00, 0x00, 0x65, 0x00, 0x00, 0x05, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x10, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0xEF, 0xF4, 0xFB])
    sleep_2 = bytes([0xF4, 0xF5, 0x00, 0x40, 0x29, 0x00, 0x00, 0x01, 0x01, 0xFE, 0x01, 0x00, 0x00, 0x65, 0x00, 0x00, 0x05, 0x05, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x10, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0xF1, 0xF4, 0xFB])
    sleep_3 = bytes([0xF4, 0xF5, 0x00, 0x40, 0x29, 0x00, 0x00, 0x01, 0x01, 0xFE, 0x01, 0x00, 0x00, 0x65, 0x00, 0x00, 0x05, 0x07, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x10, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0xF3, 0xF4, 0xFB])
    sleep_4 = bytes([0xF4, 0xF5, 0x00, 0x40, 0x29, 0x00, 0x00, 0x01, 0x01, 0xFE, 0x01, 0x00, 0x00, 0x65, 0x00, 0x00, 0x05, 0x09, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x10, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0xF5, 0xF4, 0xFB])
    sleep_off = bytes([0xF4, 0xF5, 0x00, 0x40, 0x29, 0x00, 0x00, 0x01, 0x01, 0xFE, 0x01, 0x00, 0x00, 0x65, 0x00, 0x00, 0x01, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x10, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0xE9, 0xF4, 0xFB])
    vert_dir = bytes([0xF4, 0xF5, 0x00, 0x40, 0x29, 0x00, 0x00, 0x01, 0x01, 0xFE, 0x01, 0x00, 0x00, 0x65, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 00, 0x00, 0x00, 0x01, 0x40, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0x14, 0xF4, 0xFB])
    vert_swing = bytes([0xF4, 0xF5, 0x00, 0x40, 0x29, 0x00, 0x00, 0x01, 0x01, 0xFE, 0x01, 0x00, 0x00, 0x65, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 00, 0x00, 0x00, 0x01, 0xC0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0x94, 0xF4, 0xFB])
    hor_dir = bytes([0xF4, 0xF5, 0x00, 0x40, 0x29, 0x00, 0x00, 0x01, 0x01, 0xFE, 0x01, 0x00, 0x00, 0x65, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 00, 0x00, 0x00, 0x00, 0x10, 0x00, 0x00, 0x00, 0x00, 0x14, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0xF7, 0xF4, 0xFB])
    hor_swing = bytes([0xF4, 0xF5, 0x00, 0x40, 0x29, 0x00, 0x00, 0x01, 0x01, 0xFE, 0x01, 0x00, 0x00, 0x65, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00, 0x00, 00, 0x00, 0x00, 0x00, 0x30, 0x00, 0x00, 0x00, 0x00, 0x14, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0x17, 0xF4, 0xFB])
