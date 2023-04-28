from fastapi import APIRouter, Depends, HTTPException
from ..models import Equipment, User
from ..services import EquipmentService, UserPermissionError
from typing import List, Dict, Tuple

api = APIRouter(prefix="/api/equipment")


@api.get("", response_model=list[Equipment], tags=["Equipment"])
def list(equipment_svc: EquipmentService = Depends()):
    return equipment_svc.list()

@api.get("/{equipment_name}", tags=["Equipment"])
def list_schedule(equipment_name: str, equipment_svc: EquipmentService = Depends()):
    return equipment_svc.list_schedule(equipment_name)

@api.post("/edit/{equipment_name}", tags=["Equipment"])
def edit_deviations(user_pid: int, equipment_name: str, deviations: Dict[str, List[str]], equipment_svc: EquipmentService = Depends()):
    return equipment_svc.edit_deviations(user_pid, equipment_name, deviations)

@api.post("", tags=["Equipment"])
def add(user_pid: int, equipment: Equipment, equipment_svc: EquipmentService = Depends()) -> None:
    try:
        return equipment_svc.add(user_pid, equipment)
    except UserPermissionError:
        raise HTTPException(status_code=400, detail="Not authorized to perform this action")

@api.delete("/{equipment_name}", tags=["Equipment"])
def delete(user_pid: int, equipment_name: str, equipment_svc: EquipmentService = Depends()) -> None:
    try:
        equipment_svc.delete(user_pid, equipment_name)
    except UserPermissionError:
        raise HTTPException(status_code=400, detail="Not authorized to perform this action")