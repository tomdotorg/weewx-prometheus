## weewx prometheus pushgateway extension

this weewx extension enables you to send your weather data to a [prometheus](http://prometheus.io) [pushgateway](https://github.com/prometheus/pushgateway). additional information regarding prometheus and its use can be found on the associated web site.

## requirements

this extension requires the use of the `requests` package.

```
pip install requests
```

## installation

this extension can be easily installed using the weewx extensions installer.

1. download the extension from github:
	```
	wget https://github.com/sulrich/weewx-prompush/archive/v1.0.0.tar.gz
	```

2. install using the weewx extension utility
	```
	wee_extension --install v1.0.0.tar.gz
	```

3. update **weewx.conf** to appropriately tag weather data for submission into the prometheus pushgateway and subsequent scraping from prometheus.  note that **job** and **instance** names may be subject to relabeling depending on your prometheus environment.
	```
    [StdRESTful]
      [[PromPush]]
         job = PROMETHEUS_JOB_NAME
         instance = PROMETHEUS_INSTANCE_NAME
         host = PUSH_GW_HOST
         port = PUSH_GW_PORT
	```
	
`wee_extension` will add a boilerplate `[[PromPush]]` section to your config.  You need to edit it.
	

4. restart weewx

```
sudo /etc/init.d/weewx stop
sudo /etc/init.d/weewx start
```

## administravia
**author:** steve ulrich \<[sulrich@botwerks.org](mailto:sulrich@botwerks.org)\>  
**license:** Apache License, Version 2.0. See LICENSE.  
**source:** [https://github.com/sulrich/weewx-prompush](https://github.com/sulrich/weewx-prompush)  
