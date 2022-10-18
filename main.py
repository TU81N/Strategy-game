#This is the building
class building:
    def __init__(self,hospital,Schools,Army,Businesses):
        self.hospital = hospital
        self.Schools = Schools
        self.Army = Army
        self.Businesses = Businesses


    def build(self):
        pass

#change name of Percentage
class Percentage:
    def __init__(self,given_morale,given_health,given_rank):
        self.given_morale = given_morale
        self.given_health = given_health
        self.given_rank = given_rank
    
    def Apply_percentage(self):
        pass

#what user has to do
class Actions:
    def __init__(self,announce_holidays,advertise_army,meet_others,invest_research):
        self.announce_holidays = announce_holidays
        self.advertise_army = advertise_army
        self.meet_others = meet_others              
        self.invest_research = invest_research   

    def do_actions(self):
        pass


class Warzone:
    def __init__(self,invest,weapons,salary,attacking,peace_treaty,land_available,positions_available,):
        
