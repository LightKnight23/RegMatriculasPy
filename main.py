"""
RegMatriculasPy - License Plate Validator for Panama Vehicles
This module validates Panamanian license plates and identifies the vehicle type.
"""

import re
from typing import Optional
import Modulos as mod
from vehicle_types import VehicleType

def validate_license_plate(plate: str) -> tuple[bool, Optional[VehicleType]]:
    """
    Validate a Panamanian license plate and return its vehicle type.
    
    Args:
        plate: The license plate number to validate
        
    Returns:
        A tuple containing (is_valid, vehicle_type)
        where is_valid is a boolean and vehicle_type is an optional VehicleType
    """
    patterns = {
        r'T[0-9]{5}$': VehicleType.TAXI,
        r'B[0-9]{5}$': VehicleType.BUS,
        r'MB[0-9]{4}$': VehicleType.METROBUS,
        r'PR[0-9]{4}$': VehicleType.PRESS,
        r'E[0-9]{5}$': VehicleType.JUDGE,
        r'CP[0-9]{4}$': VehicleType.PANAMA_CANAL,
        r'HP[0-9]{4}$': VehicleType.RADIO_AMATEUR,
        r'CC[0-9]{4}$': VehicleType.CONSULAR,
        r'6H[0-9]{4}$': VehicleType.HONORARY,
        r'MI[0-9]{4}$': VehicleType.INTERNATIONAL,
        r'RI[0-9]{4}$': VehicleType.INTERNAL_ROUTE,
        r'[A-C][A-Z][0-9]{4}$': VehicleType.PRIVATE,
        r'MA[0-9]{4}$': VehicleType.MOTORCYCLE,
        r'[0-9]{6}$': VehicleType.PRE_2013
    }
    
    for pattern, vehicle_type in patterns.items():
        if re.match(pattern, plate):
            return True, vehicle_type
            
    return False, None

def main() -> None:
    """Main function to run the license plate validation program."""
    plate = input("Introduzca un numero de matricula: ").strip().upper()

    is_valid, vehicle_type = validate_license_plate(plate)
    
    if is_valid and vehicle_type:
        print(mod.mensaje().format(plate), vehicle_type.value)
    else:
        print(mod.error().format(plate))

if __name__ == "__main__":
    main()