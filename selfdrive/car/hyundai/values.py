from cereal import car
from selfdrive.car import dbc_dict
from selfdrive.config import Conversions as CV
from selfdrive.kegman_conf import kegman_conf
Ecu = car.CarParams.Ecu

# Steer torque limits
class SteerLimitParams:
  kegman = kegman_conf()
  STEER_MAX = int(kegman.conf['steerMax'])
  #STEER_MAX = 255 #255   # 409 is the max, 255 is stock
  STEER_DELTA_UP = int(kegman.conf['deltaUp'])
  STEER_DELTA_DOWN = int(kegman.conf['deltaDown'])
  STEER_DRIVER_ALLOWANCE = 50
  STEER_DRIVER_MULTIPLIER = 2
  STEER_DRIVER_FACTOR = 1

class LaneChangeParms:
  LANE_CHANGE_SPEED_MIN = 60 * CV.KPH_TO_MS
  LANE_CHANGE_TIME_MAX = 10
  
class CAR:
  AVANTE = "HYUNDAI AVANTE"
  SONATA = "HYUNDAI SONATA"
  SONATA_TURBO = "HYUNDAI SONATA Turbo"
  GRANDEUR = "HYUNDAI GRANDEUR"
  GRANDEUR_HEV = "HYUNDAI GRANDEUR Hybrid"
  GENESIS = "GENESIS"
  SANTAFE = "HYUNDAI SANTAFE"
  KONA = "HYUNDAI KONA"
  KONA_HEV = "HYUNDAI KONA Hybrid"
  KONA_EV = "HYUNDAI KONA ELECTRIC"
  IONIQ_HEV = "HYUNDAI IONIQ HYBRID"
  IONIQ_EV = "HYUNDAI IONIQ ELECTRIC"
  K5 = "KIA K5"
  K5_HEV = "KIA K5 Hybrid"
  K7 = "KIA K7"
  K7_HEV = "KIA K7 Hybrid"
  STINGER = "KIA STINGER"
  SORENTO = "KIA SORENTO"
  NIRO_HEV = "KIA NIRO Hybrid"
  NIRO_EV = "KIA NIRO ELECTRIC"
  NEXO = "HYUNDAI NEXO"
  MOHAVE = "KIA MOHAVE"
  I30 = "HYUNDAI I30"


class Buttons:
  NONE = 0
  RES_ACCEL = 1
  SET_DECEL = 2
  CANCEL = 4

FINGERPRINTS = {
  CAR.AVANTE: [{}],
  CAR.SONATA: [{}],
  CAR.SONATA_TURBO: [{}],
  CAR.GRANDEUR: [{
    67: 8, 68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 516: 8, 524: 8, 528: 8, 532: 8, 544: 8, 576: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 8, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 905: 8, 909: 8, 913: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 8, 1155: 8, 1156: 8, 1157: 4, 1162: 8, 1164: 8, 1168: 8, 1170: 8, 1173: 8, 1180: 8, 1186: 2, 1191: 2, 1193: 8, 1210: 8, 1225: 8, 1227: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 8, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1371: 8, 1378: 8, 1384: 8, 1407: 8, 1419: 8, 1427: 6, 1456: 4, 1470: 8
  },
  {
    67: 8, 68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 516: 8, 524: 8, 528: 8, 532: 8, 544: 8, 576: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 8, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 905: 8, 909: 8, 913: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 8, 1155: 8, 1156: 8, 1157: 4, 1162: 8, 1164: 8, 1168: 8, 1170: 8, 1173: 8, 1180: 8, 1186: 2, 1191: 2, 1193: 8, 1210: 8, 1225: 8, 1227: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 8, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1371: 8, 1378: 8, 1384: 8, 1407: 8, 1419: 8, 1427: 6, 1456: 4, 1470: 8
  },
  {
    67: 8, 68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 516: 8, 524: 8, 528: 8, 532: 8, 544: 8, 576: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 8, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 905: 8, 909: 8, 913: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 8, 1155: 8, 1156: 8, 1157: 4, 1162: 8, 1164: 8, 1168: 8, 1170: 8, 1173: 8, 1180: 8, 1186: 2, 1191: 2, 1193: 8, 1210: 8, 1225: 8, 1227: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 8, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1371: 8, 1378: 8, 1384: 8, 1407: 8, 1419: 8, 1427: 6, 1456: 4, 1470: 8
  }],
  CAR.GRANDEUR_HEV: [{}],
  CAR.GENESIS: [{}],
  CAR.SANTAFE: [{}],
  CAR.KONA: [{}],
  CAR.KONA_HEV: [{}],
  CAR.KONA_EV: [{}],
  CAR.IONIQ_HEV: [{}],
  CAR.IONIQ_EV: [{}],
  CAR.K5: [{}],
  CAR.K5_HEV: [{}],
  CAR.K7: [{}],
  CAR.K7_HEV: [{}],
  CAR.STINGER: [{}],
  CAR.NIRO_HEV: [{}],
  CAR.NIRO_EV: [{}],
  CAR.NEXO: [{}],
  CAR.MOHAVE: [{}],
  CAR.I30: [{}],
  CAR.SORENTO: [{}],
}

