
#ID It is the record that controls the status of the shipment and delivery, for this reason it is the same.
test_data = [{"ID": "A123456789", "OLocation":"Sydney", "Dlocation":"Melbourne", "Weight":500, "IDVehiculo":"EXV25HJ", "IDCustomer":"ABC123"},                
    {"ID": "A123456780", "OLocation":"Sydney", "Dlocation":"Melbourne", "Weight":500, "IDVehiculo":"EXV30HJ", "IDCustomer":"ABC123"}]

vehicle_data = [{ "IDVehiculo":"EXV25HJ", "VehicleType" : "Truck", "VehicleCapacity" : "2000"},                
    { "IDVehiculo":"EXV30HJ", "VehicleType" : "Van", "VehicleCapacity" : "1200"},
    { "IDVehiculo":"EXV32HZ", "VehicleType" : "Car", "VehicleCapacity" : "400"}]

customer_data = [{ "IDCustomer":"ABC123", "Name" : "John Smith", " DateBirth" : "07/06/2001", "Address" : "123 Main St, Sydney, NSW 2000, Australia", "Phone" : "0420123456", "Email" : "john@example.com"}]             

delivery_data = [{ "ID":"A123456789", "Status" : "Delivered", "DeliveryDate" : "07/06/2001 14:32"},
                 { "ID":"A123456780", "Status" : "In transit", "DeliveryDate" : "07/06/2001 14:32"}]             


class FleetManagementMenu():
    #burned value for the validation test

    def __init__(self, selectOption):
        self.select_option = selectOption
    
    def options(self):
        self.create_new_shipment = "Create a new shipment"
        self.track_shipment = "Track a shipment"
        self.view_all_shipments = "View all shipments"
        self.quit_shipment_management = "Quit shipment management"
        print("1. " + self.create_new_shipment)
        print("2. " + self.track_shipment)
        print("3. " + self.view_all_shipments)
        print("4. " + self.quit_shipment_management)

    def addressMenu(self):

        if(self.select_option == 1):
            CreateNewShipment(test_data, vehicle_data, customer_data)
        if(self.select_option == 2):
            TrackShipment()
        if(self.select_option == 3):
            ViewAllShipments(test_data, delivery_data)
        if(self.select_option == 4):
            QuitFleetManagement()
        else:
            print(f"You selected option: {self.select_option}. Further actions for this option are not yet implemented.")

class CreateNewShipment():
    def __init__(self, test_data, vehicle_data, customer_data):
        print("Hello Create a new shipment")
        self.test_data = test_data
        self.vehicle_data = vehicle_data
        self.customer_data = customer_data
        self.checkShipmentID()

    def showAvailableVehicles(self, test_data):
        print("\n =========== VEHICLES FLEET LIST ==============")
        print("-------------------------------------------------")
        print("{:<15} {:<15} {:<15}".format("ID", "TYPE", "CAPACITY"))
        print("-------------------------------------------------")
        for veh in test_data:
            print("{:<15} {:<15} {:<15}".format(veh["IDVehiculo"], veh["VehicleType"], veh["VehicleCapacity"]))
        return True
    
    def showCustomerID(self, customer_data):
        print("\n =========== CUSTOMERS LIST ==============")
        print("-------------------------------------------------")
        print("{:<15} {:<15} {:<15}".format("ID", "NAME", "PHONE"))
        print("-------------------------------------------------")
        for cus in customer_data:
            print("{:<15} {:<15} {:<15}".format(cus["IDCustomer"], cus["Name"], cus["Phone"]))
        return True
    
    def showShipmentList(self, vehicle_data):
        print("\n =========== SHIPMENT LIST ==============")
        print("-------------------------------------------------")
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format("ID", "ORIGIN", "DESTINATION", "WEIGHT", "ID VEHICLE", "ID CUSTOMER"))
        print("-------------------------------------------------")
        for ship in vehicle_data:
            print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(ship["ID"], ship["OLocation"], ship["Dlocation"], ship["Weight"], ship["IDVehiculo"], ship["IDCustomer"]))
        return True

    def is_valid_shipment_id(self, shipment_id):
        if not 8 <= len(shipment_id) <= 12:
            return False
        for char in shipment_id:
            if not char.isalnum(): #Es necesario revisar la implemantacion de esta funcition
                return False
        return True

    def checkShipmentID(self):
        while True:
            shipmentID = input("Enter the new shipment ID: ")
            if not self.is_valid_shipment_id(shipmentID):
                print('Error: Invalid Shipment ID format. It must be alphanumeric and between 8 and 12 characters long.')
                continue 
            is_unique = True
            for i in self.test_data:
                if shipmentID == i['ID']:
                    print('Error: Shipment ID is not unique')
                    is_unique = False
                    break
            if is_unique:
                validData = True
                self.shipmentID = shipmentID
                self.checkOriginDestination(validData)
                break
    
    def checkOriginDestination(self, validData):
         if validData:
            originLocation = input("Origen location: ")
            dlocation = input("Destination location: ")
            self.originLocation = originLocation
            self.dlocation = dlocation
            validData = True
            self.checkWeight(validData)

    def checkWeight(self, validData):
        if validData:
            weight = int(input("Weight: "))
            if weight < 0:
                validData = False
                print('Error: Invalid Weight')
                self.checkWeight(validData)
            else:
                validData = True
                self.weight = weight
                self.chooseAvailableVehicles()

    def checkAvailableVehicles(self, vehicleChoose, vehicle_data):
        for veh in vehicle_data:
            if (vehicleChoose == veh["IDVehiculo"]):
                return True
        return False

    def chooseAvailableVehicles(self):
        self.showAvailableVehicles(vehicle_data)
        vehicleChoose = input("Select a Vehicle ID from the list: ")
        if(self.checkAvailableVehicles(vehicleChoose, vehicle_data) == True):
            self.vehicleChoose = vehicleChoose
            self.registerShipmentCustomer()
        else:
            print("Vehicle ID Not exists.")
            self.chooseAvailableVehicles()

    def checkExistsCustomers(self, customerID, customer_data):
        for c in customer_data:
            if (c["IDCustomer"] == customerID):
                return True
            else:
                return False

    def registerShipmentCustomer(self):
        self.showCustomerID(customer_data)
        customerID = input("Register the customer ID for the Shipment: ")
        if(self.checkExistsCustomers(customerID, customer_data) == True):
            self.customerID = customerID
            self.createShipment(self.shipmentID, self.originLocation, self.dlocation, self.weight, self.vehicleChoose, self.customerID)
        else:
            print("Customer ID Not exists.")
            self.registerShipmentCustomer()

    def createShipment(self, shipmentID, originLocation, dlocation, weight, vehicleChoose, customerID):
        new_shipment = {
                "ID": shipmentID,
                "OLocation": originLocation,
                "Dlocation": dlocation,
                "Weight": weight,
                "IDVehiculo": vehicleChoose,
                "IDCustomer": customerID
        }
        test_data.append(new_shipment)
        self.showShipmentList(test_data)
        temp_men = FleetManagementMenu(0)
        temp_men.options()
            

