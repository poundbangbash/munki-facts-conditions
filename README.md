# Community Facts for [munki-facts](https://github.com/munki/munki-facts) Use

## Adobe software install check
  * Check if certain versions of an Adobe title is installed.  
  * We use it to dynamically check if an install for specific add-ins to specific title of software is needed.  In our case, font management has a plugin for specific titles of a software suite.  If the suite application is installed we want to install the associated plugin.
  
## Shard
  * Sets a shard value for the hardware based on the hardware serial number.
  * If /usr/local/shard/production exists when this is run the shard value will always be set to 100.
  * If /usr/local/shard/testing exists when this is run the shard value will always be set to 1.
