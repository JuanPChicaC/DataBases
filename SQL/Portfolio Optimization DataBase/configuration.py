import json
import os 
import string
import random


def token_generator(size):
    
    chars=string.ascii_uppercase + string.digits
    
    return ''.join(
        random.choice(chars) for _ in range(size)
        )



class Environment_Configuration():
    """
    This class content all the required configuration to initialize the solutiuon
    """
    def __init__(self):
    
    
        self._production_exist = True if os.environ.get('production_environment') is not None else False
        self._uat_exist = True if os.environ.get('uat_environment') is not None else False


        if self._production_exist:
    
            self._production_trigger = os.environ.get('production_environment')
    
            if self._production_trigger not in [0,1]:
                raise Exception(
                        '''
                        the environment variable "production_environment" has to take the value of 0 or 1,
                        different value has no interpretation for the system
                        '''
                    )
            else:
                self._production_trigger = bool(
                        self._production_trigger
                    )

        if self._uat_exist:
            
            self._uat_trigger = os.environ.get('uat_environment')
            
            if self._uat_trigger not in [0,1]:
                raise Exception(
                        '''
                        the environment variable "uat_environment" has to take the value of 0 or 1,
                        different value has no interpretation for the system
                        '''
                    )
            else:
                self._uat_trigger = bool(
                        self._uat_trigger
                    )

        configuration_file = open (
            'config_parameters.json'
            )
        
        self.configuration_parameters = json.loads(
            configuration_file.read()
            )
        
        configuration_file.close()

        if self._production_exist and self._production_trigger and  self._uat_exist and  self._uat_trigger:
            
            raise Exception(
                '''
                The production and uat environment variables can´t be active at the same time.
                Take a llok on the configuration of the environment
                '''
                )
            
        elif self._production_exist and self._production_trigger:
            
            self.environment_status = 'production'
        
        elif self._uat_exist and  self._uat_trigger:
            
            self.environment_status = 'testing'
        else:
            
            self.environment_status = 'development'
            
        self.database = self.configuration_parameters[
            'db_configuration'
            ][
                self.environment_status
                ]