class TrackShipment():
    def __init__(self):
        print("Hello Create a new shipment")
        self.test_data = test_data
        self.delivery_data = delivery_data
        self.validateShipmentID()

    def showShipment(self, shipment_data):
        print("\n =========== SHIPMENT LIST ==============")
        print("-------------------------------------------------")
        print("{:<15} {:<15} {:<15}".format("ID", "Status", "Delivery Date"))
        print("-------------------------------------------------")
        print("{:<15} {:<15} {:<15}".format(shipment_data["ID"], shipment_data["Status"], shipment_data["DeliveryDate"]))
        return True
    
    def validateShipmentID(self):
        shipmentID = input("Enter the Shipment ID to track (or 'q' to quit): ")
        if shipmentID.lower() == 'q':
            temp_men = FleetManagementMenu(0)
            temp_men.options()
        else:
            if(self.checkIDShipment(shipmentID, delivery_data) == True):
                print("Customer ID Shipment.")
            else:
                print("Customer ID Not exists.")
                self.validateShipmentID()

    def checkIDShipment(self, shipmentID, delivery_data):
        for ship in delivery_data:
            if (ship["ID"] == shipmentID):
                self.showShipment(ship)
                temp_men = FleetManagementMenu(0)
                temp_men.options()

class ViewAllShipments():
    def __init__(self, test_data, delivery_data):
        print("Hello View all shipments")
        self.test_data = test_data
        self.delivery_data = delivery_data
        self.showAllShipments(test_data, delivery_data)
    
    def showAllShipments(self, test_data, delivery_data):
        print("\n =========== SHIPMENT LIST ==============")
        print("-------------------------------------------------")
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format("ID", "Origin", "Destination", "Weight", "Vehicle ID", "Status", "Delivery Date"))
        print("-------------------------------------------------")
        for ship in test_data:
            for deli in delivery_data:
                if (deli["ID"] == ship["ID"]):
                    print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(ship["ID"], ship["OLocation"], ship["Dlocation"], ship["Weight"], ship["IDVehiculo"], deli["Status"], deli["DeliveryDate"]))
    

class QuitFleetManagement():
    def __init__(self):
        exit

print("PLEASE SELECT AN OPTION FROM FLEET MANAGEMENT MENU (1-5):")
# Call the options method on the INSTANCE of FleetManagementMenu
temp_men = FleetManagementMenu(0)
temp_men.options()
selectedChoice = int(input())
fleet_menu = FleetManagementMenu(selectedChoice)


# Call the addressMenu method on the INSTANCE of FleetManagementMenu
fleet_menu.addressMenu()
