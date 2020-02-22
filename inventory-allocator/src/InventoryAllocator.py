"""
Author: Laith Adi 
Email: Laith_adi@hotmail.com
Phone: 647-920-4382
"""

"""
Few things to know:
    
    - I kept the class, testing code, and samples in one .py to make it easier to use
    - The class handles MULTIPLE orders at a time. Feel free to add/remove in as many orders and warehouses. The program will still work ;)
    - The class handles orders with quantity of 0 
    - A dashed line is used to separate each order 
    - A commented dashed line is used to separate the class, test code, and sample testing from each other 
"""

class InventoryAllocator:
    
    def __init__(self, order, warehouse):
        
        """
        def - define the order and warehouse locations as parameters for class
        order - order of the customer
        warehouse - warehouse locations to be inputed as a parameter by the tester/user of this code 
        """
        
        self.order = order
        self.warehouse = warehouse
        
        
    
    def availability(self, item, quantity):        
        """
        parameters: 
            item - the name of the item to be ordered 
            quantity - the amount of the item to be ordered 
        
        return:
            warehouses_list - a list of warehouse where the the order will be shipped from 
        """
        
        # defining variables used as counters (count, i)
        count = 0
        i = 0
        
        # defining an empty list so we can append warehouses if the warehouse has the order in its inventory 
        warehouses_list = []
        
        #set the list of warehouses as wareh just for clean coding practices 
        wareh = self.warehouse
        
        #keep looping as long as we havent reached the quantity that is order AND we have not passed the end of the self.warehouse locations  
        while count < quantity and i <= (len(wareh) - 1):
            
            # check if the first warehouse inventory contains the item
            # if the warehouse inventory contains the item (checking by the .get() method) 
            if wareh[i]['inventory'].get(item) != None:
                
                #add the warehouse to the list to be outputted since we know we are going to use this location  
                warehouses_list.append(wareh[i]) 
                
                # lets check if we need ALL the quanitity in the warehouse inventory 
                # if what we NEED to accomplish the quantity ordered is GREATER THAN or EQUAL to the amount of amount of inventory in stock, then use ALL of the stock in inventory
                if (quantity - count) >= wareh[i]['inventory'][item]:
                    
                    # adding the amount of stock we have in inventory to out count variable to keep track of how much of the order we still need 
                    count = count + wareh[i]['inventory'][item]
                
                # if the amount in inventory is GREATER than the amount needed to meet the order quantity, then we have more than enough. so we can just equate count to quantity
                else:
                    count = quantity 
                
            # incrementing i so when the code loops, we look at the NEXT location/warehouse 
            i += 1  
      
        # if we reach the end of the self.warehouse list or count is not less than quantity and count == quantity then we have the right amount in inventory to make the order
        if count == quantity:
            return warehouses_list 
        
        # if count is anyhing but equal to quantity
        else: 
            
            warehouses_list = []
            return warehouses_list
    
    
    
    def level_of_usage(self, item, quantity):
        """
        parameters:
            item - item name of specified order 
            quantity - amount of the item ordered 
        
        return:
            appropriate statement for the perticular inventory availability for the order
        """
        
        # count variable to keep track of the number of inventory we have in warehouses 
        #wareh is for easier coding practices so i dont have to type self.warehouse every time 
        count = 0
        wareh = self.warehouse
        
        # to saparete each warehouse in the list of warehouses, i use for loop to grab each index in the list
        for i in range(0, len(self.warehouse)):
            
            # warehouse has the item in inventory 
            if wareh[i]['inventory'].get(item) != None:
                
                # increment the count variable to keep track of how many we have in stock of the item 
                count += wareh[i]["inventory"][item]
                
                # if loop below is to check if we are going to use multiple warehouses to make the shipment
                if count >= quantity and i != 0 and i != len(self.warehouse) and wareh[0]["inventory"][item] < quantity:
                    print("Shipment is to come from multiple warehouses listed below!")
                    
        # following if statments are for printing the appropriete response to the comparessence of the quantity in the order to the amount we have in stock 
        if count == quantity:
            return print("Happy Case, exact inventory match!\n")
        elif count < quantity:
            return print("Not enough inventory -> no allocations!\n")
        else:
            return print("Shipment is to come from the warehouse listed below!\n")
        
        return (" ")
        
        
        
    def orderconfirmation(self):
        """
        def - separates each order and finds out whether shipment can be made and from which warehouse to ship from 
        """
        
        # take one order at a time to solve which warehouse to get the order from
        for i in range(0, len(self.order)):
            
            # using list() and .keys() to get all the keys in the self.order and places them in a list 
            #using the index 'i' from the for loop to place the first order name and quantity to their respective variables  
            order_item = list(self.order.keys())[i] 
            order_quantity = self.order[order_item]
            print("For the order of ", order_item, " of the amount ", order_quantity, ":\n")
            
            #check if the order is entered correctly 
            if order_quantity != 0:
    
                # seeing if the itemis available and in what sense 
                self.level_of_usage(order_item, order_quantity)
                #print("\n")
                
                # call the availability function to see if the ordered item is in stock and if so, where  
                print(self.availability(order_item, order_quantity))
                print("-------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            
            else:
                print("Double check the amount of quantity you are looking to purchase.")
                print("-------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
                
        return (" ")
                            
                        
                    
    

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# code for testing     
order = { "apple": 15, "orange": 3 } # add or remove any order you like 
warehouse = [{ "name": "owd", "inventory": { "apple": 10, "orange": 2 } }, { "name": "dm", "inventory": { "apple": 5, "orange": 3 }}] #add or remove any warehouse you like 

# following code just prints out the results 
res = InventoryAllocator(order, warehouse)
print(res.orderconfirmation())
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# few test cases 

"""
For order of  apple  of the amount  10 :

Shipment is to come from the warehouse listed below!

[{'name': 'owd', 'inventory': {'apple': 10, 'orange': 2}}]
-------------------------------------------------------------------------------------------------------------------------------------------------------------

For order of  orange  of the amount  2 :

Shipment is to come from the warehouse listed below!

[{'name': 'owd', 'inventory': {'apple': 10, 'orange': 2}}]
-------------------------------------------------------------------------------------------------------------------------------------------------------------
"""


"""
For the order of  apple  of the amount  0 :

Double check the amount of quantity you are looking to purchase.
-------------------------------------------------------------------------------------------------------------------------------------------------------------

For the order of  orange  of the amount  2 :

Shipment is to come from the warehouse listed below!

[{'name': 'owd', 'inventory': {'apple': 10, 'orange': 2}}]
-------------------------------------------------------------------------------------------------------------------------------------------------------------
"""


"""
For the order of  apple  of the amount  15 :

Shipment is to come from multiple warehouses listed below!
Happy Case, exact inventory match!

[{'name': 'owd', 'inventory': {'apple': 10, 'orange': 2}}, {'name': 'dm', 'inventory': {'apple': 5, 'orange': 3}}]
-------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------