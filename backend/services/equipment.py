"""Equipment services managing and changing equipments and their availability schedules"""

from ..database import db_session
from sqlalchemy import select, or_, func
from sqlalchemy.orm import Session
from fastapi import Depends
from ..models import Equipment
from ..entities import EquipmentEntity, UserEntity, RoleEntity
from sqlalchemy import select

class EquipmentService:

    _session: Session

    def __init__(self, session: Session = Depends(db_session)):
        self._session = session


    def list(self) -> list[Equipment]:
        """List all equipments"""
        statement = select(EquipmentEntity).order_by(EquipmentEntity.name)
        equipment_entities = self._session.execute(statement).scalars()
        return [equipment_entity.to_model() for equipment_entity in equipment_entities]

    
    def add(self, equipment: Equipment) -> str:
        """Staff adds an equipment into database"""
        equipment_entity = EquipmentEntity.from_model(equipment)
        self._session.add(equipment_entity)
        self._session.commit()
        return "Equipment added successfully"
    
    def delete(self, equipment_name: str):
        """Staff deletes an equipment specified by name from database"""
        equipment_to_delete = self._session.query(EquipmentEntity).filter_by(name=equipment_name).one()
        if equipment_to_delete is None:
            return "Equipment not found"
        self._session.delete(equipment_to_delete)
        self._session.commit()
        return "Equipment deleted successfully"