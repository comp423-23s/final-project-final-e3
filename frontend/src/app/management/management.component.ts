import { Component } from '@angular/core';
import { Route, Router } from '@angular/router';
import { Observable } from 'rxjs';
import { isAuthenticated } from '../gate/gate.guard';
import { ReservationsService, Room } from '../reservations.service';
import { ReservationsComponent } from '../reservations/reservations.component';
import { ManagementService } from '../management.service';
import { Form, FormBuilder } from '@angular/forms';
import { AddRoomComponent } from '../add-room/add-room.component';

@Component({
  selector: 'app-management',
  templateUrl: './management.component.html',
  styleUrls: ['./management.component.css']
})
export class ManagementComponent {
  public static Route: Route = {
    path: 'management',
    component: ManagementComponent, 
    title: 'Management', 
    canActivate: [isAuthenticated], 
  };

  public rooms$: Observable<Room[]>;
  public rName: string;

  public newRoomForm = this.formBuilder.group({
    room_name: '',
    room_capacity: '',
  });

  constructor(private reservationService: ReservationsService, private managementService: ManagementService, protected formBuilder: FormBuilder, protected router: Router){
    this.rooms$ = reservationService.list_of_rooms();
    this.rName = "";
  }

  setRoomName(roomName: string) {
    this.reservationService.setRoomName(roomName);
  }

  onClick(roomName: string): void {
    this.rName = roomName;
    this.managementService
          .deleteRoom(roomName)
          .subscribe({
            next: (room) => this.onSuccess(room)
          });
  }

  onSuccess(room: Room): void {
    window.alert(`${this.rName} has been deleted.`);
    window.location.reload();
  }
}
