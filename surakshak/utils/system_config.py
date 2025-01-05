import threading
import time 
import datetime
import logging 
from surakshak.utils.inference_engine import InferenceEngine

logger = logging.getLogger(__name__)

class SystemConfig:
    instrusion_state = ""

    @classmethod
    def set_intrusion(cls, val):
        cls.instrusion_state = val 
    
    @classmethod
    def get_intrusion(cls):
        return cls.instrusion_state
    
    @classmethod
    def start_state_switch(cls, InferenceSchedule):
        thread = threading.Thread(target=state_switch, daemon=True, name="State Switch", args=[InferenceSchedule])
        thread.start()
    
    @classmethod 
    def toggle(cls):
        if cls.instrusion_state == "ACTIVE":
            cls.instrusion_state = "INACTIVE"
            InferenceEngine.stop()
        elif cls.instrusion_state == "INACTIVE":
            cls.instrusion_state = "ACTIVE"
            InferenceEngine.start()

def state_switch(InferenceSchedule):
    while True:
        logger.info("Running periodic state switch.")
        inactive_schedule = InferenceSchedule.objects.get(pk=1)
        now_time = datetime.datetime.now()
        now_hour = now_time.hour
        now_min = now_time.min 
        now_weekday = now_time.weekday()
        mappings = {
        0: "monday", 1:"tuesday", 2: "wednesday", 3: "thursday", 4:"friday", 5:"saturday", 6:"sunday"
        }
        now_weekday_name = mappings[now_weekday]
        if getattr(inactive_schedule, now_weekday_name):
            # switch does not care about closed days
            inactive_schedule_start_hour = inactive_schedule.start_time.hour
            inactive_schedule_start_min = inactive_schedule.start_time.minute

            inactive_schedule_end_hour = inactive_schedule.end_time.hour
            inactive_schedule_end_min = inactive_schedule.end_time.minute

            if (now_hour, now_min) == (inactive_schedule_start_hour, inactive_schedule_start_min):
                SystemConfig.set_intrusion("INACTIVE")
                logger.info("System state switched to INACTIVE. Logger sleeping for 120 seconds.")
                # turn off inference engine 
                InferenceEngine.stop()
                time.sleep(120)
                continue 
            if (now_hour, now_min) == (inactive_schedule_end_hour, inactive_schedule_end_min):
                SystemConfig.set_intrusion("ACTIVE")
                logger.info("System state switched to ACTIVE. Logger sleeping for 120 seconds.")
                # turn on inference engine 
                InferenceEngine.start()
                time.sleep(120)
                continue 
        time.sleep(20)
        continue
        
                
            
    
