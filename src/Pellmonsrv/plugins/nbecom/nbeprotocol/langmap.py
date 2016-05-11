#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
    Copyright (C) 2013  Anders Nylund

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
langmap = {
'auger-auto_calculation':'LNG_SETUP_BEREGNING',
'boiler-temp':'LNG_SETUP_BOILER',
'ignition-clear_ignitions':'LNG_SETUP_CLEAR_IGNITIONS',
'boiler-diff_over':'LNG_SETUP_DIFF_OVER',
'boiler-diff_under':'LNG_SETUP_DIFF_UNDER',
'alarm-output':'LNG_SETUP_ALARM_UDGANG',
'oxygen-block_time':'LNG_SETUP_BLOKER_VENTETID',
'hopper-distance_sensor':'LNG_SETUP_DISTANCE_SENSOR',
'hopper-distance_top':'LNG_SETUP_DRIFT_EKSTRA_1',
'hopper-distance_bottom':'LNG_SETUP_DRIFT_EKSTRA_2',
'hopper-auto_fill':'LNG_SETUP_DRIFT_EKSTRA_3',
'ignition-fan_50':'LNG_SETUP_EFFEKT_EL_MIDT',
'ignition-fan_10':'LNG_SETUP_EFFEKT_EL_START',
'ignition-fan_100':'LNG_SETUP_EFFEKT_EL_SLUT',
'fan-speed_100':'LNG_SETUP_EFFEKT_HOEJ',
'fan-speed_10':'LNG_SETUP_EFFEKT_LAV',
'fan-speed_50':'LNG_SETUP_EFFEKT_MIDT',
'auger-kw_min':'LNG_SETUP_EFFEKT_KW_MIN',
'auger-kw_max':'LNG_SETUP_EFFEKT_KW',
'regulation-power_per_minute':'LNG_SETUP_EFFEKT_PR_MINUT',
'cleaning-fan_speed':'LNG_SETUP_EFFEKT_RENS',
'boiler-ext_switch':'LNG_SETUP_EKSTERN_KONTAKT_AKTIV',
'boiler-ext_off_delay':'LNG_SETUP_EKSTERN_OFF_DELAY',
'boiler-ext_on_delay':'LNG_SETUP_EKSTERN_ON_DELAY',
'boiler-ext_stop_diff':'LNG_SETUP_EKSTERN_STOP_DIFF',
'boiler-ext_stop_temp':'LNG_SETUP_EKSTERN_STOP',
'ignition-power':'LNG_SETUP_EL_EFFEKT',
'ignition-pellets':'LNG_SETUP_EL_MOTOR',
'ignition-preheat_time':'LNG_SETUP_EL_STARTPULS',
'ignition-max_time':'LNG_SETUP_EL_TID',
'ignition-ignition_number':'LNG_SETUP_ELTAEND_ANTAL',
'misc-expansion_module':'LNG_SETUP_EXTENSION_BOARD',
'auger-forced_run':'LNG_SETUP_FYLDER_SNEGL',
'regulation-dhw_gain_i':'LNG_SETUP_GAIN_I_VVB',
'regulation-boiler_gain_i':'LNG_SETUP_GAIN_I',
'regulation-dhw_gain_p':'LNG_SETUP_GAIN_P_VVB',
'regulation-boiler_gain_p':'LNG_SETUP_GAIN_P',
'oxygen-o2_high':'LNG_SETUP_ILT_HOEJ',
'oxygen-start_calibrate':'LNG_SETUP_ILT_KALIBRERING',
'oxygen-o2_low':'LNG_SETUP_ILT_LAV',
'oxygen-o2_medium':'LNG_SETUP_ILT_MIDT',
'oxygen-regulation':'LNG_SETUP_ILT_STYRING',
'sun-input_collector':'LNG_SETUP_INDGANG_FANGER_1',
'sun-input_collector_2':'LNG_SETUP_INDGANG_FANGER_2',
'sun-input_excess':'LNG_SETUP_INDGANG_OVERSKUDSVARME',
'sun-input_dhw':'LNG_SETUP_INDGANG_VVB',
'hopper-content':'LNG_SETUP_INDHOLD_MAGASIN',
'weather-input_forward':'LNG_SETUP_INPUT_FORWARD_PUMPE',
'weather-input_reference':'LNG_SETUP_INPUT_REFERENCE_PUMPE',
'hopper-auger_capacity':'LNG_SETUP_KAPACITET_KG',
'regulation-dhw_setpoint_addition':'LNG_SETUP_KEDEL_TILLAEG_VVB',
'auger-runs_minute':'LNG_SETUP_KOERSEL_PR_MINUT',
'cleaning-comp_fan_speed':'LNG_SETUP_KOMP_RENS_EFFEKT',
'cleaning-comp_period':'LNG_SETUP_KOMP_RENS_PERIODE',
'cleaning-valve_time':'LNG_SETUP_KOMP_RENS_PULSTID',
'cleaning-valve_period':'LNG_SETUP_KOMP_RENS_TID',
'cleaning-pellets_stop':'LNG_SETUP_KOMP_RENS_VENTETID',
'cleaning-output_boiler1':'LNG_SETUP_KOMP_RENS_VENTIL1',
'cleaning-output_boiler2':'LNG_SETUP_KOMP_RENS_VENTIL2',
'oxygen-corr_fan_10':'LNG_SETUP_KORREKTION_10',
'oxygen-corr_fan_50':'LNG_SETUP_KORREKTION_50',
'oxygen-corr_fan_100':'LNG_SETUP_KORREKTION_100',
'oxygen-fan_gain_i':'LNG_SETUP_KORREKTION_ILT_I',
'oxygen-fan_gain_p':'LNG_SETUP_KORREKTION_ILT_P',
'oxygen-regulation_time':'LNG_SETUP_KORREKTION_PERIODE',
'oxygen-lambda_type':'LNG_SETUP_LAMBDASONDE_TYPE',
'pump-flow_liters':'LNG_SETUP_LITER_PR_PULS',
'auger-auger_100':'LNG_SETUP_MAETNING_HOEJ',
'auger-auger_10':'LNG_SETUP_MAETNING_LAV',
'auger-auger_50':'LNG_SETUP_MAETNING_MIDT',
'auger-min_dose':'LNG_SETUP_MAETNING_PR_GANG',
'regulation-boiler_power_max':'LNG_SETUP_MAX_EFFEKT',
'alarm-max_shaft_temp':'LNG_SETUP_MAX_SKAKT',
'sun-dhw_max_temp':'LNG_SETUP_MAX_VVB_TEMPERATUR',
'hopper-min_content':'LNG_SETUP_MIN_BEHOLDNING',
'regulation-boiler_power_min':'LNG_SETUP_MIN_EFFEKT',
'alarm-min_boiler_temp':'LNG_SETUP_MIN_KEDEL',
'auger-min_dose':'LNG_SETUP_MIN_MAETNING_PR_GANG',
'boiler-min_return':'LNG_SETUP_MIN_RETURN',
'pump-flow_freq':'LNG_SETUP_PULSER_PR_LITER',
'pump-start_temp_run':'LNG_SETUP_PUMPE_START',
'pump-start_temp_idle':'LNG_SETUP_PUMPE_STOP',
'cleaning-fan_period':'LNG_SETUP_RENS_PERIODE',
'cleaning-fan_time':'LNG_SETUP_RENS_TID',
'cleaning-output_ash':'LNG_SETUP_RENS_UDGANG_ASKESNEGL',
'misc-smoke_sensor':'LNG_SETUP_ROEG_TYPE',
'ignition-exhaust_speed':'LNG_SETUP_ROGSUGER_EFFEKT_EL',
'fan-exhaust_100':'LNG_SETUP_ROGSUGER_EFFEKT_HOEJ',
'fan-exhaust_10':'LNG_SETUP_ROGSUGER_EFFEKT_LAV',
'fan-exhaust_50':'LNG_SETUP_ROGSUGER_EFFEKT_MIDT',
'fan-output_exhaust':'LNG_SETUP_ROGSUGER_UDGANG',
'fan-alarm_fan_rpm':'LNG_SETUP_RPM_ALARM_AKTIV',
'fan-use_fan_rpm':'LNG_SETUP_RPM_BLAESER',
'misc-shaft_sensor':'LNG_SETUP_SKAKT_TYPE',
'sun-flow_liters':'LNG_SETUP_SOL_LITER_PR_PULS',
'sun-collector_temp':'LNG_SETUP_SOLFANGER_TEMPERATUR',
'sun-pump_min_speed':'LNG_SETUP_SOLPUMPE_MIN_HASTIGHED',
'sun-pump_start_diff':'LNG_SETUP_SOLPUMPE_START_DIFF',
'sun-pump_stop_diff':'LNG_SETUP_SOLPUMPE_STOP_DIFF',
'fan-alarm_fan_current':'LNG_SETUP_STROM_ALARM_AKTIV',
'cleaning-output_burner':'LNG_SETUP_UDGANG_KOMPRESSOR',
'sun-output_excess':'LNG_SETUP_UDGANG_OVERSKUDSVARME',
'pump-output':'LNG_SETUP_UDGANG_PUMPE',
'sun-output_pump':'LNG_SETUP_UDGANG_SOLFANGERPUMPE',
'hot_water-output':'LNG_SETUP_UDGANG_VVB',
'boiler-timer':'LNG_SETUP_UR_VARME_AKTIV',
'hot_water-timer':'LNG_SETUP_UR_VVB_AKTIV',
'weather2-active':'LNG_SETUP_VEJR_AKTIV_2',
'weather-active':'LNG_SETUP_VEJR_AKTIV',
'weather2-chill_weight':'LNG_SETUP_VEJR_CHILL_VAEGTNING_2',
'weather-chill_weight':'LNG_SETUP_VEJR_CHILL_VAEGTNING',
'weather2-pow_1':'LNG_SETUP_VEJR_EFFEKT1_2',
'weather2-pow_2':'LNG_SETUP_VEJR_EFFEKT2_2',
'weather2-pow_3':'LNG_SETUP_VEJR_EFFEKT3_2',
'weather2-pow_4':'LNG_SETUP_VEJR_EFFEKT4_2',
'weather2-pow_5':'LNG_SETUP_VEJR_EFFEKT5_2',
'weather2-pow_6':'LNG_SETUP_VEJR_EFFEKT6_2',
'weather2-pow_7':'LNG_SETUP_VEJR_EFFEKT7_2',
'weather-pow_1':'LNG_SETUP_VEJR_EFFEKT1',
'weather-pow_2':'LNG_SETUP_VEJR_EFFEKT2',
'weather-pow_3':'LNG_SETUP_VEJR_EFFEKT3',
'weather-pow_4':'LNG_SETUP_VEJR_EFFEKT4',
'weather-pow_5':'LNG_SETUP_VEJR_EFFEKT5',
'weather-pow_6':'LNG_SETUP_VEJR_EFFEKT6',
'weather-pow_7':'LNG_SETUP_VEJR_EFFEKT7',
'weather2-temp_1':'LNG_SETUP_VEJR_FREM1_2',
'weather2-temp_2':'LNG_SETUP_VEJR_FREM2_2',
'weather2-temp_3':'LNG_SETUP_VEJR_FREM3_2',
'weather2-temp_4':'LNG_SETUP_VEJR_FREM4_2',
'weather2-temp_5':'LNG_SETUP_VEJR_FREM5_2',
'weather2-temp_6':'LNG_SETUP_VEJR_FREM6_2',
'weather2-temp_7':'LNG_SETUP_VEJR_FREM7_2',
'weather-temp_1':'LNG_SETUP_VEJR_FREM1',
'weather-temp_2':'LNG_SETUP_VEJR_FREM2',
'weather-temp_3':'LNG_SETUP_VEJR_FREM3',
'weather-temp_4':'LNG_SETUP_VEJR_FREM4',
'weather-temp_5':'LNG_SETUP_VEJR_FREM5',
'weather-temp_6':'LNG_SETUP_VEJR_FREM6',
'weather-temp_7':'LNG_SETUP_VEJR_FREM7',
'weather2-avg_out_time':'LNG_SETUP_VEJR_MIDLING_UDETEMP_2',
'weather-avg_out_time':'LNG_SETUP_VEJR_MIDLING_UDETEMP',
'weather2-gain_p':'LNG_SETUP_VEJR_P_LED_2',
'weather-gain_p':'LNG_SETUP_VEJR_P_LED',
'weather2-ref_1':'LNG_SETUP_VEJR_UDE1_2',
'weather2-ref_2':'LNG_SETUP_VEJR_UDE2_2',
'weather2-ref_3':'LNG_SETUP_VEJR_UDE3_2',
'weather2-ref_4':'LNG_SETUP_VEJR_UDE4_2',
'weather2-ref_5':'LNG_SETUP_VEJR_UDE5_2',
'weather2-ref_6':'LNG_SETUP_VEJR_UDE6_2',
'weather2-ref_7':'LNG_SETUP_VEJR_UDE7_2',
'weather-ref_1':'LNG_SETUP_VEJR_UDE1',
'weather-ref_2':'LNG_SETUP_VEJR_UDE2',
'weather-ref_3':'LNG_SETUP_VEJR_UDE3',
'weather-ref_4':'LNG_SETUP_VEJR_UDE4',
'weather-ref_5':'LNG_SETUP_VEJR_UDE5',
'weather-ref_6':'LNG_SETUP_VEJR_UDE6',
'weather-ref_7':'LNG_SETUP_VEJR_UDE7',
'weather2-output_pump':'LNG_SETUP_VEJR_UDGANG_PUMPE_2',
'weather-output_pump':'LNG_SETUP_VEJR_UDGANG_PUMPE',
'weather2-output_up':'LNG_SETUP_VEJR_UDGANG_VENTIL_1_2',
'weather-output_up':'LNG_SETUP_VEJR_UDGANG_VENTIL_1',
'weather2-output_down':'LNG_SETUP_VEJR_UDGANG_VENTIL_2_2',
'weather-output_down':'LNG_SETUP_VEJR_UDGANG_VENTIL_2',
'hot_water-diff_under':'LNG_SETUP_VVB_DIFF',
'hot_water-dhw_remain':'LNG_SETUP_VVB_FORBLIV',
'regulation-dhw_power_max':'LNG_SETUP_VVB_MAXEFFEKT',
'regulation-dhw_power_min':'LNG_SETUP_VVB_MIN_EFFEKT',
'hot_water-temp':'LNG_SETUP_VVB_TEMP',
'cleaning-pressure_t7':'LNG_MAALING_AF_TRYKLUFT_T7',
'hot_water-dwh_weather2':'LNG_SETUP_VEJR_VVB_PAA_STRENG',
'hot_water-dwh_weather':'LNG_SETUP_VEJR_VVB_PAA_STRENG',
'oxygen-pellets_gain_p':'lng_settings_oxygen_pellets_gain_p',
'oxygen-pellets_gain_i':'lng_settings_oxygen_pellets_gain_i',
'oxygen-lambda_expansion_module':'lng_settings_oxygen_lambda_expansion_module',
'boiler-reduction':'LNG_SETUP_NATSAENKNING',

}
