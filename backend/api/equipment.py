from fastapi import APIRouter, Depends
from ..models import Equipment
from ..services import EquipmentService

api = APIRouter(prefix="/api/equipment")


@api.get("", response_model=list[Equipment], tags=["Equipment"])
def list(equipment_svc: EquipmentService = Depends()):
    return equipment_svc.list()

@api.post("", tags=["Equipment"])
def add(equipment: Equipment, equipment_svc: EquipmentService = Depends()) -> None:
    return equipment_svc.add(equipment)

@api.delete("/{equipment_name}", tags=["Equipment"])
def delete(equipment_name: str, equipment_svc: EquipmentService = Depends()) -> None:
    return equipment_svc.delete(equipment_name)