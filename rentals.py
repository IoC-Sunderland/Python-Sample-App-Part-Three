"""All vehicle rentals
"""

from inventory import VehicleInventory


class RentalLog:  # pylint: disable=too-few-public-methods
    """Holds a list of all current rentals"""
    CURRENT_RENTALS = []


class RentVehicle:  # pylint: disable=too-few-public-methods
    """ Add Vehicle to current rentals i.e. vehicles out for rent
        and remove from Vehicle Inventory """

    def __init__(self, index_of_vehicle__to_rent):
        # Get the Vehicle object from Vehicle Inventory
        vehicle_for_rent = VehicleInventory \
            .ALL_VEHICLES[index_of_vehicle__to_rent]
        # Remove from Vehicle Inventory
        VehicleInventory.ALL_VEHICLES.remove(vehicle_for_rent)
        # Add to Vehicle to Rental Log
        RentalLog.CURRENT_RENTALS.append(vehicle_for_rent)


class Rentee():  # pylint: disable=too-few-public-methods
    """ A Rentee Class """
    def __init__(self):
        pass


class RentalRates():  # pylint: disable=too-few-public-methods
    """ A Rental_Rates """
    def __init__(self):
        pass