ECU_FINGERPRINT = {
  Ecu.fwdCamera: [832, 1156, 1191, 1342]
}

CHECKSUM = {
  "crc8": [CAR.SANTAFE],
  "6B": [CAR.SORENTO, CAR.GENESIS],
}

FEATURES = {
  "use_cluster_gears": [CAR.KONA, CAR.GRANDEUR, CAR.K7, CAR.MOHAVE, CAR.I30, CAR.AVANTE],  # Use Cluster for Gear Selection, rather than Transmission
  "use_tcu_gears": [CAR.K5, CAR.SONATA, CAR.SONATA_TURBO],  # Use TCU Message for Gear Selection
  "use_elect_gears": [CAR.K5_HEV, CAR.GRANDEUR_HEV, CAR.IONIQ_HEV, CAR.IONIQ_EV, CAR.NIRO_HEV, CAR.KONA_HEV, CAR.KONA_EV, CAR.NIRO_EV, CAR.NEXO],
}

DBC = {
  CAR.AVANTE: dbc_dict('hyundai_kia_generic', None),
  CAR.SONATA: dbc_dict('hyundai_kia_generic', None),
  CAR.SONATA_TURBO: dbc_dict('hyundai_kia_generic', None),
  CAR.GRANDEUR: dbc_dict('hyundai_kia_generic', None),
  CAR.GRANDEUR_HEV: dbc_dict('hyundai_kia_generic', None),
  CAR.GENESIS: dbc_dict('hyundai_kia_generic', None),
  CAR.SANTAFE: dbc_dict('hyundai_kia_generic', None),
  CAR.KONA: dbc_dict('hyundai_kia_generic', None),
  CAR.KONA_HEV: dbc_dict('hyundai_kia_generic', None),
  CAR.KONA_EV: dbc_dict('hyundai_kia_generic', None),
  CAR.IONIQ_HEV: dbc_dict('hyundai_kia_generic', None),
  CAR.IONIQ_EV: dbc_dict('hyundai_kia_generic', None),
  CAR.K5: dbc_dict('hyundai_kia_generic', None),
  CAR.K5_HEV: dbc_dict('hyundai_kia_generic', None),
  CAR.K7: dbc_dict('hyundai_kia_generic', None),
  CAR.K7_HEV: dbc_dict('hyundai_kia_generic', None),
  CAR.STINGER: dbc_dict('hyundai_kia_generic', None),
  CAR.NIRO_HEV: dbc_dict('hyundai_kia_generic', None),
  CAR.NIRO_EV: dbc_dict('hyundai_kia_generic', None),
  CAR.NEXO: dbc_dict('hyundai_kia_generic', None),
  CAR.MOHAVE: dbc_dict('hyundai_kia_generic', None),
  CAR.I30: dbc_dict('hyundai_kia_generic', None),
  CAR.SORENTO: dbc_dict('hyundai_kia_generic', None),
}

kegman = kegman_conf()
STEER_THRESHOLD = int(kegman.conf['threshold'])
