#!/usr/bin/env python

"""
sample output from simulator

key          value               type
----------------------------------------
outHumidity  79.9980573766       gauge
maxSolarRad  960.080999341
altimeter    32.0845040681       guage
heatindex    32.4567414016       gauge
radiation    748.170598504       gauge
inDewpoint   31.0785251193       gauge
inTemp       63.0012950398       gauge
barometer    31.0999352459       gauge
windchill    32.4567414016
dewpoint     26.9867627099       gauge
windrun      1.20018113179e-05
rain         0.0                 gauge
humidex      32.4567414016       gauge
pressure     31.0999352459       gauge
ET           0.480818085118
rainRate     0.0                 gauge
usUnits      1
appTemp      28.2115054547       gauge
UV           10.4743883791       gauge
dateTime     1466708460.0
windDir      359.988202072       gauge
outTemp      32.4567414016       gauge
windSpeed    0.00032377056758    gauge
inHumidity   29.9974099203       gauge
windGust     0.0004618843668     gauge
windGustDir  359.986143469       gauge
cloudbase    2122.17697538       gauge

"""

weather_metrics = {
    'outHumidity':
        {'name':    'weewx_loop_outside_humidity_percent',        'type': 'gauge'},
    'maxSolarRad':
        {'name':    'weewx_loop_maxSolarRad_watts',               'type': 'gauge'},
    'altimeter':
        {'name':    'weewx_loop_altimeter_in',                    'type': 'gauge'},
    'heatindex':
        {'name':    'weewx_loop_heatindex_degrees_f',             'type': 'gauge'},
    'radiation':
        {'name':    'weewx_loop_radiation',                       'type': 'gauge'},
    'inDewpoint':
        {'name':    'weewx_loop_inside_dewpoint_degrees_f',       'type': 'gauge'},
    'inTemp':
        {'name':    'weewx_loop_inside_temp_degrees_f',           'type': 'gauge'},
    'barometer':
        {'name':    'weewx_loop_barometer_in',                    'type': 'gauge'},
    'windchill':
        {'name':    'weewx_loop_windchill_degrees_f',             'type': 'gauge'},
    'dewpoint':
        {'name':    'weewx_loop_dewpoint_degrees_f',              'type': 'gauge'},
    # 'windrun':
    'humidex':
        {'name':    'weewx_loop_humidex_degrees_f',               'type': 'gauge'},
    'pressure':
        {'name':    'weewx_loop_pressure_in',                     'type': 'gauge'},
    # ET':
    'rainRate':
        {'name':    'weewx_loop_rain_rate_in_per_hour',           'type': 'gauge'},
    # 'usUnits':
    'appTemp':
        {'name':    'weewx_loop_apparent_temp_degrees_f',         'type': 'gauge'},
    'UV':
        {'name':    'weewx_loop_uv_index',                        'type': 'gauge'},
    # dateTime
    'windDir':
        {'name':    'weewx_loop_wind_speed_direction_degrees',    'type': 'gauge'},
    'outTemp':
        {'name':    'weewx_loop_outside_temp_degrees_f',          'type': 'gauge'},
    'windSpeed':
        {'name':    'weewx_loop_wind_speed_mph',                  'type': 'gauge'},
    'windSpeed10':
        {'name':    'weewx_loop_10_min_wind_speed_mph',           'type': 'gauge'},
    'inHumidity':
        {'name':    'weewx_loop_inside_humidity_percent',         'type': 'gauge'},
    'windGust':
        {'name':    'weewx_loop_wind_gust_mph',                   'type': 'gauge'},
    'windGustDir':
        {'name':    'weewx_loop_wind_gust_direction_degrees',     'type': 'gauge'},
    'cloudbase':
        {'name':    'weewx_loop_cloud_base_feet',                 'type': 'gauge'},
    'monthET':
        {'name':    'weewx_loop_month_evap_transipration',        'type': 'gauge'},
    'dayET':
        {'name':    'weewx_loop_day_evap_transipration',          'type': 'gauge'},
    'yearET':
        {'name':    'weewx_loop_year_evap_transipration',         'type': 'gauge'},
    'consBatteryVoltage':   
        {'name':    'weewx_loop_console_battery_volts',           'type': 'gauge'},
    'rain':
        {'name':    'weewx_loop_rain_in',                         'type': 'gauge'},
    'dayRain':
        {'name':    'weewx_loop_daily_rain_in',                   'type': 'gauge'},
    'monthRain':
        {'name':    'weewx_loop_monthly_rain_in',                 'type': 'gauge'},
    'yearRain':
        {'name':    'weewx_loop_yearly_rain_in',                  'type': 'gauge'},
    'stormRain':
        {'name':    'weewx_loop_storm_rain_in',                   'type': 'gauge'},
    'dateTime':
        {'name':    'weewx_loop_datetime_epoch_seconds',          'type': 'gauge'},
    'stormStart':
        {'name':    'weewx_loop_storm_start_epoch_seconds',       'type': 'gauge'},
    'insideAlarm':
        {'name':    'weewx_loop_inside_alarm',                    'type': 'gauge'},
    'sunrise':
        {'name':    'weewx_loop_sunrise_epoch_seconds',           'type': 'gauge'},
    'sunset':
        {'name':    'weewx_loop_sunset_epoch_seconds',            'type': 'gauge'},
    'extraTemp1':
        {'name':    'weewx_loop_extra_temp_1',                   'type': 'gauge'},
    'extraTemp2':
        {'name':    'weewx_loop_extra_temp_2',                   'type': 'gauge'},
    'extraTemp3':
        {'name':    'weewx_loop_extra_temp_3',                   'type': 'gauge'},
    'extraAlarm1':
        {'name':    'weewx_loop_extra_alarm_1',                   'type': 'gauge'},
    'extraAlarm2':
        {'name':    'weewx_loop_extra_alarm_2',                   'type': 'gauge'},
    'extraAlarm3':
        {'name':    'weewx_loop_extra_alarm_3',                   'type': 'gauge'},
    'extraAlarm4':
        {'name':    'weewx_loop_extra_alarm_4',                   'type': 'gauge'},
    'extraAlarm5':
        {'name':    'weewx_loop_extra_alarm_5',                   'type': 'gauge'},
    'extraAlarm6':
        {'name':    'weewx_loop_extra_alarm_6',                   'type': 'gauge'},
    'extraAlarm7':
        {'name':    'weewx_loop_extra_alarm_7',                   'type': 'gauge'},
    'extraAlarm8':
        {'name':    'weewx_loop_extra_alarm_8',                   'type': 'gauge'},
    'outsideAlarm1':
        {'name':    'weewx_loop_outside_alarm_1',                 'type': 'gauge'},
    'outsideAlarm2':
        {'name':    'weewx_loop_outside_alarm_2',                 'type': 'gauge'},
    'soilLeafAlarm1':
        {'name':    'weewx_loop_soil_leaf_alarm_1',               'type': 'gauge'},
    'soilLeafAlarm2':
        {'name':    'weewx_loop_soil_leaf_alarm_2',               'type': 'gauge'},
    'soilLeafAlarm3':
        {'name':    'weewx_loop_soil_leaf_alarm_3',               'type': 'gauge'},
    'soilLeafAlarm4':
        {'name':    'weewx_loop_soil_leaf_alarm_4',               'type': 'gauge'},
    'forecastRule':
        {'name':    'weewx_loop_forecast_rule',                   'type': 'gauge'},
    'rainAlarm':
        {'name':    'weewx_loop_rain_alarm',                      'type': 'gauge'},
    'trendIcon':
        {'name':    'weewx_loop_trend_icon',                      'type': 'gauge'},
    'forecastIcon':
        {'name':    'weewx_loop_forecast_icon',                   'type': 'gauge'},
    'usUnits':
        {'name':    'weewx_loop_us_units',                        'type': 'gauge'},
    'leafWet4':
        {'name':    'weewx_loop_leaf_wet_4',                      'type': 'gauge'},
    'txBatteryStatus':
        {'name':    'weewx_loop_tx_battery_status',               'type': 'gauge'}
}

