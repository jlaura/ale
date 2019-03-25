from collections import namedtuple
from unittest import mock

import pytest

import ale
from ale.drivers import mdis_driver, base
from ale.drivers.mdis_driver import MdisPDS3Driver

from conftest import SimpleSpice, get_mockkernels

@pytest.fixture
def mdislabel():
    return """
PDS_VERSION_ID       = PDS3

/*** FILE FORMAT ***/
RECORD_TYPE          = FIXED_LENGTH
RECORD_BYTES         = 2048
FILE_RECORDS          = 1028
LABEL_RECORDS         = 0004

/*** POINTERS TO START BYTE OFFSET OF OBJECTS IN IMAGE FILE ***/
^IMAGE                = 0005

/*** GENERAL DATA DESCRIPTION PARAMETERS ***/
MISSION_NAME         = "MESSENGER"
INSTRUMENT_HOST_NAME = "MESSENGER"
DATA_SET_ID          = "MESS-E/V/H-MDIS-2-EDR-RAWDATA-V1.0"
DATA_QUALITY_ID      = "0000000000000000"
PRODUCT_ID           = "EN0024934993M"
PRODUCT_VERSION_ID   = "3"
SOURCE_PRODUCT_ID    = ("0024934993_IM3WV")
PRODUCER_INSTITUTION_NAME = "APPLIED COHERENT TECHNOLOGY CORPORATION"
SOFTWARE_NAME        = "MDIS2EDR"
SOFTWARE_VERSION_ID  = "1.0"
MISSION_PHASE_NAME   = "EARTH CRUISE"
TARGET_NAME          = "EARTH"
SEQUENCE_NAME        = "05138_MLA_SUPP_1"
OBSERVATION_ID       = "703"
OBSERVATION_TYPE     = "N/A"
SITE_ID              = "N/A"

/*** TIME PARAMETERS ***/
START_TIME           = 2005-05-18T20:24:10.515023
STOP_TIME            = 2005-05-18T20:24:10.707023
SPACECRAFT_CLOCK_START_COUNT = "1/0024934993:798000"
SPACECRAFT_CLOCK_STOP_COUNT = "1/0024934993:990000"
ORBIT_NUMBER         = "N/A"
PRODUCT_CREATION_TIME = 2011-11-21T22:17:22

/***  INSTRUMENT ENGINEERING PARAMETERS ***/
INSTRUMENT_NAME      = "MERCURY DUAL IMAGING SYSTEM NARROW ANGLE CAMERA"
INSTRUMENT_ID        = "MDIS-NAC"
FILTER_NAME          = "748 BP 53"
FILTER_NUMBER        = "N/A"
CENTER_FILTER_WAVELENGTH = 747.7 <NM>
BANDWIDTH            = 52.6 <NM>
EXPOSURE_DURATION    = 192 <MS>
EXPOSURE_TYPE        = AUTO
DETECTOR_TEMPERATURE = -42.55 <DEGC>
FOCAL_PLANE_TEMPERATURE = -35.94 <DEGC>
FILTER_TEMPERATURE   = "N/A"
OPTICS_TEMPERATURE   = -37.36 <DEGC>

/*** INSTRUMENT RAW PARAMETERS ***/
MESS:MET_EXP         = 24934993
MESS:IMG_ID_LSB      = "N/A"
MESS:IMG_ID_MSB      = "N/A"
MESS:ATT_CLOCK_COUNT = 24934991
MESS:ATT_Q1          = 0.38073087
MESS:ATT_Q2          = -0.50538123
MESS:ATT_Q3          = 0.72235280
MESS:ATT_Q4          = 0.27899864
MESS:ATT_FLAG        = 7
MESS:PIV_POS_MOTOR   = "N/A"
MESS:PIV_GOAL        = 0
MESS:PIV_POS         = -1
MESS:PIV_READ        = 20740
MESS:PIV_CAL         = -26758
MESS:FW_GOAL         = 17376
MESS:FW_POS          = 17420
MESS:FW_READ         = 17420
MESS:CCD_TEMP        = 1026
MESS:CAM_T1          = 454
MESS:CAM_T2          = 478
MESS:EXPOSURE        = 192
MESS:DPU_ID          = 0
MESS:IMAGER          = 1
MESS:SOURCE          = 0
MESS:FPU_BIN         = 0
MESS:COMP12_8        = 0
MESS:COMP_ALG        = 2
MESS:COMP_FST        = 1
MESS:TIME_PLS        = 1
MESS:LATCH_UP        = 0
MESS:EXP_MODE        = 1
MESS:PIV_STAT        = 3
MESS:PIV_MPEN        = 0
MESS:PIV_PV          = 1
MESS:PIV_RV          = 1
MESS:FW_PV           = 1
MESS:FW_RV           = 1
MESS:AEX_STAT        = 256
MESS:AEX_STHR        = 0
MESS:AEX_TGTB        = 2800
MESS:AEX_BACB        = 240
MESS:AEX_MAXE        = 714
MESS:AEX_MINE        = 1
MESS:DLNKPRIO        = 3
MESS:WVLRATIO        = 4
MESS:PIXELBIN        = 0
MESS:SUBFRAME        = 0
MESS:SUBF_X1         = 4
MESS:SUBF_Y1         = 0
MESS:SUBF_DX1        = 0
MESS:SUBF_DY1        = 0
MESS:SUBF_X2         = 4
MESS:SUBF_Y2         = 0
MESS:SUBF_DX2        = 0
MESS:SUBF_DY2        = 0
MESS:SUBF_X3         = 0
MESS:SUBF_Y3         = 0
MESS:SUBF_DX3        = 0
MESS:SUBF_DY3        = 0
MESS:SUBF_X4         = 0
MESS:SUBF_Y4         = 0
MESS:SUBF_DX4        = 0
MESS:SUBF_DY4        = 0
MESS:SUBF_X5         = 0
MESS:SUBF_Y5         = 0
MESS:SUBF_DX5        = 0
MESS:SUBF_DY5        = 0
MESS:CRITOPNV        = 0
MESS:JAILBARS        = 0
MESS:JB_X0           = 0
MESS:JB_X1           = 0
MESS:JB_SPACE        = 0

/*** GEOMETRY INFORMATION ***/
RIGHT_ASCENSION      = 285.95273 <DEG>
DECLINATION          = 11.71507 <DEG>
TWIST_ANGLE          = 212.43017 <DEG>
RA_DEC_REF_PIXEL     = (512.00000,512.00000)
RETICLE_POINT_RA     = (286.18172 <DEG>,284.89969 <DEG>,287.00146 <DEG>,
  285.71292 <DEG>)
RETICLE_POINT_DECLINATION = (12.74731 <DEG>,11.95067 <DEG>,11.48768 <DEG>,
  10.68847 <DEG>)

/*** TARGET PARAMETERS ***/
SC_TARGET_POSITION_VECTOR = (-7282598.25457 <KM>,25612610.91152 <KM>,
  -5411326.66758 <KM>)
TARGET_CENTER_DISTANCE = 27172127.83986 <KM>

/*** TARGET WITHIN SENSOR FOV ***/
SLANT_DISTANCE       = "N/A"
CENTER_LATITUDE      = "N/A"
CENTER_LONGITUDE     = "N/A"
HORIZONTAL_PIXEL_SCALE = "N/A"
VERTICAL_PIXEL_SCALE = "N/A"
SMEAR_MAGNITUDE      = "N/A"
SMEAR_AZIMUTH        = "N/A"
NORTH_AZIMUTH        = "N/A"
RETICLE_POINT_LATITUDE = ("N/A","N/A","N/A","N/A")
RETICLE_POINT_LONGITUDE = ("N/A","N/A","N/A","N/A")

/*** SPACECRAFT POSITION WITH RESPECT TO CENTRAL BODY ***/
SUB_SPACECRAFT_LATITUDE = -11.49546 <DEG>
SUB_SPACECRAFT_LONGITUDE = 283.33197 <DEG>
SPACECRAFT_ALTITUDE  = 27165750.55671 <KM>
SUB_SPACECRAFT_AZIMUTH = "N/A"

/*** SPACECRAFT LOCATION ***/
SPACECRAFT_SOLAR_DISTANCE = 139069138.64129 <KM>
SC_SUN_POSITION_VECTOR = (-87690987.23333 <KM>,-92023335.85736 <KM>,
  -56411184.51298 <KM>)
SC_SUN_VELOCITY_VECTOR = (-24.04359 <KM/S>,19.51186 <KM/S>,7.92341 <KM/S>)

/*** VIEWING AND LIGHTING GEOMETRY (SUN ON TARGET) ***/
SOLAR_DISTANCE       = 151343022.60304 <KM>
SUB_SOLAR_AZIMUTH    = "N/A"
SUB_SOLAR_LATITUDE   = 19.70999 <DEG>
SUB_SOLAR_LONGITUDE  = 233.12030 <DEG>
INCIDENCE_ANGLE      = "N/A"
PHASE_ANGLE          = "N/A"
EMISSION_ANGLE       = "N/A"
LOCAL_HOUR_ANGLE     = "N/A"

/*** GEOMETRY FOR EACH SUBFRAME ***/
GROUP = SUBFRAME1_PARAMETERS
  RETICLE_POINT_LATITUDE = ("N/A","N/A","N/A","N/A")
  RETICLE_POINT_LONGITUDE = ("N/A","N/A","N/A","N/A")
END_GROUP = SUBFRAME1_PARAMETERS

GROUP = SUBFRAME2_PARAMETERS
  RETICLE_POINT_LATITUDE = ("N/A","N/A","N/A","N/A")
  RETICLE_POINT_LONGITUDE = ("N/A","N/A","N/A","N/A")
END_GROUP = SUBFRAME2_PARAMETERS

GROUP = SUBFRAME3_PARAMETERS
  RETICLE_POINT_LATITUDE = ("N/A","N/A","N/A","N/A")
  RETICLE_POINT_LONGITUDE = ("N/A","N/A","N/A","N/A")
END_GROUP = SUBFRAME3_PARAMETERS

GROUP = SUBFRAME4_PARAMETERS
  RETICLE_POINT_LATITUDE = ("N/A","N/A","N/A","N/A")
  RETICLE_POINT_LONGITUDE = ("N/A","N/A","N/A","N/A")
END_GROUP = SUBFRAME4_PARAMETERS

GROUP = SUBFRAME5_PARAMETERS
  RETICLE_POINT_LATITUDE = ("N/A","N/A","N/A","N/A")
  RETICLE_POINT_LONGITUDE = ("N/A","N/A","N/A","N/A")
END_GROUP = SUBFRAME5_PARAMETERS


OBJECT = IMAGE
  LINES              = 1024
  LINE_SAMPLES       = 1024
  SAMPLE_TYPE        = MSB_UNSIGNED_INTEGER
  SAMPLE_BITS        = 16
  UNIT               = "N/A"
  DARK_STRIP_MEAN    = 267.777

/*** IMAGE STATISTICS OF  ***/
/*** THE EXPOSED CCD AREA ***/
  MINIMUM            = 262.000
  MAXIMUM            = 2978.000
  MEAN               = 267.684
  STANDARD_DEVIATION = 17.810

/*** PIXEL COUNTS ***/
  SATURATED_PIXEL_COUNT = 0
  MISSING_PIXELS     = 0
END_OBJECT = IMAGE
END
    """

@pytest.fixture
def mdispds_driver():
  pool_keys = ['INS-12345_FL_UNCERTAINTY', 'INS-12345_FL_TEMP_COEFFS ', 'EARTH',
               'INS-12345_FPUBIN_START_LINE',
               'INS-12345_FPUBIN_START_SAMPLE']

  # Setup a kernel pool fixture for PDS3 driver testing
  simplespice = SimpleSpice(pool_keys)
  base.spice = simplespice
  mdis_driver.spice = simplespice
  MdisPDS3Driver.metakernel = get_mockkernels

def test_mdis_creation(mdispds_driver, mdislabel):
    with MdisPDS3Driver(mdislabel) as m:
        d = m.to_dict()
        assert isinstance(d, dict)
