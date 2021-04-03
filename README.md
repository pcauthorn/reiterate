#reiteration
re(garding) iteration, this project is meant to collect tools to help developers iterate faster.

##tools
###_cache_

**situation**

You're interacting with a system that takes a long time

   ```Python
    def get_data_from_system_1(arg1, arg2):  # This would gathers data and takes multiple minutes
         ...

    def get_data_from_system_2(arg1, arg2):  # This would gathers data from another system and also takes multiple minutes
        ...    

    def sync_systems(d1, d2):  # this method takes less than a second
        # do something with the data
        ...
   ```


