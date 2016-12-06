#The class StaffMember is the superclass
class StaffMember:
    def __init__(self):
        pass
    def sign_in(self):
        pass
    def report_lost_item(self):
        pass
    def report_found_item(self):
        pass
class Admin(StaffMember):
    def __init__(self):
        pass
    def add_asset(self):
        pass
    def assign_asset(self):
        pass
    def unassign_asset(self):
        pass
    def see_assigned(self):
        pass
    def remind_due(self):
        pass
    def view_lost_items(self):
        pass
    def resolve_lost(self):
        pass
class SuperAdmin(Admin):
    def add_admin(self):
        pass