__version__ = '1.1.0'

import weewx
import weewx.restx
import weeutil.weeutil

import requests

import Queue
import sys
import syslog

class PromPush(weewx.restx.StdRESTful):
    """

    sends weewx weather records to a prometheus pushgateway using the
    prometheus_client library

    """

    def __init__(self, engine, config_dict):
        super(PromPush, self).__init__(engine, config_dict)
        try:
            _prom_dict = weeutil.weeutil.accumulateLeaves(
                config_dict['StdRESTful']['PromPush'], max_level=1)
        except KeyError as e:
            logerr("config error: missing parameter %s" % e)
            return

        _manager_dict = weewx.manager.get_manager_dict(
            config_dict['DataBindings'], config_dict['Databases'], 'wx_binding')

        self.loop_queue = Queue.Queue()
        self.loop_thread = PromPushThread(self.loop_queue, _manager_dict,
                                          **_prom_dict)
        self.loop_thread.start()
        self.bind(weewx.NEW_LOOP_PACKET, self.new_loop_packet)
        loginfo("data will be sent to pushgateway at %s:%s" %
                (_prom_dict['host'], _prom_dict['port']))

    def new_loop_packet(self, event):
        self.loop_queue.put(event.packet)


class PromPushThread(weewx.restx.RESTThread):
    """
    thread for sending data to the configured prometheus pushgateway
    """

    DEFAULT_HOST = 'localhost'
    DEFAULT_PORT = '9091'
    DEFAULT_JOB = 'weewx'
    DEFAULT_INSTANCE = 'weewx-instance'
    DEFAULT_TIMEOUT = 10
    DEFAULT_MAX_TRIES = 3
    DEFAULT_RETRY_WAIT = 5

    def __init__(self, queue, manager_dict,
                 host=DEFAULT_HOST,
                 port=DEFAULT_PORT,
                 job=DEFAULT_JOB,
                 instance=DEFAULT_INSTANCE,
                 skip_post=False,
                 max_backlog=sys.maxint,
                 stale=60,
                 log_success=True,
                 log_failure=True,
                 timeout=DEFAULT_TIMEOUT,
                 max_tries=DEFAULT_MAX_TRIES,
                 retry_wait=DEFAULT_RETRY_WAIT):


        super(PromPushThread, self).__init__(
            queue,
            protocol_name='PromPush',
            manager_dict=manager_dict,
            max_backlog=max_backlog,
            stale=stale,
            log_success=log_success,
            log_failure=log_failure,
            timeout=timeout,
            max_tries=max_tries,
            retry_wait=retry_wait
        )

        self.host = host
        self.port = port
        self.job = job
        self.instance = instance
        self.skip_post = weeutil.weeutil.to_bool(skip_post)

    def post_metrics(self, data):
        # post the weather stats to the prometheus push gw
        pushgw_url = 'http://' + self.host + ":" + self.port + "/metrics/job/" + self.job

        if self.instance is not "":
            pushgw_url += "/instance/" + self.instance

        try:
            _res = requests.post(url=pushgw_url,
                                data=data,
                                headers={'Content-Type': 'application/octet-stream'})
            if 200 <= _res.status_code <= 299:
                # success
                # logdbg("pushgw post return code - %s" % _res.status_code)
                return
            else:
                # something went awry
                logerr("pushgw post error: %s" % _res.text)
                return

        except requests.ConnectionError, e:
            logerr("pushgw post error: %s" % e.message)


    def process_record(self, record, dbm):
        _ = dbm

        record_data = ''

        if self.skip_post:
            loginfo("-- prompush: skipping post")
        else:
            for key, val in record.iteritems():
                if val is None:
                    val = 0.0

                if weather_metrics.get(key):
                    # annotate the submission with the appropriate metric type.
                    # if there's no metric type supplied the pushgw will
                    # annotate with 'untyped'
#                    record_data += "# TYPE %s %s\n" % (str(weather_metrics[key]['name']), str(weather_metrics[key]['type']))
                    record_data += "# TYPE %s %s\n" % (str(weather_metrics[key]['name']), str(weather_metrics[key]['type']))
                    record_data += "%s %s\n" % (str(weather_metrics[key]['name']), str(val))
                else:
                    loginfo("missing field [%s] in defs" % (key))

        self.post_metrics(record_data)


#---------------------------------------------------------------------
# misc. logging functions
def logmsg(level, msg):
    syslog.syslog(level, 'prom-push: %s' % msg)

def logdbg(msg):
    logmsg(syslog.LOG_DEBUG, msg)

def loginfo(msg):
    logmsg(syslog.LOG_INFO, msg)

def logerr(msg):
    logmsg(syslog.LOG_ERR, msg)
