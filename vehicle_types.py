from enum import Enum, auto

class VehicleType(Enum):
    """Enumeration of vehicle types based on license plate patterns."""
    TAXI = "Taxi"
    BUS = "Buses"
    METROBUS = "Metrobus"
    PRESS = "Prensa"
    JUDGE = "Jueces/Fiscales"
    PANAMA_CANAL = "Canal de Panama"
    RADIO_AMATEUR = "Radioaficionado"
    CONSULAR = "Cuerpo Consular"
    HONORARY = "Cuerpo Honorario"
    INTERNATIONAL = "Mision Internacional"
    INTERNAL_ROUTE = "Ruta Interna"
    PRIVATE = "Vehiculos particulares"
    MOTORCYCLE = "Motos"
    PRE_2013 = "vehiculos normales(antes del 2013)"
    UNKNOWN = "Tipo de vehículo desconocido"
