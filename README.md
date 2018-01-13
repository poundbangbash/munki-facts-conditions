# Community Facts for [munki-facts](https://github.com/munki/munki-facts) Use

##Adobe software install check
  * Check if certain versions of an Adobe title is installed.  
  * For use when linking specific add-ins to specific versions of software (Font management plug-ins, etc.)
  
##Shard
  * Sets a shard value for the hardware based on the hardware serial number.
  * If /usr/local/shard/production exists when this is run the shard value will always be set to 100.
  * If /usr/local/shard/testing exists when this is run the shard value will always be set to 1.
